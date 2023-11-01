from lib2to3.pgen2 import driver

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from pageObject.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        log = self.getLogger()

        homepage = HomePage(self.driver)

        log.info("first name is "+getData["firstname"]) # insert log
        homepage.getName().send_keys(getData["firstname"])
        # homepage.getName().send_keys(getData[0])
        homepage.getEmail().send_keys(getData["lastname"])
        homepage.getPw().send_keys("1232332")
        homepage.getCheckbox().click()

        self.selectOptionByText(homepage.getGender(), getData["gender"])

        # Static Dropdown
        # dropdown = Select(homepage.getGender()) # -> move to baseclass
        # dropdown.select_by_visible_text("Female")

        self.driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        message = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        print(message)
        assert "Success" in message

        self.driver.refresh() # it will open a new browser to enter the second set of data

    # will not put in conftest coz it's not use in all test cases
    # use dictionary instead of tuple
    # use can use also key value pair - dictionary -> [{"firstname":"Ruthel","lastname":"Villa", "gender":"Female"}]

    #@pytest.fixture(params=[("Ruthel", "Villa", "Female"), ("Mark", "Insong","Male")])
    #def getData(self, request):
    #    return request.param

    @pytest.fixture(params=HomePageData.test_HomePage_Data)
    def getData(self, request):
        return request.param
