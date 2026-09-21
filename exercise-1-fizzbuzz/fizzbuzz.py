# define fizzbuzz game
def fizzbuzz(range):
  for num in range:
    if num % 3 == 0:
      if num % 5 == 0:
        print("FizzBuzz")
      else:
        print("Fizz")
    elif num % 5 == 0:
      print("Buzz")
    else:
      print(f"{num}")

fizzbuzz(100)
