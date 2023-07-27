import os 

nump = int(input("Digite o numero que deseja consultar: "))

if nump % nump == 0 and nump % 2 != 0 and nump % 3 != 0 and nump % 5 != 0:
    print("mamaco")
else:
    print("Não é primo")

os.system("pause")