import random
class game:
    def __init__(self) -> None:
        self.game = game
        self.worklist = ['мираж','конец','фильм',"иваси","камин","визит","стиль","бобби","тапир","шпага","сабля"]
        self.i = random.randint(0,len(self.worklist))
        self.quest = self.worklist[self.i]
        print(self.quest)


#функция разбивки слова на символы
# разбивает слово на символы и передает его в массиве
    def word_to_char(self, word):
        result=[]
        for i in word:
            result.append(i)

        return result    


#складывает буквы в слово
    def char_to_word(self, list):
        word =""
        x=0
        for i in list:
            word+=str(i)
            x+=1

        return word



#меняет цвет символа на красный или зеленый
    def color_char(self,char, color):
        if color=='red':
            char = "\033[31m"+char+"\033[0m" #красный цвет
        elif color == 'green':
            char="\033[32m"+char+"\033[0m" #зеленый цвет    
        return char


#метод проверки слова
    def game_check(self, word):
        if (len(word)!=5):
            return "слово не подходит"
        list = self.word_to_char(word)
        etalon = self.word_to_char(self.quest)
        x=0
        for i in list:
            find = etalon.index(i)
            if (find==-1):
                pass            
            if(x==find):
                i=self.color_char(i,'green')
            elif (x!=find):
                i=self.color_char(i,'red')

        return(self.char_to_word(list))        



