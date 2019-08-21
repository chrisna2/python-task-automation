'''
텍스트 파일 읽기
'''

file = open('favorite_colors.txt', 'r', encoding='UTF-8')
# r 은 생략이 가능하다.
line = file.readline()
lines = file.readlines()
# 파일을 항상 닫아주어야 한다.
file.close()

print(line)
print(lines)