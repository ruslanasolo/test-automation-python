# Open browser
# selenium 4
import time

import pytest
from selenium.webdriver.common.by import By

from page_objects.logged_in_successfully import LoggedInSuccessfullyPage
from page_objects.login_page import LoginPage


class TestPositiveScenarios:

    @pytest.mark.login
    @pytest.mark.positive
    def test_positive_login(self, driver):
        login_page = LoginPage(driver)

        # open page
        login_page.open()

        # Type username student into Username field
        # Type password Password123 into Password field
        # Push Submit button
        login_page.execute_login("student", "Password123")

        logged_in_page = LoggedInSuccessfullyPage(driver)
        assert logged_in_page.expected_url == logged_in_page.current_url, "Actual URL is not the same as expected"
        assert logged_in_page.header == "Logged In Successfully", "header is not expected"
        assert logged_in_page.is_logout_button_displayed(), "Logout button should be visible"

        # # Go to webpage
        # driver.get("https://practicetestautomation.com/practice-test-login/")
        # time.sleep(2)
        # driver.close()
        #
        # # Type username student into Username field
        # username_locator = driver.find_element(By.ID, "username")
        # username_locator.send_keys("student")
        #
        # # Type password Password123 into Password field
        # password_locator = driver.find_element(By.NAME, "password")
        # password_locator.send_keys("Password123")
        #
        # # Push Submit button
        # submit_button_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
        # submit_button_locator.click()
        # time.sleep(2)
        #
        # # Verify new page URL contains practicetestautomation.com/logged-in-successfully/
        # actual_url = driver.current_url
        # assert actual_url == "https://practicetestautomation.com/logged-in-successfully/"
        #
        # # Verify new page contains expected text ('Congratulations' or 'successfully logged in')
        # text_locator = driver.find_element(By.TAG_NAME, "h1")
        # actual_text = text_locator.text
        # assert actual_text == "Logged In Successfully"
        #
        # # Verify button Log out is displayed on the new page
        # log_out_button_locator = driver.find_element(By.LINK_TEXT, "Log out")
        # assert log_out_button_locator.is_displayed()