import matplotlib.pyplot as plt
import numpy as np
# vd1: Vẽ đồ thị nối các điểm với giá trị các tung độ lưu trong một list, giá trị hoành độ tương ứng với các chỉ số của list. Chúng ta sử dụng hàm plot() như dưới đây
plt.style.use("ggplot")
print("vd1")
plt.plot([1, 2, 4, 7, 5, 4])
plt.show()
# vd2: Trường hợp này, sử dụng 2 list để lưu các giá trị hoành độ và tung độ của các điểm cần vẽ
print("vd2")
plt.plot([-3, -2, 0, 5], [1, 3, 2, 10])
plt.show()
# vd3:Sử dụng hàm xlim và ylim để thay đổi giá trị hiển thị đầu và cuối mỗi trục
print("vd3")
plt.plot([-3, -2, 0, 5], [1, 3, 2, 10])
plt.xlim(-5, 7)
plt.ylim(None, 12)
plt.show()
# vd4:Tương tự cách sử dụng hàm plot() như trên, ta thử vẽ đồ thị hàm y = xx bằng cách khởi tạo list x có 500 giá trị cách đều nhau có giá trị từ -2 đến 2, và list y có giá trị là y = xx. Ta vẽ đồ thị với màu xanh dương (màu sắc mặc định là màu đỏ)
print("vd4")
x = np.linspace(-2, 2, 500)
y = x**2
plt.plot(x, y, color='blue')
plt.show()
# vd5:Sử dụng các hàm title(), xlabel() và ylabel() để thêm tiêu đề cho hình vẽ và tiêu đề cho 2 trục x, y
print("vd5")
plt.plot(x, y, color='yellow')
plt.title('Hàm bình phương')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(False)    #Thử thay đổi sang giá trị False để xem kết quả
plt.show()

# THAY ĐỔI KÍCH THƯỚC ĐỒ THỊ
# vd6: vẽ đồ thị với kích thước 12*4
print("vd6")
plt.subplot(figsize = (12,4))
plt.plot(x, y, color='red')
plt.title('Hàm bình phương')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)    #Thử thay đổi sang giá trị False để xem kết quả
plt.show()

#   ĐỊNH DẠNG ĐƯỜNG THẲNG VÀ MÀU SẮC
# vd7: thay đổi màu sắc và dạng đường vẽ
print("vd7")
plt.plot(x, y, 'b--')
plt.title('Hàm bình phương')
plt.xlabel('x')
plt.ylabel('y = x**2')
plt.show()
# vd8: Thay đổi độ rộng, độ trong suốt hay định dạng đường nối
print("vd8")
x = np.linspace(-1.4,1.4,30)
plt.plot(x,x,'g--')
plt.plot(x, x**2, 'r:')
plt.plot(x, x**3, 'b^')
plt.show()

# VẼ ĐỒ THỊ CON
# vd9:đồ thị con
print("vd9:")
x = np.linspace(-1.4,1.4,30)
plt.subplot(2,2,1)
plt.plot(x,x) # ma trận đồ thị con 2 dòng, 2 cột, đồ thị thứ nhất trái trên

plt.subplot(2, 2, 2)
plt.plot(x, x**2)      # ma trận đồ thị con 2 dòng, 2 cột, đồ thị thứ hai phải trên

plt.subplot(2, 2, 3)   # ma trận đồ thị con 2 dòng, 2 cột, đồ thị thứ ba trái dưới
plt.plot(x, x**3)

plt.subplot(2, 2, 4)
plt.plot(x, x**4)      # ma trận đồ thị con 2 dòng, 2 cột, đồ thị thứ tư phải dưới

plt.show()

# vd10: mở rộng kích thước của đồ thị
print("vd10: mở rộng kích thước của đồ thị ")
plt.subplot(2, 2, 1)  # 2 rows, 2 columns, 1st subplot = top left
plt.plot(x, x)

plt.subplot(2, 2, 2)  # 2 rows, 2 columns, 2nd subplot = top right
plt.plot(x, x**2)

plt.subplot(2, 1, 2)  # 2 rows, *1* column, 2nd subplot = bottom
plt.plot(x, x**3)
plt.show()
# vd11: THÊM CHỮ VÀ CHÚ THÍCH
print("vd11: thêm chữ và chú thích")
x = np.linspace(-1.5, 1.5, 30)
px = 0.8
py = px**2

plt.plot(x, x**2, "b-", px, py, "ro")

plt.text(0, 1.5, "Hàm số \n$y = x^2$", fontsize=15, color='blue', horizontalalignment="center")
plt.text(px, py, "x = %0.2f\ny = %0.2f"%(px, py), rotation=10, color='gray')

plt.show()

# vd12: NHÃN VÀ GHI CHÚ
print("vd12: NHÃN VÀ GHI CHÚ")
x = np.linspace(-1.4, 1.4, 50)

plt.plot(x, x**2, "r--", label="Square function")
plt.plot(x, x**3, "b-", label="Cube function")

plt.legend(loc="lower right")
plt.show()

# ĐỒ THỊ ĐƯỜNG THẲNG
print("ĐỒ THỊ ĐƯỜNG THẲNG")
def plot_line(axis, slope, intercept, **kargs):
    xmin, xmax = axis.get_xlim()
    plt.plot([xmin, xmax], [xmin*slope+intercept, xmax*slope+intercept], **kargs)

x = np.random.randn(1000)
y = 0.5*x + 5 + np.random.randn(1000)

plt.axis([-2.5, 2.5, -5, 15])
plt.scatter(x, y, alpha=0.2)
plt.plot(1, 0, "ro", color='black')

plt.vlines(1, -5, 0, color="green", linewidth=0.75)
plt.hlines(0, -2.5, 1, color="green", linewidth=0.75)
plot_line(axis=plt.gca(), slope=0.5, intercept=5, color="blue")

plt.grid(True)
plt.show()

# HISTOGRAMS
print("HISTOGRAMS")
data = [1, 1.1, 1.8, 2, 2.1, 3.2, 3, 3, 3, 3]
plt.subplot(2,1,1)
plt.hist(data, bins = 10, rwidth=0.8)

plt.subplot(2,1,2)
plt.hist(data, bins = [1, 1.5, 2, 2.5, 3], rwidth=0.8)

plt.xlabel("Value")
plt.ylabel("Frequency")

plt.show()

# SCATTER PLOTS
print("SCATTER PLOTS(đồ thị phân tán)")
x, y = np.random.rand(2, 10)
plt.scatter(x, y)
plt.show()

# Thay đổi kích thước bằng tham số s
print("Thay đổi kích thước bằng tham số s")
scale = np.random.rand(10)
scale = 500 * scale ** 2
plt.scatter(x, y, s=scale)
plt.show()
# Thay đổi màu sắc
for color in ['red', 'green', 'blue']:
    n = 10
    x, y = np.random.rand(2, n)
    scale = 500.0 * np.random.rand(n) ** 2
    plt.scatter(x, y, s=scale, c=color, alpha=0.3)

plt.show()
# BOXPLOTS
print("BOXPLOTS")
data1 = np.random.rand(10)*2 + 5
plt.boxplot(x=data1)
plt.title("Boxplot")
plt.show()
