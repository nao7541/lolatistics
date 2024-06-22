from . import info
from . import reader_base

class Reader(reader_base.Reader_Base):
    def __init__(self, api_key):
        print("Summoner.Reader.py:__init__")
        self._api_key = "api_key=" + api_key
        self._api_url = "https://jp1.api.riotgames.com/lol/summoner/v4/summoners/"

    def get_by_summoner(self, summoner_name):
        print("Summoner.Reader.py:get")
        lastpath = "by-name/" + summoner_name

        return info.Info(self.get(lastpath))