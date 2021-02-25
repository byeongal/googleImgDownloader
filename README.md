# googleImgDownloader
구글에서 검색한 이미지 결과를 다운로드 받는 클롤러

### 사용법
1. 자신의 크롬 버전 및 운영체제에 맞는 크롬 드라이버(Chrome Driver)를 다운로드 받는다.
 * https://chromedriver.chromium.org/downloads

2. python을 설치후, 필요한 모듈을 설치한다.
```shell
$ pip install -r requirements.txt
```

3. `downloadImage.py` 에서 `DRIVER_PATH` 값을 크롬 드라이버가 있는 경로로 수정 한다.
   
4. `downloadImage.py`를 실행한다.
```shell
$ python downloadImage.py
Search Keyword : Iron Man
...
```

### 주의
* 셀레니움을 이용해서 공부용으로 작성한 코드이기 때문에, 주석을 한글로 남겼고, 시도한 코드를 지우지 않고 주석 처리를 하였습니다.
* 결과에 대해서 책임을 지지 않습니다.
