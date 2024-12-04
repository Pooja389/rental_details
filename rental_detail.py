import time
from selenium import webdriver
from  selenium.webdriver.common.by import By

link = "https://docs.google.com/forms/d/e/1FAIpQLSeo76zUKJ5DL1g6kZnszDJxI6BYnT2bsKa1MxlHRDFQy9tEFQ/viewform?usp=sf_link"
driver = webdriver.Chrome()
driver.get("https://appbrewery.github.io/Zillow-Clone/")

all_price = driver.find_elements(By.CLASS_NAME,'PropertyCardWrapper__StyledPriceLine')
all_addresses = driver.find_elements(By.XPATH,'//*[@id="zpid_2056905294"]/div/div[1]/a/address')
all_url = driver.find_elements(By.XPATH,"//*[@id='zpid_2056905294']/div/div[1]/a")

addresses_20 = []
price_20 = []
url_20 = []


for i in range(20):
    price_20.append(((all_price[i].text).split("+"))[0])
    addresses_20.append(all_addresses[i].text)
    url_20.append(all_url[i].get_attribute("href"))


driver.get(url=link)
time.sleep(4)


for i in range(20):
    ques1 = driver.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
    ques2 = driver.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
    ques3 = driver.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
    ques1.click()
    ques1.send_keys(addresses_20[i])
    time.sleep(1.6)

    ques2.click()
    ques2.send_keys(price_20[i])
    time.sleep(1.6)
    
    ques3.click()
    ques3.send_keys(url_20[i])
    time.sleep(1.6)
    
    submit = driver.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div/span/span")
    submit.click()
    time.sleep(2)
    
    another_response = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div/div[4]/a")
    another_response.click()


driver.quit()
 
