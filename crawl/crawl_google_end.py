from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import os
import time
import urllib.request
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("lang=ko_KR")



# Search images from Google Images

search_names = ['겨울왕국 엘사','겨울왕국 엘사 얼굴','나루토 사쿠라 얼굴','나루토 사쿠라','너에게 닿기를 쿠로누마 사와코 얼굴','너에게 닿기를 쿠로누마 사와코','원피스 나미 얼굴','명탐정 코난 미란이 얼굴','명탐정 코난 미란이','카드캡터체리','이누야샤 가영']
#search_names = ['나루토','나루토 얼굴','너에게 닿기를 카제하야 쇼타','카제하야 쇼타','원피스 루피','원피스 루피 얼굴','명탐정코난 코난','명탐정코난 코난 얼굴','드래곤볼 손오공','드래곤볼 손오공 얼굴','이누야샤 얼굴','이누야샤 이누야샤']

for search_name in search_names:
    driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_options)
    driver.get("https://www.google.com/imghp?hl=en")
    elem = driver.find_element_by_name("q")
    elem.send_keys(search_name)
    elem.send_keys(Keys.RETURN)

    SCROLL_PAUSE_TIME = 1

# Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    for i in range(10):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(SCROLL_PAUSE_TIME)

        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            try:
                driver.find_element_by_css_selector(".mye4qd").click()
            except:
                break
        last_height = new_height

# Get each image URL and download it
    count = 1
    images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")

    for image in images:
        try:
            image.click()
            time.sleep(1.5)
            img_url = driver.find_element_by_xpath("/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div/div[2]/a/img").get_attribute("src")
            opener = urllib.request.build_opener()
            opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
            urllib.request.install_opener(opener)
            directory = "E:/AI/crawl/download/여캐/구글/"+search_name
            search_path = "E:/AI/crawl/download/여캐/구글/"+search_name+"/"+search_name
            if not os.path.exists(directory):
                os.makedirs(directory)
            urllib.request.urlretrieve(img_url, search_path+str(count) + ".jpg")
            count = count + 1
            if count == 250:
                break
        except:
            pass
    driver.close()
# Close driver
