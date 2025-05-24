from .fetcher.fetchers import get_data_from_server

# 프로그램 시작 함수. 해당 파일에서는 기존에 만든 컴포넌트를 모아서 조립한 후, 조절하여 실행하는 기능을 담당
def start(options:dict={}):

    params = {
        "branch" : "beomgye",
        "start_date" : "2025-03-24",
        "end_date" : "2025-05-24",
        "min_total": 0
    }

    get_data_from_server("https://culcom.co.kr/cs/sporex/check_successrate.php", params)


