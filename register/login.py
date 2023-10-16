import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver



class LoginUser:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.driver.implicitly_wait(10)


    def login_button(self):

        button = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, 
                '//div[@data-testid="page-container"]//div[@class="bc-quote bc-quote-gray css-djt9ab"]//button[@class="btn-link link link"]')))
        time.sleep(1)
        button.click()

    
    def login(self, email, password):

        email_element = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.ID, "login-field")))
        email_element.send_keys(email)

        password_element = self.driver.find_element(By.ID, "password_login")
        password_element.send_keys(password)

        button = self.driver.find_element(By.ID, "btn-login")
        button.click()


    def booking_for(self, myself: bool = False, my_child: bool = False):
        self.driver.implicitly_wait(15)

        if not(myself == True and my_child == True):

            if myself:
                myself_element = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-testid="for-myself"]')))
                myself_element.click()
                myself_element.click()

            elif my_child:
                my_child_element = self.driver.find_element(By.CSS_SELECTOR, 'input[data-testid="new-child"]')
                my_child_element.click()

            else:
                print("Choose one of this: myself or my_child")
        else:
            print("Choose only ones!")


    def continue_button(self):
        self.driver.implicitly_wait(15)
        time.sleep(3)
        button = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH,
                                '//div[@data-testid="page-container"]//button[@data-testid="save-and-continue"]')))
        button.click()

    
    def identification_details(self, passport: bool = True, id: bool = False):
        self.driver.implicitly_wait(15)
        if not(passport == True and id == True):

            if passport:
                passport_element = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                    'input[data-testid="Passport (Mandatory for foreign citizens. Local Passport optional for local citizens)"]')))
                passport_element.click()

            elif id:
                id_element = self.driver.find_element(By.CSS_SELECTOR,
                    'input[data-testid="ID Karta (O\'zbekiston Respublikasi Shaxs Guvohnomasi)"]')
                id_element.click()
    

    def identification(self, number, day, month, year, issuing, nation):
        self.driver.implicitly_wait(15)

        number_element = self.driver.find_element(By.ID, "id-number")
        number_element.send_keys(Keys.CONTROL + "a")
        number_element.send_keys(Keys.DELETE)
        number_element.send_keys(number)

        day_element = self.driver.find_element(By.ID, "expiryDate-7")
        day_element.send_keys(day)

        month_element = self.driver.find_element(By.CSS_SELECTOR, 'select[data-testid="dateSelectorMonth"]')
        month_element.send_keys(month)

        year_element = self.driver.find_element(By.CSS_SELECTOR, 'input[data-testid="dateSelectorYear"]')
        year_element.send_keys(year)

        issuing_auth = self.driver.find_element(By.ID, "issuingAuthority-8")
        issuing_auth.send_keys(Keys.CONTROL + "a")
        issuing_auth.send_keys(Keys.DELETE)
        issuing_auth.send_keys(issuing)

        nationality = self.driver.find_element(By.XPATH,
            '//div[@id="select-country"]//div[@class="select-search__value"]//input[@class="select-search__input"]')
        nationality.send_keys(nation)
        nationality.send_keys(Keys.ARROW_DOWN)
        nationality.send_keys(Keys.RETURN)

    
    def upload_image(self, path):

        choose_button = self.driver.find_element(By.XPATH,
            '//div[@class="uppy-Root uppy-FileInput-container"]//input[@class="uppy-FileInput-input"]')
        choose_button.clear()
        choose_button.send_keys(path)

        try:
            time.sleep(3)
            remove_file = WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.XPATH,
                    '//div[@data-testid="upload-back"]//button[@class="btn-link link"]')))
            exist = True
            time.sleep(2)
            if exist:
                remove_file.click()
            time.sleep(2)
        except Exception as e:
            print(str(e))


    def button(self):

        continue_button = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH,
            '//div[@data-testid="page-container"]//button[@data-testid="save-and-continue"]')))
        continue_button.click()

        confirmation = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                    'button[data-testid="confirm-modal-submit"]')))
        confirmation.click()

