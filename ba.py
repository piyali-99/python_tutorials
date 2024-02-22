# class person:
#     def __init__(self,piyali) :
#          print("hy")
 

# a=person("")
# a=person("652562")
# a=person(0,651)
# n=int(input("enter a value:"))
# if (n%2)!=0:
#     print("Weird")
# elif (n%2)==0 and 2<=n>=5 :
#     print("Not Weird")
# elif (n%2)==0 and 6<=n>=20:
#     print("Weird")
# elif (n%2)==0 and n<20:
#     print("Not Weird")
# # else:
#     # print("Not Weird") 


# n = int(input())
# a=[]
# for i in range(1,n):
#     r=int(input())
#     a.append(r)
# print (a[r])

a=[1,5,9,15,23,27.31,33,39]
y=list(filter(lambda x: x%3==0,a))
print(y)


  #out of range program  
num = [1]
# print(num[2])
#print(len(num))
if len(num)>=3:
    print(num[2])
else:
    print("jyhg")

# a=[]
# b=int(input())
# for i in range(0,b):
#     av=[input()]
#     a.append(av)
# print(a)
  
# def my(lst):
#     length = n
#     for element in lst:
#         for _ in range(length):
#             list=[input()]
#             my_list.append(list)
#         print(element)
# my_list = []
# n=int(input())
# my(my_list)


class A():
    def eat(self):
        print("hi")
class B(A):
    def eat1(self):
        print("hello")
class C(A):
    def eat2(self):
        print("any")
class D(B,C):
    def eat3(self):
        print("how")

obj=D();
obj.eat();
# obj.eat1();
# obj.eat2();
# obj.eat3();
