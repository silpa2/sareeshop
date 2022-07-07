
r=float(input("Enter the rate of interest :: "))
p=float(input("Enter the amount :: "))
n=float(input("Enter the duration in years :: "))
interest=p*n*r/100
print(interest)
print("The simple  interest for the amount Rs."+str(p)," at rate of interest "+str(r)," % for the time period of "+str(n)," years is Rs."+str(interest))


