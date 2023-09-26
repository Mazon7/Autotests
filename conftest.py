import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    # Initialize the WebDriver (e.g., Chrome, Firefox, etc.)
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'eager' # for not waiting the web page fully downloads
    # options.headless = True
    # options.add_argument('--disable-gpu')
    options.add_argument('--headless')
    # options.add_argument('--no-sandbox')
    # options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)

    driver.get('https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all')

    # Optional: You can maximize the browser window for better visibility
    # driver.maximize_window()
    
    # Make sure to quit the WebDriver when the test is done
    yield driver

    # Close the browser window and cleanup after the test
    driver.quit()


# Fixture to restore DB by clicking on button and alert pop-up
@pytest.fixture
def restor_db(driver):
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, "#restoreDBBtn").click()
    # Switch to the alert
    alert = driver.switch_to.alert
    # Accept (click OK) the alert
    alert.accept()
    time.sleep(3) # wait for the frontend to show notification about restoring DB