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
            '//div[@id="select-yearsOfStudyingEnglish"]//div[@class="select-search__value"]//input[@class="select-search__input"]')
        studing_year_element.send_keys(studing_year)
        studing_year_element.send_keys(Keys.ARROW_DOWN)
        studing_year_element.send_keys(Keys.RETURN)

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

    def occupation(self, country, default = "Other"):

        occupation_level_element = self.driver.find_element(By.XPATH,
            '//div[@id="select-occupationLevel"]//div[@class="select-search__value"]//input[@class="select-search__input"]')
        occupation_level_element.send_keys(default)
        occupation_level_element.send_keys(Keys.ARROW_DOWN)
        occupation_level_element.send_keys(Keys.RETURN)

        occupation_sector_element = self.driver.find_element(By.XPATH,
            '//div[@id="select-occupationSector"]//div[@class="select-search__value"]//input[@class="select-search__input"]')
        occupation_sector_element.send_keys(default)
        occupation_sector_element.send_keys(Keys.ARROW_DOWN)
        occupation_sector_element.send_keys(Keys.RETURN)

        interest = self.driver.find_element(By.XPATH,
            '//div[@id="select-reasonForTakingTest"]//div[@class="select-search__value"]//input[@class="select-search__input"]')
        interest.send_keys(default)
        interest.send_keys(Keys.ARROW_DOWN)
        interest.send_keys(Keys.RETURN)

        country_element = self.driver.find_element(By.XPATH,
            '//div[@id="select-countryBeingApplied"]//div[@class="select-search__value"]//input[@class="select-search__input"]')
        country_element.send_keys(country)
        country_element.send_keys(Keys.ARROW_DOWN)
        country_element.send_keys(Keys.RETURN)


    def button_pr(self):
         
        button_element = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR,
            'button[data-testid="save-and-continue"]')))
        button_element.click()
 