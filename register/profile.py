from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement



class Profile:
    def __init__(self, driver:WebElement):
        self.driver = driver
        self.driver.implicitly_wait(10)


    def about(self, language, studing_year, education_level):
        
        language_element = self.driver.find_element(By.XPATH,
            '//div[@id="select-mainLanguageSpoken"]//div[@class="select-search__value"]//input[@class="select-search__input"]')
        language_element.send_keys(language)
        language_element.send_keys(Keys.ARROW_DOWN)
        language_element.send_keys(Keys.RETURN)

        studing_year_element = self.driver.find_element(By.XPATH,
            '//div[@id="select-yearsOfStudyingEnglish"]//div[@id="select-yearsOfStudyingEnglish"]//input[@class="select-search__input"]')
        language_element.send_keys(studing_year)
        language_element.send_keys(Keys.ARROW_DOWN)
        language_element.send_keys(Keys.RETURN)

        if education_level == "Secondary_up_to_16":
            education_level_element = self.driver.find_element(By.XPATH,
                '//div[@data-testid="page-container"]//div[@class="form-group"]//input[@data-testid="edu-level-384"]')
            education_level_element.click()
            
        elif education_level == "Secondary":
            education_level_element = self.driver.find_element(By.XPATH,
                '//div[@data-testid="page-container"]//div[@class="form-group"]//input[@data-testid="edu-level-385"]')
            education_level_element.click()
            
        elif education_level == "Degree":
            education_level_element = self.driver.find_element(By.XPATH,
                '//div[@data-testid="page-container"]//div[@class="form-group"]//input[@data-testid="edu-level-386"]')
            education_level_element.click()
            
        elif education_level == "Postgraduate":
            education_level_element = self.driver.find_element(By.XPATH,
                '//div[@data-testid="page-container"]//div[@class="form-group"]//input[@data-testid="edu-level-387"]')
            education_level_element.click()
