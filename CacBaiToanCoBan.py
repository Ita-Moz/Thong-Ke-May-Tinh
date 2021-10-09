# MSSV: 19496051
# Tên: Lương Văn Mạnh
#1. Hello world!------------------------------------------------------
import cmath
import random
def bai1():
  print('Hello, world!')
  print('Hello', end = ' ')
  print('world', end = '!')

  print('Hello', 'Word', sep = ' ')

# 2. Program to Add Two Numbers----------------------------------------
# Add Two Numbers
def bai2():
  num1 = 1.5
  num2 = 6.3
  sum = num1 + num2
  print('Tong: {0}'.format(sum))

  # Add Two Numbers With User Input
  num1 = float(input('Enter first number: '))
  num2 = float(input('Enter second number: '))
  sum = num1+num2
  print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))


# 3. Program to Find the Square Root------------------------------------------
def bai3():
  num = 8
  num_sqrt = num ** 0.5
  print('The square root of %0.3f is %0.3f'%(num ,num_sqrt))
  # -------------------------
  num = 1+2j
  num_sqrt = cmath.sqrt(num)
  print('The square root of {0} is {1:0.3f}+{2:0.3f}j'.format(num ,num_sqrt.real,num_sqrt.imag))

# 4. Program to Calculate the Area of a Triangle-----------------------------------------
### START CODE HERE ###
def bai4():
  a = float(input('Vui long nhap vao so a:'))
  b = float(input('Vui long nhap vao so b:'))
  c = float(input('Vui long nhap vao so c:'))
  s = (a+b+c)/2
  area = cmath.sqrt(s*(s-a)*(s-b)*(s-c))
  print('The area of the triangle is {0}'.format(area))

# 5. Program to Solve Quadratic Equation-------------------------------
def bai5():
  a = int(input('Vui long nhap vao so a:'))
  b = int(input('Vui long nhap vao so b:'))
  c = int(input('Vui long nhap vao so c:'))

  if a == 0:
      if b == 0:
          if c == 0:
              print("Phương trình vô số nghiệm!")
          else:
              print("Phương trình vô nghiệm!")
      else:
          if c == 0:
              print("Phương trình có 1 nghiệm x = 0")
          else:
              print("Phương trình có 1 nghiệm x = ", -c / b)
  else:
        d = d = (b**2) - (4*a*c)
        if d < 0:
          print("Phương trình vô nghiệm!")
        elif d == 0:
          print("Phương trình có 1 nghiệm x = ", -b / (2 * a))
        else:
          print("Phương trình có 2 nghiệm phân biệt")
          sol1 = (-b-cmath.sqrt(d))/(2*a)
          sol2 = (-b+cmath.sqrt(d))/(2*a)
          print('The solution are {0} and {1}'.format(sol1,sol2))
# 6. Program to Swap Two Variables-----------------------------------
def bai6():
  x = input('Enter value of x: ')
  y = input('Enter value of y: ')
  temp = x
  x = y
  y = temp
  print('The value of x after swapping: {0} có id:{1}'.format(x, id(x)))
  print('The value of y after swapping: {0} có id:{1}'.format(y,id(y)))

# 7. Program to Generate a Random Number-----------------------------
def bai7():
  print(random.randint(0,9))
  print(random.randrange(9))
  print(random.randrange(3,9))
  print(random.random())
  # print(random.uniform(a,b))

# 8. Program to Convert Kilometers to Miles----------------------------
def bai8():
  kilometers = float(input("Enter value in kilometers: "))
  conv_fac = 0.621371
  miles = kilometers * conv_fac
  print('%0.2f kilometers is equal to %0.2f miles' %(kilometers,miles))

# 9. Program to Convert Celsius To Fahrenheit----------------------------
def bai9():
  doC = float(input("Enter value in do C: "))
  doF = (doC * 1.8) + 32
  print('Độ C: %0.1f Độ F:  %0.1f '%(doC,doF))

