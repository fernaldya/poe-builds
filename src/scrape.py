from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as bs
from datetime import datetime
from time import sleep

def get_time():
    return datetime.now().strftime('%H-%M-%S_%Y-%m-%d')

def scrape(url, driver):
    """
    Function to scrape data with the parameters:
    1. url -> URL of the website to scrape
    2. driver -> Webdriver instance
    
    A retry mechanism is implemented because sometimes there might be occurences where
    the table is empty.
    
    If the scrape is sucessful (table not empty) the function outputs all the table rows <tr>
    """
    current_time = get_time()
    print('Web scraped at: ', current_time)
    
    max_attempts = 5
    attempts = 1
    table = None

    while attempts < max_attempts and table is None: # Retry mechanism
        print('Attempt #', attempts)
        driver.get(url)
        WebDriverWait(driver, 10).until( # Waits up to a maximum of 10s until the table appears
            EC.presence_of_element_located((By.CSS_SELECTOR, "table._builds-table_8h86n_1"))
        )
        html = driver.page_source
        soup = bs(html, 'html.parser')
        table = soup.body.find('table', class_= "_builds-table_8h86n_1") # Finds the table containing all the elements we want
        attempts += 1
        
        if table:
            print('Success')
            driver.quit()
            tbody = table.find('tbody') # Fetches the table body
            table_rows = tbody.find_all('tr') # Fetches all the table rows
            return table_rows, current_time
        sleep(3)
        
    if not table:
        print('Failed to fetch table after 5 attempts.')
        driver.quit()
        
