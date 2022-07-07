#!/usr/bin/python3

from itertools import zip_longest
from os import getenv
from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
import json 
from selenium.webdriver.chrome.options import Options

password_env = getenv("LINKEDIN_PWS")
if password_env is None:
    raise ValueError("Password not found in enviroment")

username_env = getenv("LINKEDIN_USER")
if username_env is None:
    raise ValueError("User not found in enviroment")

linkedin_urls = "https://www.linkedin.com/in/laura-perez-castillo/"

chrome_options = Options()
#chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

wait = WebDriverWait(driver, 15)

driver.get('https://www.linkedin.com')

### DRIVER NAVIGATE INTO LINKEDIN
sign_in_button = driver.find_element(By.XPATH, "/html/body/nav/div/a[2]")
sign_in_button.click()
wait = WebDriverWait(driver, 15)

### DRIVER LOGIN INTO LINKEDIN
username = driver.find_element(By.NAME, 'session_key')
username.send_keys("1960@holbertonschool.com")
password = driver.find_element(By.NAME, 'session_password')
password.send_keys("Hi World1!")
log_in_button = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
wait = WebDriverWait(driver, 30)
log_in_button.click()

wait = WebDriverWait(driver, 30)
driver.get(linkedin_urls)
### NAME
name_xpath = "//h1[@class='text-heading-xlarge inline t-24 v-align-middle break-words']"
condition_name = EC.presence_of_element_located((By.XPATH, name_xpath))
name = wait.until(condition_name).text

### IMAGE 
"""image_xpath = '//*[@id="ember34"]'
condition_image = EC.presence_of_element_located((By.XPATH, image_xpath))
image = wait.until(condition_image)
image = image.get_attribute("src")"""

### COUNTRY
country_xpath = '//*[@id="ember31"]/div[2]/div[2]/div[2]/span[1]'
#country_xpath = '/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[2]/div[2]/span[1]'
condition_xp_country =  EC.presence_of_element_located((By.XPATH, country_xpath))
country = wait.until(condition_xp_country).text

### PROFESION
profetion_xpath = '//*[@id="ember31"]/div[2]/div[2]/div[1]/div[2]'
#profetion_xpath = '/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[2]/div[1]/div[2]'
condition_xp_profetion =  EC.presence_of_element_located((By.XPATH, profetion_xpath))
profetion = wait.until(condition_xp_profetion).text

### SCROLL
driver.execute_script("window.scrollBy(0, 1200)","")

### EXPERIENCE
####TITLE
xp_xpath_title = '/html/body/div[6]/div[3]/div/div/div[2]/div/div/main/section[5]/div[3]/ul/li/div/div[2]/div/div[1]/div/span/span[1]'
#xp_xpath_title = "/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[4]/div[3]/ul/li/div/div[2]/div/div/div/span/span[1]"
condition_xp_title =  EC.presence_of_element_located((By.XPATH, xp_xpath_title))
titles = wait.until(condition_xp_title)
titles = titles.find_elements(By.XPATH, xp_xpath_title)
xp_title = [x.get_attribute("textContent") for x in titles]
breakpoint()
#### COMPANY
xp_xpath_company  = '//*[@id="ember79"]/div[3]/ul/li/div/div[2]/div/div[1]/span[1]/span[1]'
#xp_xpath_company = '/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[4]/div[3]/ul/li/div/div[2]/div/div/span[1]/span[1]'
condition_xp_company = EC.presence_of_element_located((By.XPATH, xp_xpath_company))
companies = wait.until(condition_xp_company)
companies = companies.find_elements(By.XPATH, xp_xpath_company)
xp_company = [x.get_attribute("textContent") for x in companies]

####  TIME IN COMPANY
xp_xpath_time = '//*[@id="ember79"]/div[3]/ul/li/div/div[2]/div[1]/div[1]/span[2]/span[1]'
#xp_xpath_time = '/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[4]/div[3]/ul/li/div/div[2]/div/div/span[2]/span[1]'
condition_xp_time = EC.presence_of_element_located((By.XPATH, xp_xpath_time))
time = wait.until(condition_xp_time)
time = time.find_elements(By.XPATH, xp_xpath_time)
xp_time = [x.get_attribute("textContent") for x in time]


### EDUCATION
#### COLLAGUE
education_xpath_collague = '//*[@id="ember80"]/div[3]/ul/li/div/div[2]/div/a/div/span/span[1]'
#education_xpath_collague = "/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[5]/div[3]/ul/li/div/div[2]/div/a/div/span/span[1]"
condition_education_collague =  EC.presence_of_element_located((By.XPATH, education_xpath_collague))
education_collague = wait.until(condition_education_collague)
education_collague = education_collague.find_elements(By.XPATH, education_xpath_collague)
education_collague = [x.get_attribute("textContent") for x in education_collague]

#### TITLE
education_xpath_title = '//*[@id="ember80"]/div[3]/ul/li/div/div[2]/div/a/span[1]/span[1]'
#education_xpath_title = "/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[5]/div[3]/ul/li/div/div[2]/div/a/span[1]/span[1]"
condition_education_title =  EC.presence_of_element_located((By.XPATH, education_xpath_title))
education_title = wait.until(condition_education_title)
education_title = education_title.find_elements(By.XPATH, education_xpath_title)
education_title = [x.get_attribute("textContent") for x in education_title]

#### TIME
education_xpath_time = '//*[@id="ember80"]/div[3]/ul/li/div/div[2]/div/a/span[2]'
#education_xpath_time = "/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[5]/div[3]/ul/li/div/div[2]/div/a/span[2]/span[1]"
condition_education_time =  EC.presence_of_element_located((By.XPATH, education_xpath_time))
education_time = wait.until(condition_education_time)
education_time = education_time.find_elements(By.XPATH, education_xpath_time)
education_time = [x.get_attribute("textContent") for x in education_time]

###LANGUAJES
languajes_xpath = '//*[@id="ember144"]/div[3]/ul/li[1]/div/div[2]/div[1]/div[1]/div/span/span[1]'
#languajes_xpath = "/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[8]/div[3]/ul/li/div/div[2]/div/div[1]/div/span/span[1]"
condition_languajes =  EC.presence_of_element_located((By.XPATH, languajes_xpath))
languajes = wait.until(condition_languajes)
languajes = languajes.find_elements(By.XPATH, languajes_xpath)
languajes = [x.get_attribute("textContent") for x in languajes]
str_languajes = " ".join(x for x in languajes)
print(str_languajes)

### LINK
link_profile = driver.current_url

### EXPERIENCE DICTIONARY
experience_list = []
for x in range(0, len(xp_title)):  
    experience_dict = {
        "Title": xp_title[x],
        "Company": xp_company[x],
        "Time": xp_time[x]
    }
    experience_list.append(experience_dict)
### EDUCATION DICTIONARY
education_list = []
for x in range(0, len(education_collague)):
    education_dict = {
        "Collague": education_collague[x],
        "Title": education_title[x],
        "Period": education_time[x]
    }
    education_list.append(education_dict)
    
### USER DICTIONARY 
user_dict = {
    "Name": name,
    "Profession": profetion,
    "Education": education_list,
    "Experience": experience_list,
    "Languajes": str_languajes,
    "Residence": country,    
    "Link": link_profile,    

}

with open("sample.json", "w") as outfile:
    json.dump(user_dict, outfile)
    
driver.close()
