# def s(num):
    
#     result=1
#     while num>=1:
#         result=result*num
#         num-=1
#     return result
# for i in range(1,20):
#     print("hello",i,"is:",s(i))



# sum=0
# def num(n):
#     global sum
#     for i in range(1,n):
#         sum+=i
#     return sum

# print(num(10))

# product=1
# def num(n):
#     global product
#     for i in range(1,n+1):
#         product*=i
#     return product
# print(num(5))


# star=1
# def st(n):
#     global star
#     for i in range(1,n+1):
#         star/=i
#     return star
# print(st(5))

     #### factorial of a number
# def fact(n):
#     if n==0:
#         return 1
#     else:
#         result=n*fact(n-1)
#     return result
# print(fact(3))

# import math
# def fun(n):
#     return math.factorial(n)
# print(fun(5))



# l=[1,2,4]
# def f(n):
#     return n*2
# l1=list(map(f,l))
# print(l1)

# l=[1,2,3]
# a=list(map(lambda x:x*2,l))
# print(a)


# list=[]
# for i in range(51):
#     if i%10==0:
#         list.append(i)
# list.append("ram")
# print(list)

# ## syntax
# class student:
#      '''this class represent student '''
# # variables:isinstance variables
# # methods:isinstance methods
# print(student.__doc__)
# help(student)



# class Student:
#      '''this class is developed by u'''
#      def __init__(self):
#          self.name="durga"
#          self.age=40
#          self.marks=80

#      def talk(self):
#           print("Hello I am : ",self.name)
#           print("My Age is: ",self.age)
#           print("My marks are: ",self.marks)


# class Student:
#      # '''this class is developed by u'''
#      def __init__(self,name,rollno,marks):
#          self.name=name
#          self.rollno=rollno
#          self.marks=marks

#      def talk(self):
#           print("Hello I am : ",self.name)
#           print("My Rollno is: ",self.rollno)
#           print("My marks are: ",self.marks)
# s1=Student("Durga",101,80)
# s1.talk()


# class Book:
#      def __init__(self,title,author):
#         self.name=title
#         self.book=author
#      def talk(self):
#          print("BOOK NAME: ",self.name)
#          print("The author of book: ",self.book)
     
# a=Book("MATHS","R.S AGARWAL")
# a.talk()



# class Employee:
#      def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#      def talk(self):
#          print("NAME: ",self.name)
#          print("The Salary of Employee: ",self.salary)
     
# a=Book("Ram",25000)
# a.talk()


# class Circle:
#      def __init__(self,radius):
#         self.radius=radius
        
#      def talk(self):
#          print("Radius: ",self.radius)
#          print("The Area of Circle: ",3.14*self.radius**2)
#          print("The circumference of a circle: ",2*3.14*self.radius)
     
# b=Circle(5)
# b.talk()

# class Employee:
#      def __init__(self,name,subject,salary):
#         self.name=name
#         self.subject=subject
#         self.salary=salary
        
#      def talk(self):
#          print("Name: ",self.name)
#          print("Emp_1.name: ",self.subject)
#          print("Emp_1.Salary: ",self.salary)
# d=input("Enter : ")
# f=int(input("Enter a value: "))
# g=input("Subjects")
# c=Employee(d,g,f)
# c.talk()



class P:
   def Myname(self):
      print("devansh")
class C(P):
   def Myname(self):
      print("Devansh/agarwal")
c=C()
print(c)
c.Myname()


class P:
   def Myname(self):
      print("devansh")
class C(P):
   pass
c=C()
print(c)
c.Myname()


