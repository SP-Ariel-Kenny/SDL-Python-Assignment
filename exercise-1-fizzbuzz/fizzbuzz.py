# define fizzbuzz game
def fizzbuzz(i):
  for num in range(1,i+1):
    if num % 3 == 0:
      if num % 5 == 0:
        if (num % 7 == 0) and (num % 11 == 0):
          print("FizzBuzzFangBang")
        elif num % 7 == 0:
          print("FizzBuzzFang")
        elif num % 11 == 0:
          print("FizzBuzzFang")
        else:
          print("FuzzBuzz")
      else:
        print("Fizz")
    elif num % 5 == 0:
      if (num % 7 == 0) and (num % 11 == 0):
        print("BuzzFangBang")
      elif num % 7 == 0:
        print("BuzzFang")
      elif num % 11 == 0:
        print ("BuzzFangBang")
      else:
        print("Buzz")
    else:
      print(f"{num}")

fizzbuzz(100)
