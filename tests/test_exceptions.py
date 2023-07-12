from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestException:

    @pytest.mark.exceptions
    def test_no_such_element_exception(self, driver):
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()

        wait = WebDriverWait(driver, 10)
        row_2_input_locator = wait.until(ec.presence_of_element_located((By.XPATH, "//div[@id='row2']/input")))

        assert row_2_input_locator.is_displayed(), "Row 2 input should be displayed, but it's not"

    @pytest.mark.exceptions
    @pytest.mark.debug
    def test_element_not_interactable_exception(self, driver):
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()

        wait = WebDriverWait(driver, 10)
        row_2_input_locator = wait.until(ec.presence_of_element_located((By.XPATH, "//div[@id='row2']/input")))
        row_2_input_locator.send_keys("Sushi")

        save_button = driver.find_element(By.NAME, "Save")
        save_button.click()

        # verify text saved
        confirmation_element = wait.until(ec.visibility_of_element_located((By.ID, "confirmation")))
        confirmation_message = confirmation_element.text
        assert confirmation_message == "Row 2 was saved", "Confirmation message is not expected"

    @pytest.mark.exceptions
    @pytest.mark.debug
    def test_element_not_interactable_exception(self, driver):
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # clear input field
        row_1_edit_btn = driver.find_element(By.ID, "edit_btn")
        row_1_edit_btn.click()

        row_1_input_element = driver.find_element(By.XPATH, "//div[@id='row1']/input")
        wait = WebDriverWait(driver, 10)
        wait.until(ec.element_to_be_clickable(row_1_input_element))
        row_1_input_element.clear()

        # Type text into the input field
        row_1_input_element.send_keys("Sushi")

        row_1_save_btn = driver.find_element(By.ID, "save_btn")
        row_1_save_btn.click()

        # verify text saved
        confirmation_element = wait.until(ec.visibility_of_element_located((By.ID, "confirmation")))
        confirmation_message = confirmation_element.text
        assert confirmation_message == "Row 1 was saved", "Confirmation message is not expected"

        # verify text changed
        text = row_1_input_element.get_attribute("value")
        assert text == "Sushi", "expected Sushi, but get " + text

    @pytest.mark.exceptions
    @pytest.mark.debug
    def test_stale_element_reference_exception(self, driver):
        # open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # find instructions text element
        instruction_element = driver.find_element(By.ID, "instructions")

        # click button "Add"
        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()

        # verify instruction text element is no longer displayed
        wait = WebDriverWait(driver, 10)
        assert wait.until(ec.invisibility_of_element_located(
            (By.ID, "instructions")), "Instructions text should not be displayed")

    @pytest.mark.exceptions
    @pytest.mark.debug
    def test_timeout_exception(self, driver):
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()

        wait = WebDriverWait(driver, 3)
        row_2_input_locator = wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@id='row2']/input")),
                                         "Failed waiting for Row 2 input to be visible")

        assert row_2_input_locator.is_displayed(), "Row 2 input should be displayed, but it's not"

