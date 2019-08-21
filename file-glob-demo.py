'''
glob 을 이용, 파일의 목록을 읽어 올 수 있다.
- 윈도우의 dir 과 리눅스의 ls 명령과 유사한 glob 모듈
- glob.glob(‘*’) : 현재 디렉토리의 모든 파일을 리스트로 반환

★ 윈도우에서 항상 경로를 설정할때 \\ 로 디렉토리 구분
D:\\tyn_dev\\workspace_pycham\\task-automation
'''
# os 현재 경로 확인
import os
# glob 디렉토리 설정 변경
import glob

print(os.getcwd())
print(glob.glob('*'))

print(os.path.getmtime("file-error-demo.py")) # 수정 시간
print(os.path.getctime("file-error-demo.py")) # 입력 시간

os.chdir('../') # 디렉토리 경로 변경
print(os.getcwd())
print(glob.glob('*'))

'''
__inner-method__

'__' 내부에서만 사용된다는 파이썬의 약속

os.mkdir('test-job') 디렉토리 만들기

file.name
'file-error-demo.py'
file.mode
'r'
os.path.getmtime("file-error-demo.py")
1566354858.7447028
os.path.getctime("file-error-demo.py")
1566354858.7447028
os.mkdir('test-job')
os.chdir('test-job')
os.getcwd()
'D:\\tyn_dev\\workspace_pycham\\task-automation\\test-job'
os.chdir('../')
os.getcwd()
'D:\\tyn_dev\\workspace_pycham\\task-automation'
import shutil
shutil.copy("hello.txt",'./test-job')
'./test-job\\hello.txt'
shutil.copy("hello.txt",'./test-job/hello-20190821.txt')

'''
