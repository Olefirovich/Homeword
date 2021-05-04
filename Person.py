
class Person:
    def __init__(self,name,surname, qualification = 1):
        self.name = name
        self.surname = surname
        self.qualification = qualification
        print(self.name,self.surname,self.qualification)
        a = input()
    def __del__(self):
        print('До свидания, мистер', self.name, self.surname, self.qualification)
Person_1 = Person('name', 'surname')
Person_2 = Person("Alexeu", "alexeu")
Person_3 = Person('dasd','dasddasdasdasda')
del(Person_1)
input()
