from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import csv

# Initialize the WebDriver (ensure you have the correct path to your WebDriver)
driver_path = 'path/to/your/webdriver'
driver = webdriver.Chrome()

# URL of the website to scrape
url = "https://www.vcsheet.com/investors?stages=pre-seed%7Cseed&average-check-sizes=100k-500k%7C500k-1m%7C1m-3m&sectors=fintech%7Cgeneralist%7Cunder-represented-founders&geographies=usa%7Ccanada"
driver.get(url)

# Scroll to the bottom of the page to load all content
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)  # Wait for the content to load
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Parse the HTML content of the page using BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Close the WebDriver
driver.quit()

# Find the container holding the partner information
partners = soup.find_all('div', class_='list-card stand-alone more-space')

# List to store the scraped data
data = []

# Loop through each partner and extract the required information
for partner in partners:
    try:
        name = partner.find('h3').text.strip()
        
        title = partner.find('div', class_='list-title medium').text.strip().split("@")
        role = title[0]
        company = title[1]
        email = partner.find('a', class_='contact-icon email w-inline-block')
        if email:
            email = email.get('href').replace('mailto:', '').strip().replace('?subject=Contact', '')
        else:
            email = "N/A"
        linkedin = partner.find('a', class_='contact-icon linkedin w-inline-block')
        if linkedin:
            linkedin = linkedin.get('href').strip()
        else:
            linkedin = "N/A"

        data.append([name, role.strip(), company.strip(), email, linkedin])
    except: 
        print("Error, no name found")
    # role = partner.find('div', class_='partner-role').text.strip()
    # fund_name = partner.find('div', class_='fund-name').text.strip()
    # email = partner.find('a', class_='email').get('href').replace('mailto:', '').strip()
    # linkedin = partner.find('a', class_='linkedin').get('href').strip()
    
    # # Append the extracted information to the data list
    # data.append([name, role, fund_name, email, linkedin])

# Write the scraped data to a CSV file
with open('partners_info.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Role', 'Fund Name', 'Email', 'LinkedIn'])
    writer.writerows(data)

print("Scraping completed and data saved to partners_info.csv")
