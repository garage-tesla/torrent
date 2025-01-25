# Список отзывов
from functions.our_methods import download, go_to_fandom

good = ["woowwww", "Super!!!!", "very good"]
normal = ["so so", "just ok", "i wouldnt play more that a hour"]
bad = ["bad", "bad bad", "i mean its really bad("]

# список игр
games = ["Terraria", "Mincraft", "DOTA2", "cs 2", "Ded sels", "Isac", "brawl", "GTA 5", "FIFA 2024", "Warcraft"]

# Список оценок
raticgs = ["10", "10", "2", "4", "8.5", "7", "6,8", '11', '9', '5']

# Список описания
description = ["Terraria:dsdfhgvjb cxdrftgyhjn cdfrtgyhbn bvgftyghbn",
               "Mincraft:awsedrfghbvgftv vcfcvhjn bgctyh yhvn",
               'DOTA2:rdfgv bvtyujn v  vftyhgfgyhgfrtyhgftyhb           gyhvdfgfyuhg',
               "cs 2:dfyhvcfghn cfghnbvfrtyhbvfghb ftyhbvcdrtyhgvcdrtgb ",
               'Ded sels:rfgbhdgvehvfheb vgudhghbhhgftyhb  ghgghghghggb ',
               'Isac:hghgfghb vghgghggh vghhgghgv vghgghgghgxddsedsweawedc,'
               'brawl:fuhgvghjhghhv ghjhgyugyuiugh hugyuygyuyguhgvbn gfyugfgyugfg',
               'GTA 5:cfghgfgygfygfg hfgyugugfgyhgfdfghgfdswertyhjnbv ghghgghvghvgg',
               "FIFA 2024:fghgfghgvghujhgvdghsjwmnbvfstwyujnb hyudjhwhjdmnb vwbhnd ",
               "Warcraft:bhjebvfghebfvgeb dehdbevghdn evghjen cvghen cvwhnq vghn ehnw"]

# Список отзывов
coments = [good, good, bad, normal, good, good, normal, good, good, normal]

# Список ссылок
links = ["https://google.com",
         "https://yandex.ru",
         "https://youtube.com",
         "https://figma.com",
         "https://github.com",
         "https://pinterest.com",
         "https://telegram.org",
         "https://mail.ru",
         "https://google.com","https://youtube.com"]

for i, game in enumerate(games):
    print(i, game)

index = int(input("Выберите игру из списка!!!!!"))
y = int(input("Выберите действие:\n"
      "0) Скачать\n"
      "1) Перейти в фандом\n"
      "2) Написать отзыв\n"
      "3) Посмотреть описание\n"))

if y == 0:
    download(games, index)
elif y == 1:
    go_to_fandom(index, links)

print("Женя")
print("Илья")
print("Миша")
