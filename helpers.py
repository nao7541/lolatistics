import requests
from urllib.parse import urlencode
import settings


def get_puuid_from_riotid(region=settings.DEFAULT_REGION):
    """
    ACCOUNT-V1 APIポータル用ラッパー
    RIOTIDからpuuid情報を取得する
    returns: str型のpuuid情報または問題がある場合はなし
    """

    game_name = settings.GAME_NAME
    tagline = settings.TAGLINE

    params = {
        'api_key': settings.API_KEY
    }
    # riotIDからアカウント固有のpuuidを取得する
    api_url = f"https://{region}.api.riotgames.com/riot/account/v1/accounts/" \
        f"by-riot-id/{game_name}/{tagline}"

    try:
        response = requests.get(api_url, params=urlencode(params))
        response.raise_for_status()
        return response.json()['puuid']
    except requests.exceptions.RequestException as e:
        print(f'Issue getting summoner data from API: {e}')
        return None


def get_summoner_info_from_puuid(puuid=None, region_code=settings.DEFAULT_REGION_CODE):
    """
    SUMMONER-V4 APIポータル用ラッパー
    PUUIDからサモナー情報を取得する
    returns: 辞書型のサモナー情報または問題がある場合は無し
    """
    params = {
        'api_key': settings.API_KEY
    }
    # PUUIDからサモナー情報を取得する
    api_url = f"https://{region_code}.api.riotgames.com/lol/summoner/v4/summoners/" \
        "by-puuid/{puuid}"

    try:
        response = requests.get(api_url, params=urlencode(params))
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f'Issue getting summoner data from API: {e}')
        return None


def get_match_ids_from_puuid(puuid, matches_count, region=settings.DEFAULT_REGION):
    """
    サモナーが最近プレイしたマッチのマッチ ID のリストを取得します。

    引数:
        summoner_puuid (str): サモナーの PUUID (プレイヤーの汎用固有 ID)。
        matches_count (int): 取得するマッチ ID の数
        region (str、オプション): サモナーが配置されているリージョンデフォルトは settings.DEFAULT_REGION の値

    戻り値:
        list または None: 成功した場合はマッチ ID のリスト, API リクエスト中にエラーが発生した場合はなし。

    発生するもの:
        requests.Exceptions.RequestException: API リクエストに問題がある場合。

    例:
        get_matches_by_summoner('sample_puuid', 10, 'na')
    """
    params = {
        'api_key': settings.API_KEY,
        'count': matches_count
    }
    api_url = f"https://{region}.api.riotgames.com/lol/match/v5/matches/" \
        f"by-puuid/{puuid}/ids"

    try:
        response = requests.get(api_url, params=urlencode(params))
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f'Issue getting summoner match data from API: {e}')
        return None


def did_player_win_match(puuid, match_id, region=settings.DEFAULT_REGION):
    params = {
        'api_key': settings.API_KEY
    }
    api_url = f"https://{region}.api.riotgames.com/lol/match/v5/matches/{match_id}"

    try:
        response = requests.get(api_url, params=urlencode(params))
        response.raise_for_status()
        match_data = response.json()
    except requests.exceptions.RequestException as e:
        print(f'Issue getting summoner match data from API: {e}')
        return None

    if puuid in match_data['metadata']['participants']:
        player_index = match_data['metadata']['participants'].index(puuid)
    else:
        return None

    player_info = match_data['info']['participants'][player_index]
    return player_info['win']
