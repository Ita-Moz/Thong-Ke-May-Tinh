import numpy as np
from numpy.core.fromnumeric import mean
from numpy.lib.function_base import append
import array as arr
#  TH KTMT T5 7-9
#  Lưu file ntn ngày 16/9/2021
# Thực hành 1__________________________________________________
# yêu cầu 1:
array_hs = np.random.randint(0,100,(12,12))
print("Thực hành 1")
print("Yêu cầu 1:")
print(array_hs)
print("Kiểu dữ liệu của mảng",array_hs.dtype)
print("Kích thước của ma trận",array_hs.shape)
print("Số phần tử của mảng",array_hs.size)
print("Số chiều của mảng",array_hs.ndim)

# Yêu cầu 2:
print("Thực hành 1 \t Yêu cầu 2:")
l = len(array_hs[0])
print("Vector các phần tử nằm trên đường chéo chính:")
for i in range(l):
  print(array_hs[i][i],end=" ")

print("\nVector các phần tử nằm trên đường chéo phụ:")
for i in range(l-1,-1,-1):
  print(array_hs[l-1-i][i],end=" ")

# Yêu cầu 3:
print("Thực hành 1 \t Yêu cầu 3:")
dem = 0
demnho = 0
demlon = 0
x = int(input("\nNhập vào giá trị x(0,100):"))
while(x < 0 or x > 100):
  if(x < 0 or x > 100 ):
    print("số nhập vào phải trong khoảng (0,100)!!!")
    x = int(input("\nNhập vào giá trị x(0,100):"))
else:
    print(array_hs)
    for m in range(12):
      for n in range(12):
        if(x == array_hs[m][n]):
          dem+=1
        elif(array_hs[m][n] <= x ):
          demnho+=1
        elif(array_hs[m][n] >= x ):
          demlon+=1
    print("Số phần tử có giá trị bằng x:",dem)
    print("Số phần tử có giá trị nhỏ hơn x:",demnho)
    print("Số phần tử có giá trị lớn hơn x:",demlon)

# Thực hành 2
# yêu cầu 1
print("\nThực hành 2\n Yêu cầu 1:")
array_diem = np.random.randint(0,10,(10,30))
print(array_diem)
print("Cách 1:")
for i in range(0,array_diem.shape[1]):
  print("Điểm trung bình của học sinh",i+1,":",array_diem[:,i].mean())
print("Cách 2:")
mean2a = array_diem.mean(axis=0)
# axis = 0 theo hàng, axis = 1 theo cột
print("Điểm trung bình của tất cả học sinh:")
for i in range(0,mean2a.size):
  print("Điểm của học sinh ",i+1,":",mean2a[i])
for i in range(0,mean2a.size):
  if(mean2a.max()==mean2a[i]):
    print("Học sinh",i+1,"điểm trung bình cao nhất:",mean2a.max())
  elif(mean2a.min()==mean2a[i]):
    print("Học sinh",i+1,"điểm trung bình thấp nhất:",mean2a.min())

# yêu cầu 2:
print("\nThực hành 2\t Yêu cầu 2:")
mean2b = array_diem.mean(axis=1)
# axis = 0 theo hàng, axis = 1 theo cột
print("Điểm trung bình của tất cả Môn học:")
for i in range(0,mean2b.size):
  print("Điểm của môn thứ ",i+1,":",mean2b[i])
for i in range(0,mean2b.size):
  if(mean2b.max()==mean2b[i]):
    print("\nMôn học",i+1,"có điểm trung bình cao nhất:",mean2b.max())
  elif(mean2b.min()==mean2b[i]):
    print("Môn học",i+1,"có điểm trung bình thấp nhất:",mean2b.min())

# Yêu cầu 3:
print("\nThực hành 2\t Yêu cầu 3:")
print(array_diem)
stddiem  = []
for i in range(array_diem.shape[1]):
  stddiem.append(array_diem[:,i].std())
for i in range(array_diem.shape[1]):
  if(min(stddiem)==array_diem[:,i].std()):
    print("Học sinh học đồng đều nhất:",i+1,"\nBảng điểm của học sinh học đồng đều:",array_diem[:,i])
    print("Học sinh này có độ lệch chuẩn thấp là:",min(stddiem),"nên có độ đồng đều giữa các điểm số")
stdmon = []
for i in range(array_diem.shape[0]):
  stdmon.append(array_diem[:,i].std())
for i in range(array_diem.shape[0]):
  if(min(stdmon)==array_diem[:,i].std()):
    print("\nMôn học đồng đều nhất:",i+1,"\nBảng điểm của Môn học đồng đều:",array_diem[i,:])
    print("Môn học",i+1," có độ lệch chuẩn thấp là:",min(stdmon),"nên có độ đồng đều giữa các điểm số")



