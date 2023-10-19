users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

site = {
        "Общее количество" : 0,
        "Уникальные посещения" : 0
        }
uesrs2 = list(set(users))


site["Уникальные посещения"] = len(uesrs2)
site["Общее количество"] = len(users)

print(site)



# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
