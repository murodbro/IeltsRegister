from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement



class Data:
    def __init__(self, driver:WebElement):
        self.driver = driver
        self.driver.implicitly_wait(10)

    
    def exam_date_ceated_user(self):
        venue_name = self.driver.find_element(By.CSS_SELECTOR, 'h3[data-testid="venue-title"]')
        address_venue = self.driver.find_element(By.CSS_SELECTOR, 'span[data-testid="venue-address"]')
        date_time = self.driver.find_element(By.CSS_SELECTOR, 'h3[data-testid="lrw-date"]')
        note = self.driver.find_element(By.CSS_SELECTOR, 'span[data-testid="lrw-arrival"]')

        speaking_venue = self.driver.find_element(By.CSS_SELECTOR, 'h3[data-testid="venue-title"]')
        speaking_address = self.driver.find_element(By.CSS_SELECTOR, 'span[data-testid="venue-address"]')
        speaking_datetime = self.driver.find_element(By.CSS_SELECTOR, 'h3[data-testid="speaking-date"]')
        speaking_note = self.driver.find_element(By.CSS_SELECTOR, 'span[data-testid="speaking-arrival"]')
        speaking_format = self.driver.find_element(By.CSS_SELECTOR, 'span[data-testid="speaking-format"]')

        print("Main exam: \n", venue_name.get_attribute('innerHTML'), "\n", address_venue.get_attribute('innerHTML'),
                        "\n", date_time.get_attribute('innerHTML'), "\n", note.get_attribute('innerHTML'))
        print("-" * 25)
        print("Speaking exam: \n", speaking_venue.get_attribute('innerHTML'), "\n", speaking_address.get_attribute('innerHTML'),
                             "\n", speaking_datetime.get_attribute('innerHTML'), "\n", speaking_note.get_attribute('innerHTML'),
                             "\n", speaking_format.get_attribute('innerHTML'))
        

    def exam_date_user(self):
        venue_name = self.driver.find_element(By.CSS_SELECTOR, 'h3[data-testid="venue-title"]')
        address_venue = self.driver.find_element(By.CSS_SELECTOR, 'span[data-testid="venue-address"]')
        date_time = self.driver.find_element(By.CSS_SELECTOR, 'h3[data-testid="lrw-date"]')
        note = self.driver.find_element(By.CSS_SELECTOR, 'span[data-testid="lrw-arrival"]')

        speaking_venue = self.driver.find_element(By.CSS_SELECTOR, 'h3[data-testid="venue-title"]')
        speaking_address = self.driver.find_element(By.CSS_SELECTOR, 'span[data-testid="venue-address"]')
        speaking_datetime = self.driver.find_element(By.CSS_SELECTOR, 'h3[data-testid="speaking-date"]')
        speaking_note = self.driver.find_element(By.CSS_SELECTOR, 'span[data-testid="speaking-arrival"]')
        speaking_format = self.driver.find_element(By.CSS_SELECTOR, 'span[data-testid="speaking-format"]')

        print("Main exam: \n", venue_name.get_attribute('innerHTML'), "\n", address_venue.get_attribute('innerHTML'),
                        "\n", date_time.get_attribute('innerHTML'), "\n", note.get_attribute('innerHTML'))
        print("-" * 25)
        print("Speaking exam: \n", speaking_venue.get_attribute('innerHTML'), "\n", speaking_address.get_attribute('innerHTML'),
                            "\n", speaking_datetime.get_attribute('innerHTML'), "\n", speaking_note.get_attribute('innerHTML'),
                            "\n", speaking_format.get_attribute('innerHTML'))



