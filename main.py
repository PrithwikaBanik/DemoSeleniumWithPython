from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def google_search(query):
    # Set up the WebDriver (e.g., Chrome)
    driver = webdriver.Chrome()

    try:
        # Open Google
        driver.get("https://www.google.com")

        # Wait for the search box to be present
        wait = WebDriverWait(driver, 10)
        search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))

        # Type the search query
        search_box.send_keys(query)

        # Press Enter
        search_box.send_keys(Keys.RETURN)

        # Wait for the results to load
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h3")))

        # Retrieve and print the titles of the first few search results
        results = driver.find_elements(By.CSS_SELECTOR, "h3")

        print("\nTop search results:")
        for index, result in enumerate(results[:5], start=1):
            print(f"{index}. {result.text}")

    finally:
        # Close the browser
        driver.quit()


if __name__ == "__main__":
    search_term = input("Enter the search term: ")
    google_search(search_term)
