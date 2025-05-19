from .fetcher.fetchers import SpreadSheetFetcher, GoogleCalendarFetcher, APIServerFetcher


def start(options:dict={}):

    fetchers = [SpreadSheetFetcher(options['excel']), GoogleCalendarFetcher(options['calendar']), APIServerFetcher(options['api'])]

    for fetcher in fetchers:
        fetcher.fetch("url")