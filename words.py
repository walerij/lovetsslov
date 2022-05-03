#функция разбивки слова на символы
# разбивает слово на символы и передает его в массиве
def word_to_char(word):
    result=[]
    for i in word:
        result.append(i)

    return result    


#создает слово из разноцветных букв списка
def color_char(content):
    word =""    
    for i in content:
        if(i[1]=='red'):
            i[0]="\033[31m"+i[0]+"\033[0m" #красный цвет
        elif (i[1]=='green'):
            i[0]="\033[32m"+i[0]+"\033[0m" #зеленый цвет
        word+=str(i[0])
       

    return word



#создадим непрерывающийся цикл

gamestatus = "game"
step = 1 #в начале мы делаем первый шаг
from game import game
gameset = game()
while gamestatus == "game":
    you_word=input("Введите слово:") #введите Ваше слово    
    print(color_char(gameset.check(you_word))) #проверяем слово
    if gameset.win=='user':
        print("Победил пользователь") #вывод сообщения
        gamestatus="end" #выход из бесконечного цикла 
        break       
    if step==6: #если сделано 6 шагов
        gameset.win=='comp'
        print("Вы исчерпали все варианты") #вывод сообщения
        print("Победил компьютер. Загаданное слово: "+gameset.quest)
        gamestatus="end" #выход из бесконечного цикла
    step+=1 #число шагов увеличиваем на единицу
