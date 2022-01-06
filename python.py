# 辞書

enemyArray = ["スライム", "モンスター", "ドラゴン"]
print(enemyArray)
print(enemyArray[0])

enemyDictionary = {"ザコ" : "スライム", "中ボス" : "ドラゴン", "ラスボス" : "魔王" }
print(enemyDictionary)
print(enemyDictionary["中ボス"])

level = "ラスボス"
print(enemyDictionary)
print(enemyDictionary[level])

print(len(enemyDictionary))
enemyDictionary["ザコ２"] = "メタルモンスター"
print(enemyDictionary)
print(len(enemyDictionary))
enemyDictionary["中ボス"] = "メタルドラゴン"
print(enemyDictionary)

# del enemyDictionary["ザコ"]
# print(enemyDictionary)

for (rank, enemy) in enemyDictionary.items():
    print(enemyDictionary[rank] + "が現れた")
    print(rank + "の" + enemy + "が現れた")