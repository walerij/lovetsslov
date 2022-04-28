import random
class game:
    def __init__(self) -> None:
        self.workslist= ["почка","печка","конец","игрок","стена","масло"]
        self.quest=self.workslist[random.randint(0,len(self.workslist))]
        print(self.quest)