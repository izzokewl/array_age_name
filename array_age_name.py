#set array
fersons = {}
#ask user to enter name and age
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
#ask user if inserting new entry
  while True:
    new_entry = input("pahgud na q, lalagay k p bah? (ril or fik): ").strip().lower()
    if new_entry == "ril":
        break 
    elif new_entry == "fik":
        print ("ay sige")
        exit()
    else:
       print("hoi baks mali, nanggigigil n qohhh")
    #store names for array
  fersons.append((name, age))


     
   
