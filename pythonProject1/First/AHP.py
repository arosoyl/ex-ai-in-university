import numpy as np
import pandas as pd

data = pd.read_csv("data.csv", header=None)
print(data)
#print(data[:][1])

a = [0.00,0.00,0.00,0.00] # mang gia tri tong theo cot
b = [] # mang gia tri sau khi chia cho tong
c = [] # mang gia tri trung binh

def sum_col(col): # ham tinh tong
    for i in range(0,4):
        a[col] += data[i][col]
    return a[col]

def div_col(col):
    for i in range(0,4):
        a[col] = np[col][i] / sum_col(col)


def sum_row(row): # ham tinh tong theo hang
    for i in range(0,4):
        b[row] = np[i][row] / sum_col(row)

def avegr_value(row): # ham tinh giá trị trung bình theo hàng
    for i in range(0,4):
        b[i] += a[row]/sum_col(row)
        b[i] /=4

# buoc 2: lấy giá trị từng ô chia cho sum_col lưu vào 1 ma trận
# buoc 3: tính giá trị trung bình của ma trận theo từng hàng
# buoc 4:

#chuong trinh chinh
# buoc 1: tinh tong theo cot sum_col
for i in range(0,4):
    print(sum_col(i))






















