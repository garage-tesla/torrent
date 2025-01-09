import webbrowser


def download(games, index):
    print("Вы скачали", games[index])


def go_to_fandom(index, links):
    webbrowser.open(links[index])


a = [1, 2, 3, 4, 5, 6]
print(a[5])
