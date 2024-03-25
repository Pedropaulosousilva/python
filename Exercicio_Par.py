import time
numero1=float(input("Digite o numero:"))

n2= numero1 % 2

if n2 == 0 :
  print('"P-A-R!!!"')

else :
  print("Tente outra vez")
time.sleep(4)