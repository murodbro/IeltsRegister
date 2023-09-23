import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from register import constants as const
from register.create_account import Authentication
from register.login import LoginUser
from register.profile import Profile


class Register(webdriver.Firefox):
    # def __init__(self):
    #     options = webdriver.ChromeOptions()
    #     super().__init__(options=options)


    def get_url(self):
        self.get(const.BASE_URL)
        self.implicitly_wait(10)
    

    def booking_test(self):
        try:
            cookie = self.find_element(By.ID, "onetrust-accept-btn-handler")
            cookie.click()
        except Exception as e:
            print(e)
        time.sleep(3)
        academic_ielts = self.find_element(By.ID, "select-ac")
        academic_ielts.click()
        self.implicitly_wait(10)
    

    def search_box(self, country, city):
        country_search = WebDriverWait(self, 45).until(EC.element_to_be_clickable((By.CLASS_NAME, "select-search__input")))
        country_search.clear()
        country_search.send_keys(country)
        country_search.send_keys(Keys.ARROW_DOWN)
        country_search.send_keys(Keys.RETURN)

        city_search = WebDriverWait(self, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "select-search__input")))
        city_search.clear()
        city_search.send_keys(city)
        city_search.send_keys(Keys.ARROW_DOWN)
        city_search.send_keys(Keys.RETURN)
    

    def type_of_format(self, paper: bool = True, computer: bool = False):
        if paper:
            paper_element = self.find_element(By.CSS_SELECTOR, 'input[data-testid="paper-based"]')
            paper_element.click()
        elif computer:
            computer_element = self.find_element(By.CSS_SELECTOR, 'input[data-testid="computer-delivered"]')
            computer_element.click()


    def choose_all_days(self):
        button = self.find_element(By.CSS_SELECTOR, 'input[data-testid="all-dates"]')
        button.click()


    def search_button(self):
        button = self.find_element(By.CSS_SELECTOR, 'button[data-testid="search-for-tests"]')
        button.click()
        self.implicitly_wait(10)
    

    def date_of_test(self, test_day: int, test_month: str, test_year: int):

        all_dates = []
        cases = True
        all_elements = self.find_element(By.CLASS_NAME, "app-contents")
        exam_days = all_elements.find_elements(By.CSS_SELECTOR, 'h3[data-testid="lrw-date"]')

        for day in exam_days:
            date_list = day.get_attribute('innerHTML').strip().split(" ")
            exam_day = int(date_list[0].strip())
            exam_month = date_list[1].strip()
            exam_year = int(date_list[2].strip().replace(",", ""))
            all_dates.append([exam_day, exam_month, exam_year])

        for index, date in enumerate(all_dates):
            if date[0] == test_day and date[1] == test_month and date[2] == test_year:
                cases = False
                click_buttons = self.find_elements(By.CLASS_NAME, "css-1gklrnv")

                for num, element in enumerate(click_buttons):
                    if num == index:
                        click_button = element.find_element(By.CSS_SELECTOR, 'button[data-testid="btn-book"]')
                        click_button.click()
        if cases:
            print("Bunday sanada imtihon mavjud emas!")

        time.sleep(3)

    
    def user_authentication(self):

        self.implicitly_wait(15)
        user_auth = Authentication(driver=self)
        user_auth.create_account(email=const.EMAIL, confirm_email=const.EMAIL, password=const.PASSWORD)
        self.implicitly_wait(10)
        user_auth.booking_for(myself=True)
        user_auth.personal_data(first_name=const.NAME, last_name=const.LAST_NAME,
                                birthday=const.BIRTHDAY, birthday_month=const.BIRTHDAY_MONTH, birthday_year=const.BIRTHDAY_YEAR)
        user_auth.gender(male=True)
        user_auth.contact_details(phone_number=const.PHONE_NUMBER, home_country=const.COUNTRY)
        user_auth.address(tuman=const.TUMAN, viloyat=const.VILOYAT, mfy=const.MFY, zip_code=const.ZIP)
        user_auth.marketing_preference()
        user_auth.save_button()


    def login_user(self):

        self.implicitly_wait(15)
        user_login = LoginUser(driver=self)
        user_login.login_button()
        user_login.login(email=const.EMAIL, password=const.PASSWORD)
        user_login.booking_for(myself=True)
        time.sleep(2)
        user_login.continue_button()
        user_login.identification_details(passport=True)
        user_login.identification(day=const.EXPIRE_DAY, month=const.EXPIRE_MONTH, year=const.EXPIRE_YEAR,
            number=const.PASSPORT, issuing=const.ISSUING_AUTH, nation=const.COUNTRY)
        time.sleep(2)
        user_login.upload_image(path="D:\doc\passport.jpg")
        user_login.button()


    def prifile_details(self):

        self.implicitly_wait(15)
        profile = Profile(driver=self)
        profile.about(language=const.LANGUAGE, studing_year=const.STUDING_YEAR, education_level=const.SECONDARY)
        profile.occupation(country=const.COUNTRY)
        time.sleep(1)
        profile.button_pr()

    
    def check_account(self, email):

        email_element = self.find_element(By.CSS_SELECTOR, 'input[name="email"]')
        email_element.send_keys(email)
        email_confirm = self.find_element(By.ID, "confirmEmail-2")
        email_confirm.click()
        exist = False

        try:
            login_element = WebDriverWait(self, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-testid="go-to-LogIn"]')))
            exist = True
            login_element.click()
        
        except Exception as e:
            print(str(e))

        if exist:
            Register.login_user(self=self)
            Register.prifile_details(self=self)
        
        else:
            Register.user_authentication(self=self)





