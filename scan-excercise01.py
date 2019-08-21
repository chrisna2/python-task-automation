import os
import glob
import shutil

# 정리할 디렉토리를 생성한다.
# 임의로 설정 할것 my-job/scans 생성
try:
    os.mkdir("D:/tyn_dev/workspace_pycham/my-job/scans")
except Exception as ex:
    print("디렉토리가 존재하므로 생성은 과정은 패스")
    print(ex)

os.chdir("D:/tyn_dev/workspace_pycham/my-job/scans")

# my-job/scans/01 ~ 20 디렉토리 생성
# (len(glob.glob("*"))

if 0 >= len(glob.glob("*")):
    for int in range(20):
        os.mkdir(str(int+1).rjust(2, '0'))
else:
    print("디렉토리가 존재하므로 생성은 과정은 패스")

# 현재 cwd 를 work-for-python(스캔 원본이 있는 곳으로 이동)
os.chdir("D:\\tyn_dev\\workspace_pycham\\work-for-python")


print(glob.glob('*.pdf'))

if len(glob.glob('*.pdf')) > 0 :
    for pdf in glob.glob('*.pdf'):
        number = int(pdf[8:11])
        print(number)
        if 0 < number and 10 >= number:
            shutil.move(pdf, 'D:/tyn_dev/workspace_pycham/my-job/scans/01')
        elif 10 < number and 20 >= number:
            shutil.move(pdf, 'D:/tyn_dev/workspace_pycham/my-job/scans/02')
        elif 20 < number and 30 >= number:
            shutil.move(pdf, 'D:/tyn_dev/workspace_pycham/my-job/scans/03')
        elif 30 < number and 40 >= number:
            shutil.move(pdf, 'D:/tyn_dev/workspace_pycham/my-job/scans/04')
        elif 40 < number and 50 >= number:
            shutil.move(pdf, 'D:/tyn_dev/workspace_pycham/my-job/scans/05')
        elif 50 < number and 60 >= number:
            shutil.move(pdf, 'D:/tyn_dev/workspace_pycham/my-job/scans/06')
        elif 60 < number and 70 >= number:
            shutil.move(pdf, 'D:/tyn_dev/workspace_pycham/my-job/scans/07')
        elif 70 < number and 80 >= number:
            shutil.move(pdf, 'D:/tyn_dev/workspace_pycham/my-job/scans/08')
        elif 80 < number and 90 >= number:
            shutil.move(pdf, 'D:/tyn_dev/workspace_pycham/my-job/scans/09')
        elif 90 < number and 100 >= number:
            shutil.move(pdf, 'D:/tyn_dev/workspace_pycham/my-job/scans/10')
        elif 100 < number and 110 >= number:
            shutil.move(pdf, 'D:/tyn_dev/workspace_pycham/my-job/scans/11')
        elif 110 < number and 120 >= number:
            shutil.move(pdf, 'D:/tyn_dev/workspace_pycham/my-job/scans/12')
        elif 120 < number and 130 >= number:
            shutil.move(pdf, 'D:/tyn_dev/workspace_pycham/my-job/scans/13')
        elif 130 < number and 140 >= number:
            shutil.move(pdf, 'D:/tyn_dev/workspace_pycham/my-job/scans/14')
        elif 140 < number and 150 >= number:
            shutil.move(pdf, 'D:/tyn_dev/workspace_pycham/my-job/scans/15')
        elif 150 < number and 160 >= number:
            shutil.move(pdf, 'D:/tyn_dev/workspace_pycham/my-job/scans/16')
        elif 160 < number and 170 >= number:
            shutil.move(pdf, 'D:/tyn_dev/workspace_pycham/my-job/scans/17')
        elif 170 < number and 180 >= number:
            shutil.move(pdf, 'D:/tyn_dev/workspace_pycham/my-job/scans/18')
        elif 180 < number and 190 >= number:
            shutil.move(pdf, 'D:/tyn_dev/workspace_pycham/my-job/scans/19')
        elif 190 < number and 200 >= number:
            shutil.move(pdf, 'D:/tyn_dev/workspace_pycham/my-job/scans/20')
else:
    print("there is no files")

