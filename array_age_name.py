#ask user to input their name and age
def hasNumbers(inputString):
  return any(char.isdigit() for char in inputString)
while True:
  name = input("pangalan mo baks: ")
  if hasNumbers(name):
    print ("baks omayus ka, ulet!")
