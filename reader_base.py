import unittest
import urllib.request as urllib2
import json

class Reader_Base():
    def __init__(self, api_key):
        print("Reader_Base.py:__init__")
        self._api_key = "api_key" + api_key
        self._api_url = "" # オーバーライドしたクラスで記載する
    
    def get(self, last_path):
        """
        apiアクセスの結果を取得する

        args:
            last_path: str
                apiアクセスのパス
        """
        print("Reader_Base.py:get")
        url = self._create_url(last_path)

        with self._get_url_session(url) as f:
            ret = self._jsonLoad(f, 'utf-8')
        
        return ret
    
    def _jsonLoad(self, session, character_map):
        """
        json形式でロードする
        """
        print("Reader_Base.py:_jsonLoad")
        return json.loads(session.read().decode(character_map))
    
    def _get_url_session(self, url):
        """
        open url session.

        returns:
            opened session
        """
        print("Reader_Base.py:_get_url_session")
        return urllib2.urlopen(url)
    
    def _create_url(self, lastPath):
        """
        create api access url
        """
        print("Reader_Base.py:_create_url")
        url = self._api_url
        url += lastPath
        url += "?"
        url += self._api_key
        return url