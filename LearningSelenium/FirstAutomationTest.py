from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


from webdriver_manager.chrome import ChromeDriverManager
options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

driver.get("https://youtube.com/")
print(driver.title)
