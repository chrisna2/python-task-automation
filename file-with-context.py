#file = open('hello.txt','r',encoding='utf-8')
#lines = file.readlines()
#print(lines)

# with 파일이 자동으로 닫힌다. file.close 자동실행
with open("hello.txt","r",encoding='utf-8') as file:
    lines = file.readlines()
    print(lines)