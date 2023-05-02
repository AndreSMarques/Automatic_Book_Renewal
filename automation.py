import  time
from selenium import webdriver
from selenium.webdriver.common.by import By


def download_image_captcha():
    with open('filename.png', 'wb') as file:
        file.write(driver.find_element(By.XPATH, '/html/body/form/div/div[1]/center/table/tbody/tr[3]/td/img').screenshot_as_png)


def login():
    rgm = driver.find_element(By.XPATH, '//*[@id="id_login"]').send_keys("RGM")
    password = driver.find_element(By.XPATH, '//*[@id="id_senhaLogin"]').send_keys("password")
    time.sleep(10)
    login = driver.find_element(By.XPATH, '//*[@id="button"]').click()



def renew_book():
    pass
    
    


page_link = 'https://biblioteca.udf.edu.br/pergamum_udf/biblioteca_s/php/login_usu.php?flag=index.php'

driver = webdriver.Chrome()
driver.get(page_link)
login()
download_image_captcha()
#renew_book()
time.sleep(50)


