'''
from selenium import webdriver as wd

driver = wd.Chrome("./chromedriver.exe")
url = "https://www.naver.com"
driver.get(url)
'''
import time
import os
from selenium import webdriver
from bs4 import BeautifulSoup as soups
 
def search_selenium(search_name, search_path, search_limit) :
    search_url = "https://search.naver.com/search.naver?where=image&query={}".format(search_name)
    chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument("headless")
    #chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("lang=ko_KR")
    browser = webdriver.Chrome('E:/AI/crawl/chromedriver.exe',chrome_options=chrome_options)
    browser.get(search_url)
    body = browser.find_element_by_css_selector('body')
    print(body)

    imgs = browser.find_elements_by_css_selector('img._image')
    links = []
    for img in imgs:
        link = img.get_attribute('src')
        if 'http' in link:
            links.append(link)
 
    browser.close()
 
if __name__ == "__main__" :
    
    #search_name = ['너에게 닿기를 아라이 카즈이치','너에게 닿기를 쿠로누마 사와코','너에게 닿기를 쿠루미자와 우메','원피스 나미','원피스 니코 로빈','원피스 비비','원피스 보아 핸콕','나루토 사쿠라','나루토 히나타','나루토 츠나데','나루토 ',' 나루토 텐텐','도라에몽 이슬이','포켓몬스터 꼬북이','포켓몬스터 이슬이','포켓몬스터 간호순','포켓몬스터 여경','코난 미란이','코난 카즈하','코난 하이바라 아이','인사이드 아웃 슬픔이','겨울왕국 안나','겨울왕국 엘사','뽀로로 루피','코코몽 코코몽','뽀로로 뽀로로']
    search_name = '너에게 닿기를 아라이 카즈이치'
    search_limit = 150
    directory = "E:/AI/crawl/download/여캐/네이버/"+search_name
    search_path = "E:/AI/crawl/download/여캐/네이버/"+search_name+"/"+search_name
    if not os.path.exists(directory):
        os.makedirs(directory)
    search_selenium(search_name, search_limit, search_path)
    #search_selenium(i, search_path, search_limit)