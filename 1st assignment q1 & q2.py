#Q:1
class Data:
    def __init__(self,hobbies,info):
        self.info=info
        self.hobbies=hobbies
        
    def Info(self):
        print(self.info)
    
    def Hobbies(self):
        print('My hobbies are ' +self.hobbies)
        
shaiz=Data('swimming,reading','i m shaiz i am 20 years old and i like cs')
shaiz.Info()
shaiz.Hobbies()

shaiz.info='i am ali and i am 10 years old'
shaiz.Info()
shaiz.hobbies='cycling,programming'
shaiz.Hobbies()


#Q:2

#create a class dinner having dishes insdie dinner class such as soup, salad, course,desert,juice
#create methods that can print these dishes inside dinner such as soup,salad, course, desert, jouce
#create objects of your friends and change parametrs according to each friend

class Dinner:
    def __init__(self,soup,salad,course,desert,juice):
        self.soup=soup
        self.salad=salad
        self.course=course
        self.desert=desert
        self.juice=juice
        
    def Soup(self):
        print("you ordered " + self.soup + " in soup")
    def Salad(self):
        print("you ordered " + self.salad + " in salad")
    def Course(self):
        print("you ordered " + self.course + " in course")
    def Desert(self):
        print("you ordered " + self.desert + " in desert")
    def Juice(self):
        print("you ordered " + self.juice + " in juice")
        
mydish=Dinner('1 hot&sour','1 fruit','2 noddles','1 cake','1 orange')
mydish.Soup()
mydish.Salad()
mydish.Course()
mydish.Desert()
mydish.Juice()

#friend
mydish.soup='chicken soup'
mydish.salad='10fruit'
mydish.course='rice'
mydish.desert='brownies'
mydish.juice='10 mango'

        