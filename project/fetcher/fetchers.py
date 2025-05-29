import requests
from bs4 import BeautifulSoup
import pandas as pd

# 1. 현재 날짜를 구한다.
# 2. 현재 날짜에 해당하는 행을 구한다
# 3. 이 중, 양수인 값만 가지고 집계한다
# 4. 집계 후, 총 건수(양수인 것만) + 총 합계(양수인 것만)
def get_data_from_excel(url, params={}):
    data_path = './sample_data/membership.xlsx'
    df = pd.read_excel(data_path, skiprows=1)
    
    매출정보_idx = ["일자", "멤버쉽", "이름", "언어", "수단", "코멘트"]
    멤버쉽_idx = ["타입", "금액.1"]
    매출정보_df = df[매출정보_idx]
    
    멤버쉽_df = df[멤버쉽_idx]
    
    df = pd.merge(매출정보_df, 멤버쉽_df, left_on='멤버쉽', right_on='타입').drop('타입', axis=1)
    
    today = '2020.05.01'
    
    filtered = df[df["일자"]==today]
    
    
    total_sum = filtered['금액.1'].sum()
    print(total_sum)

def get_data_from_server(url, params={}):
    response = requests.post(url, data=params)
    response.encoding = 'utf-8'
    if response.status_code == 200:
        res_text = response.text
        soup = BeautifulSoup(res_text, "html.parser")
        table = soup.find('table', id='statsTable')

        rows = table.find_all('tr')[1:]

        whole_cnt = 0
        whole_success = 0
        whole_fail = 0

        for row in rows:
            colums = row.find_all("td")
            cnt = colums[1].get_text(strip=True)
            success_cnt, _ = colums[2].get_text(strip=True).split(" ")
            fail_cnt, _ = colums[3].get_text(strip=True).split(" ")

            whole_cnt += int(cnt)
            whole_success += int(success_cnt)
            whole_fail += int(fail_cnt)

        res_ = {
            "params": params,
            "stat":{
                "whole_cnt": whole_cnt,
                "whole_success": whole_success,
                "whole_fail": whole_fail,
                "success_rate": (whole_success / whole_cnt) * 100,
                "fail_rate": (whole_fail / whole_cnt) * 100
            }
        }

        print(res_)

        return res_
