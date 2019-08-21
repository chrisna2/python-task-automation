'''
part2 업무 자동화
'''

favorite_colors = ['red', 'blue', 'yellow', 'white', 'black']

new_colors = []

for color in favorite_colors:
    new_colors.append(color+"\n")


file = open('favorite_colors.txt','w', encoding='UTF-8')

'''
w : 새로 덮어쓰기
a : 해당 글자 계속 추가 삽입
'''

# 파이썬에서 메소드는 self를 기본적으로 받게 되어 있다.
file.write('내가 좋아하는 색상\n')

file.writelines(favorite_colors)
file.writelines(new_colors)

file.close()

print("file operation ok..")

'''
파일이 실행되는 경로에 파일이 생성된다.
파이썬은 기본적으로 UTF-8 코드로 설정 되있는데
윈도우만 MS949로 설정되어 한글이 깨짐
'''