import random
class game:
    def __init__(self) -> None:
        self.workslist= []
        with open("words.txt",'r') as f:
            self.workslist=f.read().splitlines()                   
        self.quest=self.workslist[random.randint(0,len(self.workslist))]
        self.win=""

    def check(self,word):
        result=[] 
        if(word==self.quest):
            for i in word:
                result.append([i,'green']) 
            self.win='user'    
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