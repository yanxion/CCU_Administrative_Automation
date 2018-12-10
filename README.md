# 中正大學：兼任助理、臨時工工作日誌
===
## 此自動化填寫時數軟體 僅限中正大學使用
使用Python撰寫搭配Selenium與Chrome Driver

![](https://i.imgur.com/c0xfM2A.png =500x)

使用方式：

1. 更改default_set.json檔案，輸入自己的資料
```json=
{
    "plan_num": "plan_num",
    "acc": "account",
    "pwd": "password",
    "set_yy": "107",
    "set_mm": "10",
    "set_dd": [0],
    "set_hrs": [4,3,3,4,3,3,4,3,3],
    "set_workin": "整理資料"
  }
```
- plan_num：計畫編號，只需打前面的數字，e.g.,107-00001
  - ![](https://i.imgur.com/U0VyUTF.png =150x)
- acc：系統帳號
- pwd：系統密碼
- set_yy：工作日期 - 年份
    - ![](https://i.imgur.com/VPxu76V.png =400x)
- set_mm：工作日期 - 月份
    - ![](https://i.imgur.com/eRhYuzH.png =400x)
- set_dd：兩種寫法
    - 一種搭配set_hrs，兩個的總數要一樣，代表是日期與時間會是相對應的e.g., 1日報4小時，2日報3小時，3日報3小時...類推
      ```json=
        "set_dd": [1,2,3,4,5,6,7,8,9],
        "set_hrs": [4,3,3,4,3,3,4,3,3],
      ```
    - 一種只寫[0]，會自動根據set_hrs的時數隨機搭配日期。
      ```json=
        "set_dd": [0],
        "set_hrs": [4,3,3,4,3,3,4,3,3],
      ```
- set_hrs：預報帳的時數，各自拆開來，一格代表一天，一天不得超過4小時。
    - ![](https://i.imgur.com/PmVPlX5.png =300x)
    ```json=
        "set_hrs": [4,3,3,4,3,3,4,3,3], //代表要報25小時
    ```
- set_workin：工作內容，填入工作的內容。
    - ![](https://i.imgur.com/24XtyLT.png =300x)
 
## 使用方式：
上述資料填寫完成後，執行exe檔即可自動化輸入。

- 待改善：
    - 目前預設的登入身份都是兼任助理。
    - 目前時數沒辦法像日期一樣[0]。

