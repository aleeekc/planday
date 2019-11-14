import unittest
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from time import sleep
import random
from uuid import uuid4


class TestPayday(unittest.TestCase):
    def setUp(self):
        """ Tests are being run on Firefox """
        dir_path = os.path.dirname(os.path.realpath(__file__))
        executable_path = dir_path + "\\drivers\\geckodriver.exe"
        self.driver = webdriver.Firefox(executable_path=executable_path)

    def test_1(self):
        """ Run test case 1 """
        self.driver.get("https://www.planday.com/signup/signup")

        companyLabel = self.driver.find_element_by_id("companyLabel")
        assert companyLabel.text == 'Company name', "Wrong text in company label!"

        assert self.driver.find_element_by_id("company"), "Company field not present!"

        industry = self.driver.find_element_by_xpath(
            '/html/body/main/article/div/div[3]/div/div/form/div/div[4]/label')
        assert industry.text == 'Industry', "Wrong text in industry label!"
        Industry_selector = self.driver.find_element_by_id("Industry")

        number_of_employees = self.driver.find_element_by_xpath(
            '/html/body/main/article/div/div[3]/div/div/form/div/div[5]/label')
        assert number_of_employees.text == 'Number of employees', "Wrong text in number_of_employees label!"
        Number_of_employees_selector = self.driver.find_element_by_id("Number of employees")

        phoneLabel = self.driver.find_element_by_id("phoneLabel")
        assert phoneLabel.text == 'Phone number', "Wrong text in phoneLabel label!"
        phone_selector = self.driver.find_element_by_xpath(
            '/html/body/main/article/div/div[3]/div/div/form/div/div[6]/div[1]')

    def test_2(self):
        """ Run test case 2 """
        self.driver.get("https://www.planday.com/signup/signup")

        made_up_field = self.driver.find_element_by_id("Made Up Field")

    def test_3(self):
        """ Run test case 3 """
        # TODO: Check if all options are present
        self.driver.get("https://www.planday.com/signup/signup")

        number_of_employees_selector = Select(self.driver.find_element_by_id("Number of employees"))
        for options in number_of_employees_selector.options:
            assert options.text in ['Select', '1 - 9', '10 - 20', '21 - 40', '41 - 100', '+101'],\
                "Wrong \'Number of employees\' selector!"

    def test_4_and_5(self):
        """ Run test case 4 and 5"""
        self.driver.get("https://www.planday.com/signup/signup")
        sleep(3)

        email = self.driver.find_element_by_xpath("//*[@id=\'email\']")
        email.send_keys("THIS IS NOT AN EMAIL")

        fullname = self.driver.find_element_by_id("fullname")
        fullname.send_keys("1234567980")

        company = self.driver.find_element_by_id("company")
        company.send_keys("9876543210!@#$%^&*<>?)=(№")

        password = self.driver.find_element_by_id("password")
        password.send_keys("THE STRONGEST PASSWORD IN THE WORLD!@#$%^&*><?№–/:=%")

        submit = self.driver.find_element_by_xpath(
            '/html/body/main/article/div/div[3]/div/div/form/button')

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        submit.click()

        sleep(2)

        emailInvalid = self.driver.find_element_by_id("emailInvalid")
        assert emailInvalid.text == "This needs to be a valid email", "Wrong emailInvalid text"

        fullnameInvalid = self.driver.find_element_by_id("fullnameInvalid")
        assert fullnameInvalid.text == "No special characters, please", "Wrong fullnameInvalid text"

        companyInvalid = self.driver.find_element_by_id("companyInvalid")
        assert companyInvalid.text == "Please enter a valid company name", "Wrong companyInvalid text"

        industryInvalid = self.driver.find_element_by_id("industryInvalid")
        assert industryInvalid.text == "This field is required", "Wrong industryInvalid text"

        consentInvalid = self.driver.find_element_by_id("consentInvalid")
        assert consentInvalid.text == "This field is required", "Wrong consentInvalid text"

    def test_6_and_7_and_8(self):
        """ Run test case 6 and 7 and 8"""
        self.driver.get("https://www.planday.com/signup/signup")

        sleep(3)

        email = self.driver.find_element_by_xpath("//*[@id=\'email\']")
        test_email = "martinjosephbakewell" + str(random.randrange(1000000, 9999999)) + "@gmail.com"
        print("Test email: " + test_email)
        email.send_keys(test_email)

        fullname = self.driver.find_element_by_id("fullname")
        fullname.send_keys("Test Please Ignore")

        company = self.driver.find_element_by_id("company")
        company.send_keys("Test Please Ignore")

        industry = Select(self.driver.find_element_by_id("Industry"))
        industry.select_by_value('Bar, Pub & Nightclub')

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        number_of_employees_selector = Select(self.driver.find_element_by_id("Number of employees"))
        number_of_employees_selector.select_by_value('21 - 40')

        phone = self.driver.find_element_by_xpath("/html/body/main/article/div/div[3]/div/div/form/div/div[6]/div[1]/input")
        phone.send_keys("77777777")

        password = self.driver.find_element_by_id("password")
        test_password = str(uuid4()).replace("-", "")[:8]
        print("Password: " + str(test_password))
        password.send_keys(test_password)

        consent = self.driver.find_element_by_id("consentLabel")
        consent.click()

        submit = self.driver.find_element_by_xpath(
            '/html/body/main/article/div/div[3]/div/div/form/button')

        submit.click()

        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.url_changes("https://www.planday.com/uk/signup/signup/#/creating"))

    def TearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
