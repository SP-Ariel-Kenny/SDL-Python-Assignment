# define fizzbuzz game
def fizzbuzz(i):
  for num in range(1,i+1):
    F = ""
    B = ""
    f = ""
    b = ""
    flip = False
    if num % 3 == 0:
      F = "Fizz"
      flip = True
    if num % 5 == 0:
      B = "Buzz"
      flip = True
    if num % 7 == 0:
      f = "Fang"
      flip = True
    if num % 11 == 0:
      b = "Bang"
      flip = True
    if flip = False:
      print(f"{num}")
    elif flip = True:
      print(f"{F}{B}{f}{b}")

fizzbuzz(100)
