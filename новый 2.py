import math
def get_totem(year):
    etalon = 1976
    totems=[
        "Темный Сох (Лось)",
        "Жалящий Шершень (Оса)",
        "Притаившийся Лют (Волк)",
        "Огненная Векша (Белка)",
        "Жемчужная Щука",
        "Бородатая Жаба",
        "Дикий Вепрь (Кабан) ",
        "Белый Филин",
        "Шипящий Уж ",
        "Крадущийся Лис",
        "Свернувшийся Еж",
        "Парящий Орел",
        "Прядущий Мизгирь (Паук) ",
        "Кричащий Петух",
        "Златорогий Тур (Бык)",
        "Огнегривый Конь"
    ]

    ost=abs((year-etalon)%16)
    return totems[ost]

file:///E:/html_js/less/vkgor/...
you_year =  input("Введите год: ")

print(get_totem(int(you_year)))


