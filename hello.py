

#функция разбивки слова на символы
# разбивает слово на символы и передает его в массиве
def word_to_char(word):
    result=[]
    for i in word:
        result.append(i)

    return result    


#создает разноцветное слово
def color_char(list):
    word =""
    x=0
    for i in list:
        if(i[1]=='red'):
            i[0]="\033[31m"+i[0]+"\033[0m" #красный цвет
        elif (i[1]=='green'):
            i[0]="\033[32m"+i[0]+"\033[0m" #зеленый цвет
        word+=str(i[0])
        x+=1

    return word


#создадим непрерывающийся цикл

from unittest import result
from g1 import game

game_=game()

cond=1
sc=1
while cond==1:
    if(sc==6):
        cond=3
   
    name=input("Введите слово:")
    #print(game_.color_char(name,'red'))
    result = color_char(game_.check(name))
    print (result)
    if(game_.game=='end'):
        cond=3 
    # if (result.find("-слово угадано!")!=-1):
    #    cond=3
    #    re.finditer() нам надо копать в сторону этой функции
    #print(str(sc)+" hello, "+name)
    #char_word=word_to_char(name)
    #print(char_word)
    #print(len(char_word))

    #print(color_char(char_word))

    sc+=1 




