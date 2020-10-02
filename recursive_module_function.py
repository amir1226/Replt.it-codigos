def recursive_module(n,m):
  if n<m:
    return n
  return(recursive_module((n-m),m))

def module (x,y):
  if y>x:
    return recursive_module(y,x)
  return recursive_module(x,y)

val_1=int(input("Enter first number: "))
val_2=int(input("Enter second number: "))

result=module (val_1,val_2)
print(result)
