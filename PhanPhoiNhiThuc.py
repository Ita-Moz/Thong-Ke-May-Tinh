from matplotlib.pyplot  import xlabel, ylabel
import scipy
import seaborn as sns
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from scipy.stats import norm

# Bai1: Tính phân phối nhị thức
x = stats.binom(120, 0.25)
# xác định số câu trên 65
prA = 1-x.cdf(65)
ky_vong = x.mean()
do_lech = x.std()
print('Xác xuất: {0} Kỳ Vong: {1} Độ lệch: {2}'.format(prA,ky_vong,do_lech))

def pmf_ngau_nhien():
  nhi_thuc = np.arange(0,121)
  pmf = x.pmf(nhi_thuc)
  PMF = sns.barplot(nhi_thuc, pmf)
  PMF.set(xlabel = 'số lần A xảy ra',ylabel = 'P_X(x)')
  plt.show()
pmf_ngau_nhien()

def cdf_ngau_nhien():
    x = stats.binom(120, 0.25)
    nhi_thuc = np.arange(0,121)
    cdf = x.cdf(nhi_thuc)
    CDF = sns.barplot(nhi_thuc,cdf)
    CDF.set(xlabel = 'số lần xảy ra', ylabel = 'CDF_X(X)')
    plt.show()
cdf_ngau_nhien()

# Bài 2: Phân bố sigma chuẩn tắc
def mo_ta_chuan_tac():
  # Quy tắc 1 sigma
  sigma1 = 2*norm.cdf(1)-1
  # Quy tắc 2 sigma
  sigma2 = 2*norm.cdf(2)-1
  # Quy tắc 3 sigma
  sigma3 = 2*norm.cdf(3)-1
  # Phân vị mức 0.9
  phan_vi9 = norm.ppf(0.9)
  # Phân vị mức 0.95
  phan_vi95 = norm.ppf(0.95)
  # Phân vị mức 0.99
  phan_vi99 = norm.ppf(0.99)
  print('Phân bố chuẩn tắc----------------------------------')
  print('sigma1: {0}\nsigma2: {1}\nsigma3: {2}\nphanvi9: {3}\nphân vị95: {4} \nphân vị 99: {5}'.format(sigma1,sigma2,sigma3,phan_vi9,phan_vi95,phan_vi99))
mo_ta_chuan_tac()

# Bài3:
mu =165
sigma = 2.5
prB = norm.cdf((158-mu)/sigma)
prC = 1-norm.cdf((172-mu)/sigma)
prD = norm.cdf((172-mu)/sigma)-norm.cdf((166-mu)/sigma)
print('Bài3: Bài tập tính xác xuất--------------------------------')
print('Xác xuất có một bạn < 158cm là:',prB)
print('Xác xuất có một bạn > 172cm là:',prC)
print('Xác xuất có một bạn trong khoảng 166cm đến 172cm là:',prD)
print('Chiều cao thấp bé (5%)',norm.ppf(0.05,mu,sigma))
print('Chiều cao Cao lớn (7%)',norm.ppf(1-0.07,mu,sigma))



