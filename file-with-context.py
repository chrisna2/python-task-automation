#file = open('hello.txt','r',encoding='utf-8')
#lines = file.readlines()
#print(lines)


with open("hello.txt","r",encoding='utf-8') as file:
    lines = file.readlines()
    print(lines)