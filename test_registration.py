from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# Initialize ChromeDriver
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

try:
    driver.get("http://localhost:31096")  # Replace with correct port

    # Fill the form
    wait.until(EC.presence_of_element_located((By.NAME, "full_name"))).send_keys("Test User")
    driver.find_element(By.NAME, "email").send_keys("test_user@gmail.com")
    driver.find_element(By.NAME, "username").send_keys("testuser123")
    driver.find_element(By.NAME, "password").send_keys("password123")
    driver.find_element(By.NAME, "confirm_password").send_keys("password123")
    driver.find_element(By.NAME, "phone").send_keys("9876543210")
    driver.find_element(By.NAME, "dob").send_keys("2000-01-01")
    driver.find_element(By.NAME, "gender").send_keys("Male")
    driver.find_element(By.NAME, "address").send_keys("Hyderabad, India")

    # Scroll the submit button into view and click safely
    submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    actions = ActionChains(driver)
    actions.move_to_element(submit_button).click().perform()

    # Wait for some confirmation or just sleep
    wait.until(EC.url_changes("http://localhost:31096"))  # Optional: wait until page redirects
    print("Test Completed Successfully!")

finally:
    driver.quit()
