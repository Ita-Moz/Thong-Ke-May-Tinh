from numpy import tan
import pandas as pd
# Yêu cầu 2.2.1: Học viên đọc dữ liệu dạng CSV lưu trong file csv_Data_Loan.csv với các tham số mặc định
# 01.Đọc dữ liêu
path = 'US_Baby_Names.csv'
data = pd.read_csv(path)
print("01.Bảng dữ liệu sau khi đọc")
data.info()
# 02.Hiển thị 10 dòng dữ liệu bất kỳ
print("Hiển thị 10 dòng dữ liệu bất kỳ")
print(data.head(10))
# 03.Cho biết kích thước của dữ liệu
print("03.Cho biết kích thước của dữ liệu")
print(data.shape)
# 04. Xóa 2 cột 'Unnamed: 0' and 'Id'
print("04. Xóa 2 cột 'Unnamed: 0' and 'Id'")
print(data.drop(['Unnamed: 0', 'Id'], axis=1))
# 05. Cho biết số lượng bé trai, bé gái?
print("05. Cho biết số lượng bé trai, bé gái?")
data_gender = data[['Gender']]
print(data_gender.value_counts())
# 06. Trong bộ dữ liệu có bao nhiêu tên khác nhau?
print("06. Trong bộ dữ liệu có bao nhiêu tên khác nhau?")
data_name = data[['Name']]
print("Số tên khác nhau: ", data_name.value_counts().size)
# 07. Tên nào xuất hiện ít nhất?
print("07. Tên nào xuất hiện ít nhất?")
print("Tên sử dụng ít nhất:", data_name.values.min())
# 08. Top 10 tên được sử dụng nhiều nhất?
print("08. Top 10 tên được sử dụng nhiều nhất?")
print("Top 10 tên sử dụng nhiều nhất:",data_name.value_counts().head(10))
