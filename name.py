import sys

# Define a main() function that prints a little greeting.
def main():
  # Get the name from the command line, using 'World' as a fallback.
  if len(sys.argv) >= 2:
    name1 = str(sys.argv[1:])
    name = name1[2:-2]
  else:
    name = 'World'
  for letter in name :
    print ("     ",letter)
  print  ("Hello!  And Matt is a cheab.")
  print (("Say my name, " * 3) + "yeah.")
  Fav = input("Enter your favorite food: ")
  print (Fav + " is your favorite food.  \n You love " + Fav + " so much, it makes you wanna die. It's " + Fav + "alicous!")
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()

mad = "Super Cheab"
Mad2 = mad[:5]
print (Mad2)

