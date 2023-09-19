import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement



class LoginUser:
    def __init__(self, driver:WebElement):
        self.driver = driver
        self.driver.implicitly_wait(10)

    
    def login_button(self):

        button = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, 
                '//div[@data-testid="page-container"]//div[@class="bc-quote bc-quote-gray css-djt9ab"]//button[@class="btn-link link link"]')))
        button.click()

    
    def login(self, email, password):

        email_element = self.driver.find_element(By.ID, "login-field")
        email_element.send_keys(email)

        password_element = self.driver.find_element(By.ID, "password_login")
        password_element.send_keys(password)

        button = self.driver.find_element(By.ID, "btn-login")
        button.click()


    def booking_for(self, myself: bool = False, my_child: bool = False):

        if not(myself == True and my_child == True):

            if myself:
                myself_element = self.driver.find_element(By.CSS_SELECTOR, 'input[data-testid="for-myself"]')
                myself_element.click()

            elif my_child:
                my_child_element = self.driver.find_element(By.CSS_SELECTOR, 'input[data-testid="new-child"]')
                my_child_element.click()

            else:
                print("Choose one of this: myself or my_child")
        else:
            print("Choose only ones!")


    def continue_button(self):
        time.sleep(3)
        button = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH,
                                '//div[@data-testid="page-container"]//button[@data-testid="save-and-continue"]')))
        button.click()

    
    def identification_details(self, passport: bool = True, id: bool = False):
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

        number_element = self.driver.find_element(By.ID, "id-number")
        number_element.clear()
        number_element.send_keys(number)

        day_element = self.driver.find_element(By.ID, "expiryDate-7")
        day_element.send_keys(day)

        month_element = self.driver.find_element(By.CSS_SELECTOR, 'select[data-testid="dateSelectorMonth"]')
        month_element.send_keys(month)

        year_element = self.driver.find_element(By.CSS_SELECTOR, 'input[data-testid="dateSelectorYear"]')
        year_element.send_keys(year)

        issuing_auth = self.driver.find_element(By.ID, "issuingAuthority-8")
        issuing_auth.clear()
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

        remove_file = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH,
                '//div[@data-testid="upload-back"]//div[@class]//div[@class]//div[@class]//button[@class="btn-link link"]')))
        time.sleep(3)
        if remove_file:
            print("ishladi")
            remove_file.click()


        # try:
        #     remove_file = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH,
        #         '//div[@data-testid="upload-back"]//div[@class]//div[@class]//div[@class]//button[@class="btn-link link"]')))
        #     print("ishladi")
        #     remove_file.click()

        # except Exception as e:
        #     print(e)
        #     print("ishlamadi")


        # time.sleep(3)
        # continue_button = self.driver.find_element(By.XPATH,
        #     '//div[@data-testid="page-container"]//button[@data-testid="save-and-continue"]')
        # continue_button.click()

        # confirmation = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR,
        #                             'button[data-testid="confirm-modal-submit"]')))
        # confirmation.click()





        