from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# Setup Selenium with Chrome WebDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run headless Chrome


# Initialize the WebDriver
driver = webdriver.Chrome(service=Service(), options=chrome_options)

try:
    # Step 1: Go to the YouTube video URL
    driver.get("https://www.youtube.com/watch?v=n8yFCmjXZeE")

    # Step 2: Wait for the "expand" button to be clickable and then click it
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "expand"))).click()

    # Allow for any content to load after expanding
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "yt-attributed-string.style-scope.ytd-text-inline-expander"))
    )

    # Step 3: Parse everything in the element <yt-attributed-string class="style-scope ytd-text-inline-expander">
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')

    yt_attributed_string = soup.find_all("yt-attributed-string", class_="style-scope ytd-text-inline-expander")
    with open("output.txt", "w") as f:
        for element in yt_attributed_string:
            f.write(element.get_text() + "\n")

    # Step 4: Parse everything in the element <yt-formatted-string id="info" class="style-scope ytd-watch-info-text">
    yt_formatted_string_info = soup.find_all("yt-formatted-string", id="info", class_="style-scope ytd-watch-info-text")

    with open ("output.txt", "a") as f:
        f.write("\n---------------------------\n")
        for element in yt_formatted_string_info:
            f.write(element.get_text() + "\n")

finally:
    # Close the WebDriver
    driver.quit()