from scipy.stats import kurtosis
from scipy.stats import skew
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statistics as sta
data = pd.read_csv('babies.txt',sep = '\s+')
# Loc du lieu
databwt = data['bwt']
datasm  = data['smoke']
hutthuoc = data[data['smoke']==1]
khongthuoc = data[data['smoke']==0]
dt_hutthuoc  = hutthuoc['bwt']
dt_khongthuoc = khongthuoc['bwt']
# data.boxplot(by = 'smoke',column=['bwt'])
print("Cac gia tri thong ke nguoi CO hut thuoc")
print(dt_hutthuoc.describe())
print("Phanvi 25%:" ,np.quantile(dt_hutthuoc,.25))
print("Phanvi 50%:" ,np.quantile(dt_hutthuoc,.50))
print("Phanvi 75%:" ,np.quantile(dt_hutthuoc,.75))
# c2
print("Phanvi 75%:" ,np.percentile(dt_hutthuoc,75))
#
print("Range:", np.ptp(dt_hutthuoc))
print("Median:",dt_hutthuoc.median())
print("Mean:",dt_hutthuoc.mean())
print("Min:",dt_hutthuoc.min())
print("Max:",dt_hutthuoc.max())
print("Phuong sai Var:", dt_hutthuoc.var())
print("IQR:75 - 25 :",np.quantile(dt_hutthuoc,.75)-np.quantile(dt_hutthuoc,.25))
print('Kurtosis có hút thuoc:',kurtosis(dt_hutthuoc))
print('Skew có hút thuoc:',skew(dt_hutthuoc))
print("Yeu vi mode",sta.mode(dt_hutthuoc))


# ----------------
print("Cac gia tri thong ke nguoi KHONG hut thuoc")
print(dt_khongthuoc.describe())
print("Phanvi 25%:" ,np.quantile(dt_khongthuoc,.25))
print("Phanvi 50%:" ,np.quantile(dt_khongthuoc,.50))
print("Phanvi 75%:" ,np.quantile(dt_khongthuoc,.75))
print("Range:", np.ptp(dt_khongthuoc))
print("Median:",dt_khongthuoc.median())
print("Mean:",dt_khongthuoc.mean())
print("Min:",dt_khongthuoc.min())
print("Max:",dt_khongthuoc.max())
print("Phuong sai Var:", dt_khongthuoc.var())
print("IQR:75 - 25 :",np.quantile(dt_khongthuoc,.75)-np.quantile(dt_khongthuoc,.25))
print('Kurtosis có hút thuoc:',kurtosis(dt_khongthuoc))
print('Skew có hút thuoc:',skew(dt_khongthuoc))
print("Yeu vi mode",sta.mode(dt_khongthuoc))

# -------------
plt.boxplot([dt_khongthuoc,dt_hutthuoc],labels=['khong thuoc','co hut thuoc'])
plt.title("Boxplot")
plt.show()
# plt.subplot(2,1,1)
# plt.boxplot(dt_khongthuoc)
# plt.subplot(2,1,2)
# plt.boxplot(dt_hutthuoc)
# plt.show()
# ---------Hinstgram
plt.subplot(1,2,1)
plt.title("Ba Me Hut Thuoc")
plt.hist(dt_hutthuoc, bins = 12)
plt.subplot(1,2,2)
plt.title("Ba Me Khong Hut Thuoc")
plt.hist(dt_khongthuoc, bins = 12)
plt.show()

