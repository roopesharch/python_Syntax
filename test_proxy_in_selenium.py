from selenium import webdriver

driver_path="Driver_path"
PROXY="Type_proxy"

chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument("--disable-notifications")
chrome_option.add_argument('--headless')
chrome_option.add_argument('--proxy-server=%s' % PROXY)
chrome_option.add_argument("--incognito")
chrome_option.add_argument("--start-maximized")

connection_attempt=0
while True:
    connection=0
    connection_attempt=connection_attempt+1
    try:
        driver = webdriver.Chrome(executable_path= driver_path,chrome_options=chrome_option)
        driver.maximize_window()
        br=1
        connection=1
        print("\n Connection successfull")
    except Exception as e:
        print(e)
        driver_path=input("\n Enter the Compatible chrome driver path")

    if connection==1 or connection_attempt > 5:
        break

driver.get("https://www.linkedin.com/login")
