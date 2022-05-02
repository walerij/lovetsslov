#from cgitb import reset
import random
class game:
    def __init__(self) -> None:
        self.game = 'game'
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
        #list = self.word_to_char(word)
        #etalon = self.word_to_char(self.quest)
        x=0
        screz=0
        result=''
        for i in word:
            find = self.quest.find(i)
            if (find==-1):
                pass            
            elif(x==find):
                i=self.color_char(i,'green')
                screz+=1
            elif (x!=find):
                i=self.color_char(i,'red')

            result =result+i
            x+=1
        if screz==5:
            return result+"-слово угадано!"
        return result     


    def check(self, word):
        result=[]
        x=0
        screz=0
        if word==self.quest:
            for i in word:
                result.append([i,'green'])
            self.game='end'    
            return result
        elif word!=self.quest:
            for i in word:
                find = self.quest.find(i)
                if (find==-1):
                    result.append([i,''])            
                elif(x==find):
                    result.append([i,'green'])
                    screz+=1
                elif (x!=find):
                    result.append([i,'red'])            
                x+=1                  
            return result



