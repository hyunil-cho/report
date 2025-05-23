from .fetcher.fetchers import SpreadSheetFetcher, GoogleCalendarFetcher, APIServerFetcher

# 프로그램 시작 함수. 해당 파일에서는 기존에 만든 컴포넌트를 모아서 조립한 후, 조절하여 실행하는 기능을 담당
def start(options:dict={}):

    fetchers = [SpreadSheetFetcher(options['excel']), GoogleCalendarFetcher(options['calendar']), APIServerFetcher(options['api'])]

    for fetcher in fetchers:
        fetcher.fetch("url")
