from abc import ABC,abstractmethod

class Button(ABC):

    def __init__(self,set_link):
        self.link = set_link

    @abstractmethod
    def click(self):
        pass


class PushButton(Button):
    
    def click(self):
        print("Go To: {}".format(self.link))



tombol1 = PushButton("www.kelasterbuka.id")
tombol1.click()	



tombol1.link = "hallo"
tombol1.click()










