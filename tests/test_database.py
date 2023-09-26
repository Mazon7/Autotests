from selenium.webdriver.common.by import By
import re
import time
from constants import *


class TestDatabase:
    def test_first(self, driver, restor_db):

        # Set editor value
        editor_value = CommonMethods.set_editor_value(CommonMethods.get_customers)

        # Execute the JavaScript code
        driver.execute_script(editor_value)

        driver.find_element(By.CSS_SELECTOR, 'button[class="ws-btn"]').click()

        table_headers_elements = driver.find_elements(By.CSS_SELECTOR, "table[class^='ws-table-all'] tbody tr th")
        table_headers = [i.text for i in table_headers_elements]

        # Get Cell element of ContactName that has value of "Giovanni Rovelli"
        cell_element = driver.find_element(By.XPATH, f"//*[starts-with(@class, 'ws-table-all')]/tbody/tr/td[{table_headers.index('ContactName')+1}][text()='Giovanni Rovelli']")

        row_cell_values = cell_element.find_element(By.XPATH, "..").find_elements(By.TAG_NAME, "td")
        cell_values = [i.text for i in row_cell_values]

        # Assertion that column 'Address' has the value 'Via Ludovico il Moro 22'
        assert table_headers.index('Address') == cell_values.index('Via Ludovico il Moro 22'), 'Other value is specified for Address column!'


    def test_second(self, driver, restor_db):
        
        # Set editor value
        editor_value = CommonMethods.set_editor_value(SecondTest.sql_query)

        # Execute the JavaScript code
        driver.execute_script(editor_value)

        driver.find_element(By.CSS_SELECTOR, 'button[class="ws-btn"]').click()

        records_number_element = driver.find_element(By.CSS_SELECTOR, "#divResultSQL div div").text

        # Number of rows excluding Header
        rows = driver.find_elements(By.CSS_SELECTOR, "table[class^='ws-table-all'] tbody tr")[1:]

        # Meaning that we know that our expected result is a 1 digit
        records_number = re.search(r'\d', records_number_element)[0]

        # Alternative method
        # int(records_number.split(":")[1].strip())

        # Assert that number of record equals 6 (Notification number equals to the number of rows in the table)
        assert len(rows) == int(records_number)


    def test_third(self, driver, restor_db):

        # Set editor value
        editor_value = CommonMethods.set_editor_value(ThirdTest.sql_query)

        # Execute the JavaScript code
        driver.execute_script(editor_value)

        driver.find_element(By.CSS_SELECTOR, 'button[class="ws-btn"]').click()

        # Check that notification appears
        change_notification = driver.find_element(By.CSS_SELECTOR, "#divResultSQL div").text

        assert "Rows affected: 1" in change_notification

        # Set editor value to check added data
        editor_value_updated = CommonMethods.set_editor_value(CommonMethods.get_customers)
        # Execute the JavaScript code
        driver.execute_script(editor_value_updated)

        last_row_elements = driver.find_elements(By.CSS_SELECTOR, "table[class^='ws-table-all'] tbody tr:nth-last-child(1) td")

        # Last Row Cell values
        last_row_values = [i.text for i in last_row_elements]

        # Assert added record values with the Values for SQL query
        for cell_vaue, row_value  in zip(ThirdTest.record_values, last_row_values):
            assert cell_vaue == row_value


    def test_fourth(self, driver, restor_db):

        # Set editor value
        editor_value = CommonMethods.set_editor_value(FourTest.sql_query)

        # Execute the JavaScript code
        driver.execute_script(editor_value)

        driver.find_element(By.CSS_SELECTOR, 'button[class="ws-btn"]').click()

        # Check that notification appears
        change_notification = driver.find_element(By.CSS_SELECTOR, "#divResultSQL div").text

        assert "Rows affected: 1" in change_notification

        # Set editor value to check added data
        editor_value_updated = CommonMethods.set_editor_value(CommonMethods.get_customers)
        # Execute the JavaScript code
        driver.execute_script(editor_value_updated)

        driver.find_element(By.CSS_SELECTOR, 'button[class="ws-btn"]').click()

        last_row_elements = driver.find_elements(By.CSS_SELECTOR, "table[class^='ws-table-all'] tbody tr:nth-child(1) td")

        # Last Row Cell values
        last_row_values = [i.text for i in last_row_elements]

        # Assert added record values with the Values for SQL query
        for cell_vaue, row_value  in zip(FourTest.record_values, last_row_values):
            assert cell_vaue == row_value


    # Create View for Order table and Assert the Employee that processed max number of orders
    def test_fifth(self, driver, restor_db):

        # Set editor value
        editor_value = CommonMethods.set_editor_value(FifthTest.orders_view)

        # Execute the JavaScript code
        driver.execute_script(editor_value)

        driver.find_element(By.CSS_SELECTOR, 'button[class="ws-btn"]').click()

        # Check that notification appears
        change_notification = driver.find_element(By.CSS_SELECTOR, "#divResultSQL div").text
        assert "You have made changes to the database." in change_notification

        views_section_element = driver.find_element(By.CSS_SELECTOR, "#yourRC")
        view_name_element = views_section_element.find_element(By.XPATH, ".//td[contains(text(), 'OrdersNew')]")

        # Assert that View has been created
        assert view_name_element

        # Set editor value to check added data
        editor_value_updated = CommonMethods.set_editor_value(FifthTest.count_orders)
        # Execute the JavaScript code
        driver.execute_script(editor_value_updated)

        driver.find_element(By.CSS_SELECTOR, 'button[class="ws-btn"]').click()

        first_row_elements = driver.find_elements(By.CSS_SELECTOR, "table[class^='ws-table-all'] tbody tr:nth-child(2) td")
        
        # First Row Cell values
        first_row_values = [i.text for i in first_row_elements]
        
        # Assert that Margaret Peacock has been processed that most orders and order numbers equal 40
        assert first_row_values[0] == "Margaret Peacock"
        assert int(first_row_values[1]) == 40