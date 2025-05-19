from abc import ABC, abstractmethod

from project.fetcher.datas import DataCapsule


class Fetcher(ABC):
    def __init__(self, option):
        self.option = option

    @abstractmethod
    def fetch(self, url: str) -> DataCapsule:
        pass


class SpreadSheetFetcher(Fetcher, ABC):

    def fetch(self, url: str) -> DataCapsule:
        print("bring data from google spreadsheet!")


class GoogleCalendarFetcher(Fetcher, ABC):

    def fetch(self, url: str) -> DataCapsule:
        print("bring data from calendar!")


class APIServerFetcher(Fetcher, ABC):

    def fetch(self, url: str) -> DataCapsule:
        print('bring data from api')
