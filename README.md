## Description

address-standardization 입니다.

poi\_addr, poi\_name, poi\_phone 등을 정규화하는 기능을 REST Web API 형태로 제공합니다.

현재는 poi\_addr 정규화 기능만 제공합니다.


## API Reference

**addr normalize**

주소정규화

- **URL**

  /addr/normalize

- **Method:**

  `GET`
  
-  **URL Params**

   **Required:**
 
   `addr=[string]`

- **Data Params**

  None

- **Success Response:**

  - **Code:** 200 <br />
    **Content:** `{ status_code : 200, status_msg: "success", normalized_addr : "경기도 수원시 팔달구 화서동 10-2" }`
 
- **Error Response:**

  - **Code:** 404 NOT FOUND <br />
    **Content:** `{ error : "User doesn't exist" }`

- **Sample Call:**

  ```javascript
    $.ajax({
      url: "/addr/normalize?addr=경기 수원 팔달구화서동 10-2 화서빌딩 2층",
      dataType: "json",
      type : "GET",
      success : function(r) {
        console.log(r);
      }
    });
  ```

아래 구글스프레드시트 참조

https://docs.google.com/a/kiwiple.com/spreadsheets/d/1ZH7QugzRgfIFJt6vSuz8M6KOEmfDwgJYc3QL3mDk5Qo/edit?usp=sharing


## 실행방법

서버에서 다음을 실행

$ screen python api-server/run.py


## 주소데이터 갱신방법

1. gov\_addr/raw\_data 이하의 .txt파일을 모두 삭제
2. http://www.juso.go.kr/support/AddressBuild.do 의 "01. 전체주소"에서 최신 주소데이터를 다운로드
3. 압축을 풀어서 gov\_addr/raw\_data 에 넣음
4. 다음을 실행

$ python gov\_addr/generate_all.py
