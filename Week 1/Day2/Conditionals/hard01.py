# ask for a num if it's divisible by 3 then print "fizz" ifby 5 then "Buzz" if by both then "FizzBuzz"

num = int(input("enter a number "))

if num%3==0 and num%5==0:
    print("FizzBuzz")
elif num%3==0:
    print("Fizz")
elif num%5==0:
    print("Buzz")
else:
    print("not divisible by any")