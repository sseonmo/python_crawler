강의자 git - https://github.com/Kyeongrok/python_example/blob/master/README.md / https://github.com/Kyeongrok/python_crawler
## Python - Hello 출력
- 디렉토리(Directory) 만들기
- 파이썬 파일(.py) 만들

# 파이썬 크롤러 만들기
### Naver 금융 주식 데이터 수집하기
- 특정종목 금액 받아오기
- 종목 금액 받아오기
- 특정종목의 봉차 데이터(open, close, high,  low) 받아오기
- 특정종목의 봉차트 데이터(시고저종) 받아오기
- 여러종목의 봉차트 데이터 받아오기

### python module import 하기 - libs5
- 자주 사용하는 기능을 라이브러리 형태로 만드는 것
- 만들어 놓고 호출해서 쓴다.
> dirtory 가 아닌 package 로 폴더링을 해야한다.

### 엑셀로 데이터 저장하기 - com > week8

### Naver 검색결과 100개씩 10페이지 가지고 오기 - lecture > practice > 11_stage.py
- 모듈로 분리 한 후에 여러번 호출하기
- 결과값 json으로 저장하기

### python pandas로 데이터 분석하기 
- 블로그 참조 : https://doorbw.tistory.com/172
- 2000개의 검색결과중 가장 많이 등장하는 블로거 이름은?
- 어떤 블로거에게 광고를 의뢰하면 노출이 많이될까?

데이터 분석
1. 개수세기 - count
1. 필터링 - 월기준
1. 정렬하기 - 내림차순, 올림차순
    > dfSorted = df.sort_values(['price']) - 기본 오름차순  
    dfSorted = df.sort_values(['price'], ascending=0) - 내림차순
1. 특정 키워드 포함된 데이터 뽑아내기
    > result = df[df['name'].str.contains('페레로로쉐')]

### 공공데이터 api 호출하기 - 부동산 실거래가
- https://www.data.go.kr/dataset/3050988/openapi.do 
- 김포시 법정동 코드 - 4157000000
- 아파트 분양권전매 신고정보
> 일반 인증키  
> piLQMdjVMa9MniGNBO8EJ33uVdnBxExDigHFi3LHPYLlhu7JVrb2S7tbcS1cT7sfSR6yjcBo3OqIBplQskTXXg%3D%3D  
> End Point  
> http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc

#### api 사용 신청하기 - 사용신청 후 신청가능
- 시크릿 발급받기

#### 서브페이 데이터 수집하기
- http://www.netd.ac.za/ 크롤링
- https://www.ncbi.nlm.nih.gov

#### 쿠팡에서 상품정보 수집하기 
- url 분석하기
- 1개의 url에 있는 60개 상품정보 수집하기
- https://www.coupang.com/np/categories/186764?page=1
- https://www.coupang.com/np/categories/186764?page=2

