

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
        if(x==2):
            i="\033[31m"+i+"\033[0m" #красный цвет
        elif (x==4):
            i="\033[32m"+i+"\033[0m" #зеленый цвет
        word+=str(i)
        x+=1

    return word


#создадим непрерывающийся цикл

cond=1
sc=1
while cond==1:
    if(sc==6):
        cond=3
    name=input("Введите слово:")
    #print(str(sc)+" hello, "+name)
    char_word=word_to_char(name)
    print(char_word)
    print(len(char_word))

    print(color_char(char_word))

    sc+=1 




