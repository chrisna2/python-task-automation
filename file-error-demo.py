try:
    # 에러가 발생 할 수 있는 코드
    with open("hell.txt","r",encoding='utf-8') as file:
        lines = file.readlines()
        print(lines)

except FileNotFoundError as fne:
    # 에러 대신에 발생하는 코드
    print("파일을 읽을 수 없습니다.")
    print(fne)


print("파일 읽기 종료.")

# 에러가 발생하면 코드가 죽어 버린다.
# 따라서 에러 처리를 해야 한다.
'''
try:

except:

로그 분석 : [금융권] 사기 탐지

'''
