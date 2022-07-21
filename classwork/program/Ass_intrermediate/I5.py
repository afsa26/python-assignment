#Write a Python program to compute the value of a specified principal amount
#rate of interest ,and a number of years

princpl_amnt = float (input ("Enter the value of Principal Amount: "))
rate_intrst = float (input("Enter the Rate of Interst: "))
time_period = float (input("Enter the number of years: "))
simple_interst=( princpl_amnt *rate_intrst*time_period)/100
#print("\nSimple interst for principle amount{0}={1}".format(princpl_amnt and rate_intrst))
print("compute The value of P,R,Y are",simple_interst)