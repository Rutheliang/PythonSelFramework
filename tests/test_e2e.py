import pytest
from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
# chrome driver
from selenium.webdriver.chrome.service import Service
# chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait, expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

from pageObject.CheckoutPage import CheckoutPage
from pageObject.ConfirmPage import ConfirmPage
from pageObject.HomePage import HomePage
from utilities.BaseClass import BaseClass


# @pytest.mark.usefixtures("setup") # optimize in baseclass since this is use in every file
# make sure to call baseclass in this file (parent to child inheritance)

class TestOne(BaseClass):

    def test_e2e(self):

        #homePage = HomePage(self.driver)
        #homePage.shopItems().click()
        #checkoutPage = CheckoutPage(self.driver)
        #products = checkoutPage.getCardTitles()

        log = self.getLogger()

        homePage = HomePage(self.driver)
        checkoutPage = homePage.shopItems()

        log.info("getting all the card titles") # insert log

        # checkoutPage = CheckoutPage(self.driver) -> not required / skip creating object for your next class
        products = checkoutPage.getCardTitles()

        for product in products:
            productName = product.text
            log.info(productName)
            if productName == "Blackberry":
                checkoutPage.getCardFooter().click()

        self.driver.find_element(By.CSS_SELECTOR, "a[class='nav-link btn btn-primary']").click()

        checkoutPage.checkOutItems().click()
        confirmPage = ConfirmPage(self.driver)

        log.info("Entering country name as Ind")
        confirmPage.confirmItem().send_keys("ind")

        self.verifyLikPresence("India")

        #wait = WebDriverWait(self.driver, 10)
        #wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))

        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        successText = self.driver.find_element(By.CLASS_NAME, "alert-success").text

        log.info("Text received from application is " + successText)
        assert "Success! Thank you!" in successText  # use IN instead of equal for partial words
