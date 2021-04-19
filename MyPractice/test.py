import time
import json
class Student():
    def __init__(self,name,age,tel):
        self.name = name
        self.age = age
        self.tel = tel

    def __str__(self):
        return f"{self.name}-{self.age}-{self.tel}"

stu = Student("lxfly",1111,1123243435)

dic1 = {"name":"lala", "age":111, "tel":15110302520}
dic2 = dict(name="lxfly")

list1 = []
list2 = []


dic3 = dict()

list1.append(stu)
list2.append(dic1)

print(list1)
print(list2)

#print(list1)
#print(json.dumps(list2))
