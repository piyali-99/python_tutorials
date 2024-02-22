print("hello")
counter = 100          # Creates an integer variable
miles   = 1000.0       # Creates a floating point variable
name    = "Zara Ali"   # Creates a string variable

print (counter)
print (miles)
print (name)
print(type(counter))

width=10
height=20
area=width*height
print(area)
perimeter=2*(width+height)
print(perimeter)


str = 'Hello World!'

print (str)          
print (str[0])       
print (str[2:5])    
print (str[2:])      
print (str * 2)      
print (str + "TEST") 

list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print (list)            
print (list[0])        
print (list[1:3])      
print (list[2:])       
print (tinylist * 2)    
print (list + tinylist)


#dict
dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}

print (dict['one'])       
print (dict[2])           
print (tinydict)          
print (tinydict.keys())   
print (tinydict.values())

#bool
a = 2
b = 4
print(bool(a==b))

#type_casting
a=True;
b=10.5;
c=a+b;

print (c);


a = int("100")


type(a)

a = ("10"+"01")
a = int("10"+"01")
print(a)
print(type(a))

# a=[1,2,3,4,5]
# c="Hello"  #sting object 
# a=list(c)
# print(a)

a=10+5j
b=20.5
print ("subtraction of complex and float")
print ("a=",a,"b=",b,"a-b=",a-b)
print ("a=",a,"b=",b,"b-a=",b-a)

#modulas
a=10
b=2
print ("a=",a, "b=",b, "a%b=", a%b)

#relational operators

a=5
b=7
print ("a=",a, "b=",b, "a>b is", a>b)
print ("a=",a, "b=",b,"a<b is",a<b)
print ("a=",a, "b=",b,"a==b is",a==b)
print ("a=",a, "b=",b,"a!=b is",a!=b)


print ("comparison of int and float")
a=10
b=10.0
print ("a=",a, "b=",b, "a>b is", a>b)
print ("a=",a, "b=",b,"a<b is",a<b)
print ("a=",a, "b=",b,"a==b is",a==b)
print ("a=",a, "b=",b,"a!=b is",a!=b)

print ("comparison of Booleans")
a=True
b=False
print ("a=",a, "b=",b,"a<b is",a<b)
print ("a=",a, "b=",b,"a>b is",a>b)
print ("a=",a, "b=",b,"a==b is",a==b)
print ("a=",a, "b=",b,"a!=b is",a!=b)

#Python − Augmented Addition Operator (+=)


a=10
b=5
print ("Augmented addition of int and int")
a+=b
print ("a=",a, "type(a):", type(a))

#Logical Operators

x = 10
y = 20
print("x > 0 and x < 10:",x > 0 and x < 10)
print("x > 0 and y > 10:",x > 0 and y > 10)
print("x > 10 or y > 10:",x > 10 or y > 10)
print("x%2 == 0 and y%2 == 0:",x%2 == 0 and y%2 == 0)
print ("not (x+y>15):", not (x+y)>15)
print (" (x+y>15):", (x+y)>15)

#Membership Operators
var = "TutorialsPoint"
a = "P"
b = "tor"
c = "in"
d = "To"
print (a, "in", var, ":", a in var)
print (b, "not in", var, ":", b not in var)
print (c, "in", var, ":", c in var)
print (d, "not in", var, ":", d not in var)


var = [10,20,30,40]
a = 20
b = 10
c = a-b
d = a/2
print (a, "in", var, ":", a in var)
print (b, "not in", var, ":", b not in var)
print (c, "in", var, ":", c in var)
print (d, "not in", var, ":", d not in var)


#identity
a=[1,2,3]
b=[1,2,3]
print ("id(a), id(b):", id(a), id(b))
print ("a is b:", a is b)
print ("b is not a:", b is not a)
#####
a = 20
b = 10
c = 15
d = 5
e = 0

e = (a + b) * c / d       #( 30 * 15 ) / 5
print ("Value of (a + b) * c / d is ",  e)

# name = input()
# city = input()

# print ("Hello My name is", name)
# print ("I am from ", city)


#bool forms
a = True
print(bool(a))


#if

marks = 80 
result = ""
if marks < 30:
   result = "Failed"
elif marks > 75:
   result = "Passed with distinction"
else:
   result = "Passed"

print(result)

#################
age=25
print ("age: ", age)
if age >=18:
   print ("eligible to vote")
else:
   print ("not eligible to vote")


#match case
def checkVowel(n):
   match n:
      case 'a': return "Vowel alphabet"
      case 'e': return "Vowel alphabet"
      case 'i': return "Vowel alphabet"
      case 'o': return "Vowel alphabet"
      case 'u': return "Vowel alphabet"
      case _: return "Simple alphabet"
print (checkVowel('a'))
print (checkVowel('m'))
print (checkVowel('o'))


#for loop
words = ["one", "two", "three"]
for x in words:
  print(x)

#while loop
  i = 1
while i < 6:
  print(i)
  i += 1
###########################
def access(user):
   match user:
      case "admin" | "manager": return "Full access"
      case "Guest": return "Limited access"
      case _: return "No access"
print (access("manager"))
print (access("Guest"))
print (access("Ravi"))


zen = '''
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
'''
for char in zen:
   if char not in 'aeiou':
      print (char, end='')


numbers = (34,54,67,21,78,97,45,44,80,19)
total = 0
for num in numbers:
   total+=num
print ("Total =", total)



#for range
for num in range(5):
 print (num, end=' ')
print()
for num in range(10,20):
 print (num, end=' ')
print()
for num in range(1, 10, 2):
 print (num, end=' ')


#factorial no
 fact=1
N = 5
for x in range(1, N+1):
   fact=fact*x
print ("factorial of {} is {}".format(N, fact))


numbers = [34,54,67,21,78]
indices = range(len(numbers))
for index in indices:
   print ("index:",index, "number:",numbers[index])
print()
          
 #break  
for letter in 'Python':     
   if letter == 'h':
      break
   print ('Current Letter :', letter)
  
var = 10                   
while var > 0:              
   print ('Current variable value :', var)
   var = var -1
   if var == 5:
      break

print ("Good bye!")


#continue

for letter in 'Python': 
   if letter == 'h':
      continue
   print ('Current Letter :', letter)
var = 10 
while var > 0:
   var = var -1
   if var == 5:
      continue
   print ('Current variable value :', var)
print ("Good bye!")


#nested loops
months = ["jan", "feb", "mar"]
days = ["sun", "mon", "tue"]


for x in months:
  for y in days:
    print(x, y)

print ("Good bye!")





#parameter and arguments

# Here a,b are the parameters 
def sum(a,b): 
  print(a+b) 
	
sum(1,2)

def sum(a,b): 
  print(a+b) 
	
# Here the values 1,2 are arguments 
sum(1,2) 

#string slicing
var="HELLO PYTHON"

print ("var:",var)
print ("var[:6][:2]:", var[:6][:2])

var1=var[:6]
print ("slice:", var1)
print ("var1[:2]:", var1[:2])


a=[1,2,3,4,5,6]
for x in a:
   a[-1]=x
   print(a)
   print (a[-1])