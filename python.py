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


# リストの整列 

wepons = ["2.イージスト","1.ウインドスピア","3.アースブレイカー","4.稲妻ハンマー"]

print(wepons)

print(sorted(wepons))
print(sorted(wepons, reverse=True))

# 辞書の配列
wepons = {"イージスト":40, "ウインドスピア":12, "アースブレイカー": 50, "4.稲妻ハンマー":99}
print(wepons)

print(sorted(wepons))

# アイテム一覧


