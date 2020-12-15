
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    
    cena = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    print(cena)
    if cena == True:
        browser.find_element_by_id("book").click()
    pass
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    x_element = browser.find_element_by_tag_name("span#input_value.nowrap")
    x = x_element.text
    y = calc(x)
    browser.find_element_by_xpath("//input[@class='form-control']").send_keys(y)
    # Отправляем заполненную форму
    browser.find_element_by_id("solve").click()
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(10)

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


