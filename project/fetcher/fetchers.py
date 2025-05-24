import requests
from bs4 import BeautifulSoup


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
