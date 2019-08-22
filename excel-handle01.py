import openpyxl

'''
 엑셀 파일의 데이터 출력
'''


def main():
    wb = openpyxl.load_workbook("D:\\tyn_dev\workspace_pycham\\task-automation\\excel_files\\2017.12.1.xlsx")
    sheet = wb['Sheet']
    print(sheet['C'])
    for cell in sheet['C']:
        print(cell.value)

        
main()