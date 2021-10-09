import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#  Chiều cao của phụ nữ: biểu diễn chiều cao của phụ nữ từ Dataset 1
data = pd.read_excel('01_MHEALTH1.xls')
print(data)
datah = data['HT']
plt.hist(datah,bins = 15, rwidth=0.5)
plt.title("Biểu đồ chiều cao của phụ nữ")
plt.xlabel("Height")
plt.ylabel("Frequency")
plt.show()

dt = pd.read_excel('04_CIGARET.xls')
dtx = dt['KgTar']
dty = dt['MnCO']
plt.scatter(dtx,dty)
plt.title("Biểu đồ Nhựa/CO trong thuốc lá")
plt.xlabel('KgTar')
plt.ylabel('MnCo')
plt.show()
