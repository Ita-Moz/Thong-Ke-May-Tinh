from numpy.core.fromnumeric import sort
import seaborn as sns
from matplotlib.pyplot import xlabel, ylabel
import matplotlib.pyplot as plt
import numpy as np

so_lan_tung = 10000
tung_dong_xu = np.random.randint(2, size=so_lan_tung)
so_lan_0 = (tung_dong_xu ==0 ).sum()
so_lan_1 = (tung_dong_xu ==0 ).sum()
P_0 = so_lan_0/so_lan_tung
P_1 = so_lan_1/so_lan_tung
print(P_0)
print(P_1)
# --------------------------------------------------------
def tung_xu():
  if np.random.random()<0.6:
    return 0
  else:
    return 1
ket_qua = np.zeros(so_lan_tung)
for i in range(so_lan_tung):
  ket_qua[i] = (tung_xu())
P_3 = (ket_qua==0).sum()/so_lan_tung
P_4 = (ket_qua==1).sum()/so_lan_tung
print(P_3)
print(P_4)

# Hàm trọng số
gia_tri = [10,2]
diem = np.random.randint(0,11,100)
bien_ngau_nhien, tan_so = np.unique(diem, return_counts=True)
pmf = tan_so/ len(gia_tri)
# Bảng phân phối xác xuất
bang = np.column_stack((bien_ngau_nhien,pmf))
print(bang)

# Đồ thị hàm trọng số
PMF = sns.barplot(bien_ngau_nhien, sort(pmf))
PMF.set(xlabel = 'Diem', ylabel='P_X(x)')
plt.show();

# Sắp xếp đồ thị
