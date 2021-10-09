from matplotlib.pyplot  import xlabel, ylabel
import scipy
import seaborn as sns
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from scipy.stats import norm

# Bai1: Tính phân phối nhị thức
x = stats.binom(100, 0.25)
# Thỏa mãn phân phối nhị thức: 100
# xác xuất đậu ít nhất 1 trường(đúng ít nhất là 50 câu)
prA = 1-x.cdf(50)
ky_vong = x.mean()
do_lech = x.std()
print("Bài1--------------------------------------")
print('Xác xuất để đậu vào ít nhất 1 trường là: {0} \nKỳ Vọng: {1} \nĐộ lệch: {2}'.format(prA,ky_vong,do_lech))

def pmf_ngau_nhien():
  x = stats.binom(100, 0.25)
  nhi_thuc = np.arange(0,100)
  pmf = x.pmf(nhi_thuc)
  PMF = sns.barplot(nhi_thuc, pmf)
  PMF.set(xlabel = 'số lần A xảy ra',ylabel = 'P_X(x)')
  plt.show()
pmf_ngau_nhien()
def cdf_ngau_nhien():
    x = stats.binom(100, 0.25)
    nhi_thuc = np.arange(0,100)
    cdf = x.cdf(nhi_thuc)
    CDF = sns.barplot(nhi_thuc,cdf)
    CDF.set(xlabel = 'số lần xảy ra', ylabel = 'CDF_X(X)')
    plt.show()
cdf_ngau_nhien()

# Bài 2: Phân bố sigma chuẩn tắc
mu =172
sigma = 4
prB = norm.cdf((164-mu)/sigma)
prC = 1-norm.cdf((180-mu)/sigma)
prD = norm.cdf((176-mu)/sigma)-norm.cdf((168-mu)/sigma)
print('Bài2: ------------------------------------------------')
print('Xác xuất có một bạn lùn (< 164cm) là:',prB)
print('Xác xuất có một bạn cao lớn (> 180cm) là:',prC)
print('Xác xuất có một bạn trong khoảng 168cm đến 176cm là:',prD)
print('Chiều cao thấp bé (5%):',norm.ppf(0.05,mu,sigma),"cm gọi là thấp bé")
print('Chiều cao Cao lớn (7%):',norm.ppf(1-0.07,mu,sigma),"cm gọi là người cao lớn")
print("BIỂU ĐỒ PHÂN BỐ CHUẨN TRONG NGƯỠNG [-6,6,0.2]")

chuan = np.arange(-6,6,0.2)
pmf = x.pmf(chuan)
PMF = plt.plot(chuan,pmf)
plt.xlabel('x')
plt.ylabel('F_X(x)')
plt.show()

cdf = x.cdf(chuan)
CDF = plt.plot(chuan,cdf)
plt.xlabel('x')
plt.ylabel('F_X(x)')
plt.show()


