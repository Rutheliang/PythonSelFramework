from selenium.webdriver.common.by import By


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    cardFooter = (By.CSS_SELECTOR, ".card-footer")
    checkOut = (By.CSS_SELECTOR, "button[class='btn btn-success']")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)
        # driver.find_elements(By.XPATH, "//div[@class='card h-100']")

    def getCardFooter(self):
        return self.driver.find_element(*CheckoutPage.cardFooter)
        # driver.find_element(By.CSS_SELECTOR, ".card-footer").click()

    def checkOutItems(self):
        return self.driver.find_element(*CheckoutPage.checkOut)
        #driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-success']")

