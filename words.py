#функция разбивки слова на символы
# разбивает слово на символы и передает его в массиве
def word_to_char(word):
    result=[]
    for i in word:
        result.append(i)

    return result    


#создает слово из разноцветных букв
def color_char(content):
    word =""
    x=0
    for i in content:
        if(x==2):
            i="\033[31m"+i+"\033[0m" #красный цвет
        elif (x==4):
            i="\033[32m"+i+"\033[0m" #зеленый цвет
        word+=str(i)
        x+=1

    return word



#создадим непрерывающийся цикл

game = "game"
step = 1 #в начале мы делаем первый шаг
while game == "game":
    you_word=input("Введите слово:") #введите Ваше слово    
    print(color_char(you_word)) #распечатаем слово с перекрашенными символами
    if step==6: #если сделано 6 шагов
        print("Вы исчерпали все варианты") #вывод сообщения
        game="end" #выход из бесконечного цикла
    step+=1 #число шагов увеличиваем на единицу
