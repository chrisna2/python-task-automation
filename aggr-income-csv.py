import os
import glob
import csv
"""
파이썬은 덕후들이 만든 언어
-> 코딩 할때 스타일을 공식적으로 지정해 놓았다.
-> 스타일에 벗어나면 노란색의 및줄이 쳐진다.
-> 세상에 이런 언어는 두개 뿐이다. 파이썬과 Go
-> 어우 찌릉내
"""

SALES_FILE_PATH = "D:\\tyn_dev\\workspace_pycham\\task-automation\\csv_files"


def get_sales_files():
    files = glob.glob(os.path.join(SALES_FILE_PATH, "*.csv"))
    return files


def calc_total_sale(file_month):
    with open(os.path.join(SALES_FILE_PATH, file_month), 'r', encoding="UTF-8") as file :
        sum_sales = 0
        # 1에서 부터 끝까지
        for line in file.readlines()[1:]:
            sum_sales += int(line.split(',')[1])

        return sum_sales

def create_year_csv_from_result(result_data):
    print(result_data)

    with open('year_month_sales.csv','w', newline='', encoding='utf-8') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(['년', '월', '매출'])

        for idx, month_data in enumerate(result_data):
            csv_writer.writerow(['2017', str(idx+1).rjust(2, '0'), month_data])

    pass


def main():
    files = get_sales_files()

    result_data = []

    for file_month in files:
        total_sales = calc_total_sale(file_month)
        result_data.append(total_sales)

    create_year_csv_from_result(result_data)
    print("job's done!")


main()
