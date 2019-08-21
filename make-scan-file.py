import os

try:
    os.mkdir("D:\\tyn_dev\\workspace_pycham\\work-for-python")
except:
    print("디렉토리가 존재하므로 생성은 과정은 패스")

os.chdir("D:\\tyn_dev\\workspace_pycham\\work-for-python")

print(os.getcwd())

'''
파이썬은 스트링과 숫자의 결합이 안된다.
'''
for int in range(200):
    file = open('scan-000'+str(int+1).rjust(3, '0')+'-demo-file.pdf','w')
    print(file.name+'_created...')
    file.close()
