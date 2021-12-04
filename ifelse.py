x=int(input("enter the number"))
if x%5==0:
      if x%11==0:
            print("divisible by 5 and 11")
      else:
            print("divisible by 5")
# elif x%5==0:
#       print("divisible by 5")
elif x%11==0:
      print("divisible by 11")
else:
      print("non of the correct answer")