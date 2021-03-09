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
    search_url = "https://www.google.com/search?q=" + str(search_name) + "&hl=ko&tbm=isch"
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("lang=ko_KR")
    browser = webdriver.Chrome('./chromedriver.exe',chrome_options=chrome_options)
    browser.get(search_url)
    
    image_count = len(browser.find_elements_by_tag_name("img"))
    
    print("로드된 이미지 개수 : ", image_count)
 
    browser.implicitly_wait(2)
 
    for i in range( search_limit ) :
        image = browser.find_elements_by_tag_name("img")[i]
        time.sleep(0.5)
        image.screenshot(search_path + str(i) + ".png")
 
    browser.close()
 
if __name__ == "__main__" :
    
    search_name = ['너에게 닿기를 아라이 카즈이치','너에게 닿기를 쿠로누마 사와코','너에게 닿기를 쿠루미자와 우메','원피스 나미','원피스 니코 로빈','원피스 비비','원피스 보아 핸콕','나루토 사쿠라','나루토 히나타','나루토 츠나데','나루토 ',' 나루토 텐텐','도라에몽 이슬이','포켓몬스터 꼬북이','포켓몬스터 이슬이','포켓몬스터 간호순','포켓몬스터 여경','코난 미란이','코난 카즈하','코난 하이바라 아이','인사이드 아웃 슬픔이','겨울왕국 안나','겨울왕국 엘사','뽀로로 루피','코코몽 코코몽','뽀로로 뽀로로']
    search_limit = 150
    for i in search_name:
        print(i)
        directory = "E:/AI/crawl/download/여캐/"+i
        search_path = "E:/AI/crawl/download/여캐/"+i+"/"+i
        if not os.path.exists(directory):
            os.makedirs(directory)
    # search_maybe(search_name, search_limit, search_path)
        search_selenium(i, search_path, search_limit)