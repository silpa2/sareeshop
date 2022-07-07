weight=float(input("weight: "))
unit=input("(K)g or (L)bs :")
if unit.upper()== 'K':
    weightnew=float(weight/.45)
    print("weight in Lbs:"+str(weightnew))
else:
    weightnew=float(weight*.45)
    print("weight in Kg :"+str(weightnew))

