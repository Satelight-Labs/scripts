from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


import time
import csv

# Initialize the WebDriver (ensure you have the correct path to your WebDriver)
# driver_path = 'path/to/your/webdriver'
# driver = webdriver.Chrome()

profile_path = 'C:\\Users\\Vijay\\AppData\\Local\\Google\\Chrome\\User Data'
# profile_path = 'C:\\Users\\Vijay\\Documents\\Satelight Labs Local\\Scripts\\vikramdata'

# URL of the website to scrape
chrome_options = Options()
chrome_options.add_argument("user-data-dir=" + profile_path)
chrome_options.add_argument(f"profile-directory=Profile 1")
chrome_options.add_argument("--no-sandbox")  # Added to prevent some sandboxing issues
chrome_options.add_argument("--disable-dev-shm-usage")  # Added to prevent some shared memory issues
chrome_options.add_argument("--disable-extensions")  # Disable extensions
chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration
# chrome driver is in the same directory as this script, set the path to the driver
chrome_options.add_argument("--remote-debugging-port=9222")  # Ensure this is set to avoid port conflict

chrome_options.add_argument("--enable-logging")
chrome_options.add_argument("--v=1")

service = Service()

driver = webdriver.Chrome(service=service, options=chrome_options)

time.sleep(1)

def typeEmail(email):
        actions = ActionChains(driver)
        actions.send_keys(email)
        actions.perform()

        time.sleep(0.5)
        # enter action to select the email
        enterAction = ActionChains(driver)
        enterAction.send_keys(Keys.ENTER)
        enterAction.perform()

url = "https://app.hubspot.com/live-messages/46304105"
driver.get(url)

emails = ["emailmaria@hubspot.com","kirandas123@gmail.com","vijaysambamurthy@gmail.com"]


for email in emails:
    input(f"Press Enter to continue... Email: {email}")
    button = driver.find_element(By.CSS_SELECTOR, '[data-test-id="compose-email-button"]')
    button.click()

    time.sleep(0.2)

    try:

        emailElem = driver.find_element(By.XPATH, '//*[text()="Enter or choose a recipient"]')
        emailElem.click()

        typeEmail(email)

        time.sleep(0.2)

        driver.find_element(By.XPATH, '//*[text()="Cc"]').click()

        time.sleep(0.2)

        emailElem = driver.find_element(By.XPATH, '//*[text()="Enter or choose a recipient"]')
        emailElem.click()

        typeEmail("newton@withemerge.com")

        time.sleep(0.2)
        
    except Exception as e:
        print(e)
        print("No email")
        pass

    time.sleep(0.5)

    insert = driver.find_element(By.XPATH, "(//I18N-STRING[@data-locale-at-render='en-us'][text()='Insert'])[2]")
    insert.click()

    time.sleep(0.1)

    templates = driver.find_element(By.XPATH, "//*[text()='Templates']")
    templates.click()

    time.sleep(0.3)

    template = driver.find_element(By.XPATH, "//*[text()='VC Outreach Cold']")
    template.click()

    


# email.send_keys("emailmaria@hubspot.com")


input("Quit?")
driver.quit()
