'''
DATE:31TH DEC 2022
DAY: SATURDAY
TOPIC: ERROR_HANDLING
AUTHOR:RAMA BHARGAvi
'''
print("python")
print("core python")
a=5
b='6'
try:
    print(a/5)
    print(a/0)
except ZeroDivisionError:
    print('not ok divided by zero')
else:
    print("its ok divided by zero")
print("advance python")
print("python analytics")
print("python")
print("core python")
a=5
b='6'
try:
    print(a/5)
    print(a/0)
except ZeroDivisionError:
    print('not ok divided by zero')
finally:
    print("its ok next time don't divide by zero")
print("advance python")
print("python analytics")
n=int(input('enter any value:'))
if n<17:
    assert print("you are not aligible to vote")
n=int(input('enter the value more then then 40:'))
if (n>40):
    raise Exception('your elibible')