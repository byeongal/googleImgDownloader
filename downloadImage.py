import os
import time
from urllib.request import urlretrieve


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tqdm import tqdm

PAUSE_TIME = 1
IMPLICITY_WAIT_TIME = 3
DRIVER_PATH = './chromedriver.exe'

def main():
    chrome_options = webdriver.ChromeOptions()
    # # 시크릿 모드
    # chrome_options.add_argument("--incognito")
    # # 창 안나오게
    # chrome_options.add_argument('headless')

    # 셀레니움 드라이버
    driver = webdriver.Chrome(DRIVER_PATH, options=chrome_options)
    driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&authuser=0&ogbl")
    # driver.implicitly_wait(IMPLICITY_WAIT_TIME)
    time.sleep(PAUSE_TIME)

    # 검색할 키워드를 사용자에게 입력받고 폴더 생성
    search_keyword = input('Search Keyword : ')
    if not os.path.exists(f'./{search_keyword}'):
        os.makedirs(search_keyword)

    # 검색 시작
    search_bar = driver.find_element_by_xpath(
        '/html/body/div[2]/div[2]/div[2]/form/div[2]/div[1]/div[1]/div/div[2]/input')
    search_bar.send_keys(search_keyword)
    search_bar.send_keys(Keys.RETURN)

    # 현재 화면 크기(세로)를 가져움
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # 화면의 끝까지 내려봄 -> 그러면 이미지 더 있으면 크기가 바뀜
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # driver.implicitly_wait(IMPLICITY_WAIT_TIME)
        time.sleep(PAUSE_TIME)

        # 새로운 크기를 계산함
        new_height = driver.execute_script("return document.body.scrollHeight")

        # 새로운 크기랑 기존 크기가 같으면 이미지가 더 없던가 "결과 더보기" 눌러야함
        if new_height == last_height:
            # 결과 더 보기 찾아보고 있으면 눌러봄
            try:
                add_more_info = driver.find_element_by_xpath(
                    '/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[5]/input')
                add_more_info.click()
                # driver.implicitly_wait(IMPLICITY_WAIT_TIME)
                time.sleep(PAUSE_TIME)
            # 없으면 그냥 스크롤 내리기 끝
            except Exception as e:
                break
        last_height = new_height

    # 검색 결과에서 img 태그를 찾음
    search_results = driver.find_element_by_xpath('/html/body/div[2]/c-wiz/div[3]/div[1]')
    imgs = search_results.find_elements_by_css_selector('img')

    # 이미지를 저장함
    img_idx = 1
    for img in tqdm(imgs):
        try:
            img_url = img.get_attribute('src')
            if img_url is None:
                continue
            urlretrieve(img_url, f'./{search_keyword}/{img_idx}.jpeg')
            img_idx += 1
            # if img_url.startswith('data:image/jpeg'):
            #     urlretrieve(img_url, f'./{search_keyword}/{idx}.jpeg')
            # else:
            #     print(idx, img_url)
        except Exception as e:
            # print(e)
            # print(img_url)
            pass
    driver.close()


if __name__ == '__main__':
    main()
