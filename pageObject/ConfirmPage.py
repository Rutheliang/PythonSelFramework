from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    confirm = (By.ID, "country")

    def confirmItem(self):
        return self.driver.find_element(*ConfirmPage.confirm)
        # driver.find_element(By.ID, "country").send_keys("ind")
