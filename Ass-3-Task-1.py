# Task 1: Calculate Factorial Using a Function

def fact(n):
    if n < 2 :
        return 1
    else:
        return n * (fact(n-1))

a = int(input("Enter a Number : "))
ans = fact(a)
ans = int(ans)
print("Factorial of",a ,"is",ans)

#print(f"Factorial of {a} is {ans}")
#print("Factorial of {} is {}".format(a, ans))
