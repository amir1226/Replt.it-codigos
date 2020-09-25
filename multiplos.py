n=int(input("digite n:\n"))
m=int(input("digite m:\n"))

print("los múltiplos son:")

for i in range (n):
  if i*m > n:
    break
  print(i*m)
