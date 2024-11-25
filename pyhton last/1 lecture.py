# try:
#     x=int(input("Enter First Number: "))
#     y=int(input("Enter Second Number: "))
#     print(x/y)
# except ZeroDivisionError:
#     print("Can't Divide with Zero")
# except ValueError:
#     print("please provide int value only")

# try:
#     x=int(input("Enter a value: "))
#     y=int(input("enter a second value: "))
#     print(x/y)
# except ArithmeticError:
#     print("ArithmeticError")
# except ZeroDivisionError:
#     print("Zero DivisionError")

# try:
#     x=int(input("Enter First Number: "))
#     y=int(input(" Enter Second value: "))
#     print(x/y)
# except (ZeroDivisionError,ValueError) as msg:
#     print("Plz Provide valid numbers only and problem is:",msg)

# try:
#     x=int(input("Enter First Number: "))
#     y=int(input("Enter Second value: "))
#     print(x/y)
# except ZeroDivisionError:
#     print("Zero Division Error: Can't division with zero")
# except:
#     print("Defaut Except:Plz provide valid input only")

# try:
#     print("try")
# except:
#     print("except")
# finally:
#     print("finally")

# try:
#     print("try")
#     print(10/0)
# except:
#     print("except")
# finally:
#     print("finally")

# try:
#     print("try")
#     print(10/0)
# except NameError:
#     print("except")
# finally:
#     print("finally")

# try:
#     print("outer try block")
#     # print(10/0)
#     try:
#         print("Inner try block")
#         print(10/0)
#     except ZeroDivisionError:
#         print("Inner except block")
#     finally:
#         print("Inner finally block")
# except:
#     print("outer except block")
# finally:
#     print("outer finally block")

try:
    print("madhav")
    print("64")
    print("12410885")
    try:
        print("Lakhya")
        print("59")
        print("1240855")
    except NameError:
        print("Dekhle ")
    finally:
        print("bus kr ")
    print(10/0)
except ZeroDivisionError:
    print("Zero Division")
finally:
    print("finally")

