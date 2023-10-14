users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

data = {
    "Общее количество": 0,
    "Уникальные посещения": 0
}

data["Общее количество"] = len(users)
data["Уникальные посещения"] = len(set(users))

print(data)