#ask user to input their name and age
def numbers(string):
  return any(char.isdigit() for char in string)
while True:
  name = input("pangalan mo baks: ")
  if numbers(name):
    print ("baks omayus ka, ulet!")
  else:
      while True:
        try:
            age = int(input("edad mo baks: "))
            if age>0:
               break
        except ValueError:
            print ("hoi omayus k sabeh")
            if break:
               print ("maglagay k pa bah, pahgud n q")
