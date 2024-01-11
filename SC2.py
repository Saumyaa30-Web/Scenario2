from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Function to set up the WebDriver
def setup_webdriver():
    # Use appropriate webdriver path (e.g., chromedriver.exe for Chrome)
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

# Test Scenario 2
def test_scenario_2(search_string):
    # Step 1: Open ebay.com
    driver.get("https://www.ebay.com")

    # Step 2: Type any search string in the search bar
    search_bar = driver.find_element(By.ID, "gh-ac")
    search_bar.send_keys(search_string)

    # Step 3: Change the Search category to Computers/Tablets & Networking and click Search
    category_dropdown = driver.find_element(By.ID, "gh-cat")
    category_dropdown.send_keys("Computers/Tablets & Networking", Keys.RETURN)

    # Step 4: Verify that the page loads completely
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "s-results-list-atf")))

    # Step 5: Verify that the first result name matches with the search string
    first_result_name = driver.find_element(By.XPATH, "//li[@id='srp-river-results-listing1']//h3").text
    assert search_string.lower() in first_result_name.lower(), f"Search string '{search_string}' not found in the first result"

    print("Scenario 2: Test Passed!")

# Execute the test
search_string = "MacBook"
driver = setup_webdriver()
test_scenario_2(search_string)
driver.quit()
