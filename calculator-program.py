num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
def sum_sub_mul_divide(x,y):
      a=x+y
      b=x-y
      c=x*y
      d=x/y
      return a,b,c,d


g,h,i,t=sum_sub_mul_divide(num1,num2)
print(g)
print(h)
print(i)
print(t)
