# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import requests
import json
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pyperclip

LOGIN_ID = 'myson0545'
LOGIN_PASSWORD = 'alstn0677'
CHROME_DRIVER = '/app/.chromedriver/bin/chromedriver'

title_dict = {}
title_link_dict = {}
time_dict = {}


def clipboard_input(user_xpath, user_input):
        temp_user_input = pyperclip.paste()  # 사용자 클립보드를 따로 저장

        pyperclip.copy(user_input)
        driver.find_element_by_xpath(user_xpath).click()
        ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

        pyperclip.copy(temp_user_input)  # 사용자 클립보드에 저장 된 내용을 다시 가져 옴
        time.sleep(1)


# 새로운 채용 공고가 업데이트 되면 슬랙 알림 전송
def send_message_to_slack():
    webhook_url = 'https://hooks.slack.com/services/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'
    print_str = ':bell: 채용공고 알림 :bell:\n'
    no_update = True

    if len(title_dict['finance']) != 0:
        no_update = False
        print_str += "++++++++++++++++++++++++++\n"
        print_str += ':bulb: 금융권 채용공고 :bulb:\n'
        print_str += "==========================\n"
        for idx in range(0, len(title_dict['finance'])):
            print_str += ":white_check_mark:제목:white_check_mark: : "
            print_str += title_dict['finance'][idx]
            print_str += '\n'
            print_str += "- 공고 링크 : "
            print_str += title_link_dict['finance'][idx]
            print_str += '\n'
            print_str += "- 업로드 시간 : "
            print_str += time_dict['finance'][idx]
            print_str += '\n'
            print_str += "==========================\n"
        print_str += "++++++++++++++++++++++++++\n\n"

    if len(title_dict['engineer']) != 0:
        no_update = False
        print_str += "++++++++++++++++++++++++++\n"
        print_str += ':bulb: 이공계 채용공고 :bulb:\n'
        print_str += "==========================\n"
        for idx in range(0, len(title_dict['engineer'])):
            print_str += ":white_check_mark:제목:white_check_mark: : "
            print_str += title_dict['engineer'][idx]
            print_str += '\n'
            print_str += "- 공고 링크 : "
            print_str += title_link_dict['engineer'][idx]
            print_str += '\n'
            print_str += "- 업로드 시간 : "
            print_str += time_dict['engineer'][idx]
            print_str += '\n'
            print_str += "==========================\n"
        print_str += "++++++++++++++++++++++++++\n\n"

    if len(title_dict['intern']) != 0:
        no_update = False
        print_str += "++++++++++++++++++++++++++\n"
        print_str += ':bulb: 인턴 채용공고 :bulb:\n'
        print_str += "==========================\n"
        for idx in range(0, len(title_dict['intern'])):
            print_str += ":white_check_mark:제목:white_check_mark: : "
            print_str += title_dict['intern'][idx]
            print_str += '\n'
            print_str += "- 공고 링크 : "
            print_str += title_link_dict['intern'][idx]
            print_str += '\n'
            print_str += "- 업로드 시간 : "
            print_str += time_dict['intern'][idx]
            print_str += '\n'
            print_str += "==========================\n"
        print_str += "++++++++++++++++++++++++++\n\n"

    if len(title_dict['IT']) != 0:
        no_update = False
        print_str += "++++++++++++++++++++++++++\n"
        print_str += ':bulb: IT 채용공고 :bulb:\n'
        print_str += "==========================\n"
        for idx in range(0, len(title_dict['IT'])):
            print_str += ":white_check_mark:제목:white_check_mark: : "
            print_str += title_dict['IT'][idx]
            print_str += '\n'
            print_str += "- 공고 링크 : "
            print_str += title_link_dict['IT'][idx]
            print_str += '\n'
            print_str += "- 업로드 시간 : "
            print_str += time_dict['IT'][idx]
            print_str += '\n'
            print_str += "==========================\n"
        print_str += "++++++++++++++++++++++++++\n\n"

    if no_update:
        print_str += '금일 채용공고 소식 없음!\n'

    data = {'channel': '#job_info_notice', 'as_user': 'false', 'username': '채용공고 알리미', 'text': print_str,
            'icon_emoji': ':bell:'}
    res = requests.post(webhook_url, data=json.dumps(data))
    print(res)


try:
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(executable_path=CHROME_DRIVER, options=chrome_options)
    # driver = webdriver.Chrome(executable_path=r'C:/chromedriver.exe', options=chrome_options)

    # 독취사 접속
    driver.get("https://cafe.naver.com/dokchi/485362")
    time.sleep(1)

    # 창
    driver.switch_to.window(driver.window_handles[-1])

    # 네이버 로그인
    elem_id = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/form/fieldset/div[1]/div[1]/span/input')
    elem_id.send_keys(LOGIN_ID)
    time.sleep(1)
    elem_password = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/form/fieldset/div[2]/div[1]/span/input')
    elem_password.send_keys(LOGIN_PASSWORD)
    time.sleep(1)
    # clipboard_input('/html/body/div[1]/div[3]/div/form/fieldset/div[1]/div[1]/span/input', LOGIN_ID)
    # clipboard_input('/html/body/div[1]/div[3]/div/form/fieldset/div[2]/div[1]/span/input', LOGIN_PASSWORD)
    elem = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/form/fieldset/input')
    elem.click()

    # 창
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(1)

    # 금융권 공고
    # elem = driver.find_element_by_xpath('/html/body/div[2]/div/div[6]/div[1]/div[3]/div[2]/ul[8]/li[10]/a')
    elem = driver.find_element_by_id('menuLink5271')
    elem.click()
    time.sleep(2)

    # iframe 변경
    driver.switch_to.frame("cafe_main")
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # 공고 리스트 추출
    table = soup.find_all('div', {'class': 'article-board m-tcol-c'})[1].find_all('tr')

    title_list = []
    title_link_list = []
    time_list = []
    index = 0
    for i in table:
        index = index + 1
        if index % 2 == 0:
            continue

        title = i.find('td', {'class': 'td_article'})
        upload_date = i.find('td', {'class': 'td_date'})

        if ":" in upload_date.text:
            title_str = title.find('a', {'class': 'article'}).text.strip()
            title_link = 'https://cafe.naver.com' + title.find('a', {'class': 'article'})['href']

            title_list.append(title_str)
            title_link_list.append(title_link)
            time_list.append(upload_date.text)

            print('채용공고:', title_str)
            print('공고 Link:', title_link)
            print('업데이트 시간:', upload_date.text)
        else:
            print('금융권 : 오늘 업데이트 공고 끝.')
            break
    title_dict['finance'] = title_list
    title_link_dict['finance'] = title_link_list
    time_dict['finance'] = time_list

    # 이공계 공고
    driver.switch_to.default_content()
    # elem = driver.find_element_by_xpath('/html/body/div[2]/div/div[6]/div[1]/div[3]/div[2]/ul[8]/li[9]/a')
    elem = driver.find_element_by_id('menuLink5269')
    elem.click()
    time.sleep(2)

    # iframe 변경
    driver.switch_to.frame("cafe_main")
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # 공고 리스트 추출
    table = soup.find_all('div', {'class': 'article-board m-tcol-c'})[1].find_all('tr')

    title_list = []
    title_link_list = []
    time_list = []
    index = 0
    for i in table:
        index = index + 1
        if index % 2 == 0:
            continue

        title = i.find('td', {'class': 'td_article'})
        upload_date = i.find('td', {'class': 'td_date'})

        if ":" in upload_date.text:
            title_str = title.find('a', {'class': 'article'}).text.strip()
            title_link = 'https://cafe.naver.com' + title.find('a', {'class': 'article'})['href']

            title_list.append(title_str)
            title_link_list.append(title_link)
            time_list.append(upload_date.text)

            print('채용공고:', title_str)
            print('공고 Link:', title_link)
            print('업데이트 시간:', upload_date.text)
        else:
            print('이공계 : 오늘 업데이트 공고 끝.')
            break
    title_dict['engineer'] = title_list
    title_link_dict['engineer'] = title_link_list
    time_dict['engineer'] = time_list

    # 인턴 공고
    driver.switch_to.default_content()
    # elem = driver.find_element_by_xpath('/html/body/div[2]/div/div[6]/div[1]/div[3]/div[2]/ul[8]/li[4]/a')
    elem = driver.find_element_by_id('menuLink133')
    elem.click()
    time.sleep(2)

    # iframe 변경
    driver.switch_to.frame("cafe_main")
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # 공고 리스트 추출
    table = soup.find_all('div', {'class': 'article-board m-tcol-c'})[1].find_all('tr')

    title_list = []
    title_link_list = []
    time_list = []
    index = 0
    for i in table:
        index = index + 1
        if index % 2 == 0:
            continue

        title = i.find('td', {'class': 'td_article'})
        upload_date = i.find('td', {'class': 'td_date'})

        if ":" in upload_date.text:
            title_str = title.find('a', {'class': 'article'}).text.strip()
            title_link = 'https://cafe.naver.com' + title.find('a', {'class': 'article'})['href']

            title_list.append(title_str)
            title_link_list.append(title_link)
            time_list.append(upload_date.text)

            print('채용공고:', title_str)
            print('공고 Link:', title_link)
            print('업데이트 시간:', upload_date.text)
        else:
            print('인턴 : 오늘 업데이트 공고 끝.')
            break
    title_dict['intern'] = title_list
    title_link_dict['intern'] = title_link_list
    time_dict['intern'] = time_list

    # 연구개발/IT 공고
    driver.switch_to.default_content()
    # elem = driver.find_element_by_xpath('/html/body/div[2]/div/div[6]/div[1]/div[3]/div[2]/ul[25]/li[5]/a')
    elem = driver.find_element_by_id('menuLink3479')
    elem.click()
    time.sleep(2)

    # iframe 변경
    driver.switch_to.frame("cafe_main")
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # 공고 리스트 추출
    table = soup.find_all('div', {'class': 'article-board m-tcol-c'})[1].find_all('tr')

    title_list = []
    title_link_list = []
    time_list = []
    index = 0
    for i in table:
        index = index + 1
        if index % 2 == 0:
            continue

        title = i.find('td', {'class': 'td_article'})
        upload_date = i.find('td', {'class': 'td_date'})

        if ":" in upload_date.text:
            title_str = title.find('a', {'class': 'article'}).text.strip()
            title_link = 'https://cafe.naver.com' + title.find('a', {'class': 'article'})['href']

            title_list.append(title_str)
            title_link_list.append(title_link)
            time_list.append(upload_date.text)

            print('채용공고:', title_str)
            print('공고 Link:', title_link)
            print('업데이트 시간:', upload_date.text)
        else:
            print('IT : 오늘 업데이트 공고 끝.')
            break
    title_dict['IT'] = title_list
    title_link_dict['IT'] = title_link_list
    time_dict['IT'] = time_list

    driver.close()
    # 슬랙 알림 보내기
    send_message_to_slack()

except Exception as e:
    print(str(e))
