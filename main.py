from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from src.scrape import scrape
from src.fetch_builds import fetch_builds
from src.tabularise_clean import tabularise_clean

def main():
    """
    Creates an instance of the webdriver and does the following:
    1. Scrape the given URL
    2. 
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=chrome_options)
    
    url = 'https://poe.ninja/builds/affliction?sort=dps'
    table_rows, scrape_time = scrape(url, driver)
    builds = fetch_builds(table_rows)
    tabularise_clean(builds, scrape_time)
    
if __name__ == '__main__':
    main()
