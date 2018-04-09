class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s:%s'%(self.__name, self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

bart = Student('bart person', 59)
print(bart.get_name())
print(type(bart))