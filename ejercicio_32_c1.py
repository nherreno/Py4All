#same that 31 but with the option of erase or print something different if there are errors#

try:
    hrs = input("Enter Hours:")
    rate=input("rate:")
except:
    print("error,please enter numeric input")
    quit()
rate=float(rate)
h = float(hrs)
b=0

if h>40:
    b=h-40
    pay=(rate*h)+(b*0.5*rate)
else:
    pay=rate*h

print(pay)