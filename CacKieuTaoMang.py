import numpy as np
from numpy.core.fromnumeric import size

# Tạo mảng 1 chiều-----------------------------
a = np.array([1,2,5,7,0,8])
print(a)
print("Loại dữ liệu của biến a",type(a))
print("Kiểu dữ liệu của phần tử trong mảng a:",a.dtype)
print("Kích thước của mảng a:", a.shape)
print("Số phần tử của mảng a:",a.size)
print("Số chiều của mảng a:",a.ndim)

# Tạo mảng 2 chiều----------------------------
b = np.array([(4,5,6.0),(1,2,3.5)])
print(b)
print("Loại dữ liệu của biến b",type(b))
print("Kiểu dữ liệu của phần tử trong mảng b:",b.dtype)
print("Kích thước của mảng b:", b.shape)
print("Số phần tử của mảng b:",b.size)
print("Số chiều của mảng b:",b.ndim)

# Tạo mảng 3 chiều---------------------------
c = np.array([[(2,4,0,6),(4,5,6,3)],[(2,4,6,2),(9,3,7,4)],[(4,6,7,3),(4,5,3,7)]])
print(c)
print("Loại dữ liệu của biến a",type(c))
print("Kiểu dữ liệu của phần tử trong mảng a:",c.dtype)
print("Kích thước của mảng a:", c.shape)
print("Số phần tử của mảng a:",c.size)
print("Số chiều của mảng a:",c.ndim)

# Vd 1: Tạo ma trận 0|1 kích thước m x n Slide 18-------------------------
array_zeros = np.zeros((5,3))
print("Vd 1: Tạo ma trận 0|1 kích thước m x n Slide 18-------------------------")
print(array_zeros)
print("Kiểu dữ liệu trong mảng array_zeros:",array_zeros.dtype)
print("Kích thước của mảng array_zeros:",array_zeros.shape)
print("Số phần tử của mảng array_zeros:",array_zeros.size)
print("Số chiều của mảng array_zeros:",array_zeros.ndim)

#VD2: Tạo ma trận đơn vị cấp n (ma trận chéo)---------------------
array_eye = np.eye(5)
print("VD2: Tạo ma trận đơn vị cấp n---------------------")
print(array_eye)
print("Kiểu dữ liệu trong mảng array_eye",array_eye.dtype)
print("Kích thước của mảng array_eye",array_eye.shape)
print("Số phần tử của mảng array_eye",array_eye.size)
print("Số chiều của mảng array_eye",array_eye.ndim)

# VD3: Tạo ma trận với các phần tử ngẫu nhiên trong khoảng (0,1)---------------
array_random = np.random.random((7,5))
print("VD3: Tạo ma trận với các phần tử ngẫu nhiên trong khoảng (0,1)---------------")
print(array_random)
print("Kiểu dữ liệu trong mảng array_random",array_random.dtype)
print("Kích thước của mảng array_random",array_random.shape)
print("Số phần tử của mảng array_random",array_random.size)
print("Số chiều của mảng array_random",array_random.ndim)

# Vd 5: Tạo vector với các tham số thiết lập-----------------------
# Tọa vecto:
# Phần tử đầu tiên = a
# Kết thúc<b
# Mỗi phần tử cách nhau một khoảng =steps
d = np.arange(1,15,2)
print("Vd 5: Tạo vector với các tham số thiết lập-----------------------")
print("Vector d: ",d)
print("số phần tử của vector d:",d.size)
print("----------------------------------------")
# Phương thức Linspace (a,b,num)
# Tạo vector:
# Phần tử đầu tiên = a
# Phần tử kết thúc = b
# Số phần tử của ma trận = num
f = np.linspace(1,15,11)
print("Vector f:",f)
print("Số phần tử của vector f:",f.size)

# Đọc dữ liệu từ file txt vào biến mảng
path = 'filetaodiem.txt'
diem_2a = np.loadtxt(path,delimiter=',',dtype=np.int)
print(diem_2a)
print("Kiểu dữ liệu của phần tử trong mảng 2a:",diem_2a.dtype)
print("Kích thước của mảng 2a:", diem_2a.shape)
print("Số phần tử của mảng trên 2a:",diem_2a.size)
print("Số chiều của mảng điểm 2a:",diem_2a.ndim)