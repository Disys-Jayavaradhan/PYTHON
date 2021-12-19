'''approach'''
name='deepak'


'''approach 2'''

class friday:
    __work="python"
    def __init__(self):
        self.__tea=5
    def display(self):
        print(self.__tea)


deepak=friday()
deepak.display()


'''approach 3'''
saturday=("sleep","eat","play","repeat")
print (saturday [3])

'''approach 4'''

sunday={"morning":"idly","afternoon":"watchingtv","evening":"worriedstudents"}
print (sunday["morning"])

'''approach 5'''
print(saturday)
for i in saturday:
    print(i)
for i in sunday.values():
    print(i)
for i in sunday.keys():
    print(i)

''' approach 6'''
students=[{"id":23,"name":"anu","branch":"bba"},{"id":67,"name":"jaya","branch":"bba"},{"id":29,"name":"jai","branch":"bba"}]
print(students[0],students[1])


for i in students:
    if i["name"]=="anu":
        print("anu is available")
    elif i["branch"]=="bba":
        print("bba")
        



