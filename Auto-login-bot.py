import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def startbot(username, password, url):
    path = "C:\\Users\\Madhu\\Downloads\\chromedriver.exe"

    service = Service(path)

    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(service=service, options=chrome_options)

    print ("Opening the login page")
    driver.get(url)
    
    print ("Filling in the username...")
    driver.find_element(By.ID, "login_field").send_keys(username)

    print ("Filling in the Password...")
    driver.find_element(By.ID, "password").send_keys(password)
    
    print ("Clicking the login button...")
    driver.find_element(By.NAME, "commit").click()

    print ("Login process initiated...")
    time.sleep(60)

    driver.quit()
    
username = "Venkii._.1622"
password = "123naruto"
url = "https://www.instagram.com/accounts/login/"

startbot(username, password, url)