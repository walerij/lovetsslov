import random
from unittest import result
class game:
    def __init__(self) -> None:
        self.workslist= ["почка","печка","конец","игрок","стена","масло"]
        self.quest=self.workslist[random.randint(0,len(self.workslist))]
        print(self.quest)

    def check(self,word):
        result=[] 
        if(word==self.quest):
            for i in word:
                result.append([i,'green']) 
            return result
        elif word!=self.quest:
            pos = 0

            for i in word:
                find = self.quest.find(i)
                if find==-1:
                    result.append([i,''])
                elif find==pos:
                    result.append([i,'green'])
                elif find!=pos:
                    result.append([i,'red'])  
                pos+=1
            return result                  