import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import os

# Customize log format to show only the message without any log level
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s"  # Only the message will be printed
)

# URL of the Flask app's home endpoint
URL = "http://localhost:5000/home"

# Configure Chrome options (uncomment headless mode if needed)
options = Options()
# options.add_argument("--headless")  # Run without opening a GUI window

# Path to the chromedriver (assumes it's in the same folder as this script)
driver_path = os.path.join(os.path.dirname(__file__), 'chromedriver')
service = Service(driver_path)

try:
    # Start Chrome browser using the driver
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(URL)

    # Wait for the cat fact element to be present in the DOM
    wait = WebDriverWait(driver, 10)

    # Wait for the element with ID 'cat-fact' to be present and contain non-empty text
    wait.until(EC.presence_of_element_located((By.ID, "cat-fact")))
    wait.until(lambda d: d.find_element(By.ID, "cat-fact").text.strip() != "")

    # Extract the fact and print it
    cat_fact = driver.find_element(By.ID, "cat-fact").text
    logging.info(f" 🐾 Did You Know?: {cat_fact}")

except Exception as e:
    logging.error(f"Something went wrong: {e}", file=sys.stderr)

finally:
    # Make sure the browser closes even if there's an error
    driver.quit()
