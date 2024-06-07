import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def main():
    # Set up the WebDriver (e.g., ChromeDriver)
    driver = webdriver.Chrome()

    # Open a webpage
    driver.get("https://www.python.org")

    # Find an element (e.g., the search bar)
    search_bar = driver.find_element(By.NAME, "q")

    # Interact with the element (e.g., enter text and submit)
    search_bar.send_keys("web scraping")
    search_bar.send_keys(Keys.RETURN)

    # Wait for results to load and display the title
    print(driver.title)

    time.sleep(5)
    # Close the browser
    driver.quit()

if __name__ == '__main__':
    main()