#Q1
def is_odd(number):
     if(number % 2 == 0):
          return True
     else:
          return False


#Q2
def avg_numbers(*args):
     result = 0
     for i in args:
          result += i
     return result
     
#Q3 int()취한다.

#Q4

#답: 3

#Q5
f1 = open("test.txt",'w')
f1.write("Life is too short")

f1 = open("test.txt",'r')
print(f1.read())


#Q6

user_input = input("저장할 내용을 입력하세요 : ")
f = open('test.txt','a')
f.write(user_input)
f.close


#Q7
open('test.txt','w')
f.write("Life is too short")

f = open('test.txt','r')
body = f.read()
f.close()

body.replace('Life','python')

f = open('test.txt','w')
f.write(body)
f.close

print(f.read())





print(avg_numbers(1, 2))

num = 3

print("num is ",is_odd(num))
