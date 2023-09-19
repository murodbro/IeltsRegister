from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement



class Authentication:
    def __init__(self, driver: WebElement):
        self.driver = driver
        self.driver.implicitly_wait(10)

    def login(self):

        login_element = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'button[data-testid="go-to-LogIn"]')))
        login_element.click()


    def create_account(self, email, confirm_email, password):

        email_element = self.driver.find_element(By.CSS_SELECTOR, 'input[name="email"]')
        email_element.send_keys(email)
        email_element.send_keys(email)


        email_confirm = self.driver.find_element(By.ID, "confirmEmail-2")
        email_confirm.send_keys(confirm_email)

        password_element = self.driver.find_element(By.CSS_SELECTOR, 'input[type="password"]')
        password_element.send_keys(password)


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


    def personal_data(self, first_name, last_name, birthday, birthday_month, birthday_year):

        name_element = self.driver.find_element(By.ID, "firstName-3")
        name_element.send_keys(first_name)

        last_name_element = self.driver.find_element(By.CSS_SELECTOR, 'input[data-testid="last-name"]')
        last_name_element.send_keys(last_name)

        birthday_element = self.driver.find_element(By.ID, "dateOfBirth-4")
        birthday_element.send_keys(birthday)

        birthday_month_element = self.driver.find_element(By.CSS_SELECTOR, 'select[data-testid="dateSelectorMonth"]')
        birthday_month_element.send_keys(birthday_month)

        birthday_year_element = self.driver.find_element(By.CSS_SELECTOR, 'input[data-testid="dateSelectorYear"]')
        birthday_year_element.send_keys(birthday_year)


    def gender(self, male: bool = False, female: bool = False):

        if not(male == True and female == True):
            if male:
                male_element = self.driver.find_element(By.CSS_SELECTOR, 'input[data-testid="Male"]')
                male_element.click()
            elif female:
                female_element = self.driver.find_element(By.CSS_SELECTOR, 'input[data-testid="Female"]')
                female_element.click()
            else:
                print("Choose gender!")
        else:
            print("Choose only ones!")


    def contact_details(self, phone_number, home_country):

        phone_number_element = self.driver.find_element(By.ID, "mobile-number-id")
        phone_number_element.send_keys(phone_number)

        home_country_element = self.driver.find_element(By.XPATH, '//div[@id="select-country"]//div[@class="select-search__value"]//input')
        home_country_element.send_keys(home_country)
        home_country_element.send_keys(Keys.ARROW_DOWN)
        home_country_element.send_keys(Keys.RETURN)


    def address(self, viloyat, tuman, mfy, zip_code):

        viloyat_element = self.driver.find_element(By.ID, "addressLine1-5")
        viloyat_element.send_keys(viloyat)

        tuman_element = self.driver.find_element(By.ID, "addressLine2-6")
        tuman_element.send_keys(tuman)

        mfy_element = self.driver.find_element(By.ID, "addressLine3-7")
        mfy_element.send_keys(mfy)

        town = self.driver.find_element(By.ID, "town-8")
        town.send_keys(tuman)

        post_code = self.driver.find_element(By.ID, "postcode-9")
        post_code.send_keys(zip_code)


    def marketing_preference(self):

        dont_send = self.driver.find_element(By.CSS_SELECTOR, 'input[data-testid="marketing-bc-only"]')
        dont_send.click()

        agree_button = self.driver.find_element(By.ID, "acceptIeltsTermsAndConditions-10")
        agree_button.click()

        # button = self.driver.find_element(By.CSS_SELECTOR, 'input[data-testid="save-and-continue"]')
        continue_button = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[data-testid="save-and-continue"]')))
        continue_button.click()
