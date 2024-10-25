#ask user to input their name and age
def numbers(string):
  return any(char.isdigit() for char in string)
while True:
  name = input("pangalan mo baks: ")
  if numbers(name):
    print ("baks omayus ka, ulet!")
  else:
    age = int(input("edad mo baks: "))