from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--window-size=1920x1080')

driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get("https://www.google.com")

    driver.implicitly_wait(5)

    title = driver.title

    print(f"Connexion réussie. Titre de la page : {title}")

finally:
    driver.quit()
