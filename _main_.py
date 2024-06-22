from helpers import get_puuid_from_riotid, get_summoner_info_from_puuid, \
                    get_match_ids_from_puuid, did_player_win_match


puuid = get_puuid_from_riotid()
print(puuid)
summoner = get_summoner_info_from_puuid(puuid)
print(summoner)
print(summoner['id'])

match_ids = get_match_ids_from_puuid(puuid, 20)
print(match_ids)

win = did_player_win_match(puuid, match_ids[0])
print(win)
