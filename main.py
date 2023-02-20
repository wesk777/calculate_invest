import requests # Модуль для обработки URL
from bs4 import BeautifulSoup # Модуль для работы с HTML
import time # Модуль для остановки программы
import smtplib # Модуль для работы с почтой

# Ссылка на нужную страницу
def check_currency():
    DOLLAR_RUB = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&sxsrf=AJOqlzXIuVvLvnUpUkXFpgYoOmSKf3ZBVA:1676886185969&ei=qUDzY63rOonQqwGD3pnABA&ved=0ahUKEwjt48Xr56P9AhUJ6CoKHQNvBkgQ4dUDCA8&uact=5&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIKCAAQgAQQRhCCAjIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDoHCCMQsAMQJzoKCAAQRxDWBBCwAzoHCAAQsAMQQzoECCMQJzoECAAQQzoKCAAQgAQQFBCHAjoNCAAQgAQQFBCHAhDJAzoICAAQgAQQyQM6CQgjECcQRhCCAkoECEEYAFD-A1ixGWDsGmgBcAF4AYABvQGIAbQSkgEEMC4xN5gBAKABAcgBCsABAQ&sclient=gws-wiz-serp'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}

    full_page=requests.get(DOLLAR_RUB,headers=headers)
    soup=BeautifulSoup(full_page.content, 'html.parser')

    convert=soup.findAll("span", {"class": "DFlfde","class": "SwHCTb", "data-precision":"2"})
    print("Course dollar now = " + convert[0].text)
    time.sleep(3)
    check_currency()

check_currency()





#
#
# def first_count_capital():
#     value_biswap = input ("Сколько у Вас денег в biswap: ")
#     value_metamask = input("Сколько у Вас денег в Metamask: ")
#     value_cash = input("Сколько у Вас денег наличных: ")
#     value_card = input("Сколько у Вас денег на карте: ")
#     common_value = (int(value_biswap)+int(value_metamask)+int(value_cash)+int(value_card))
#     print(common_value)
#
#
# first_count_capital()
