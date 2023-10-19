list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

pl1 = [0] *  int(len(list_players) / 2)
pl2 = [0] *  int(len(list_players) / 2)


for i in range(0, int(len(list_players)/2)):
    pl1[i] = list_players[i]
for i in range(int(len(list_players)/2), len(list_players)):
    pl2[i-3] = list_players[i]

print(pl1)
print(pl2)
# TODO Разделите участников на две команды
