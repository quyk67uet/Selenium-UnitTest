from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  

PATH = r"C:\Program Files (x86)\chromedriver.exe" 

service = Service(PATH)

driver = webdriver.Chrome(service=service)

driver.get("https://www.python.org/")
print(driver.title)

search = driver.find_element(By.ID, "id-search-field")
search.send_keys("fastapi")
search.send_keys(Keys.RETURN)

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "content"))
    )
    titles = main.find_elements(By.TAG_NAME, "h3")

    for title in titles:
        print(title.text)

finally:
    driver.quit()
