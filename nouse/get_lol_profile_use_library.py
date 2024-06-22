from riotwatcher import LolWatcher, ApiError

watcher = LolWatcher('RGAPI-c71fd0d8-840a-4c01-87f3-afe81ffa36ea')
my_region = 'jp1'

me = watcher.summoner.by_name(my_region, 'みみした#mimi')
print(me)