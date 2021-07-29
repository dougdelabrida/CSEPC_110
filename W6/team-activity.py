first_rider_age = int(input("What is the age of the first rider? "))
first_rider_height = float(input("What is the height of the first rider? "))
is_there_second_rider = input("Is there a second rider (yes/no)? ") == "yes"

if (first_rider_age < 18 or first_rider_height < 62) and is_there_second_rider == False:
  print("Sorry, you may not ride.")
else:
  if is_there_second_rider:
    second_rider_age = int(input("What is the age of the second rider? "))
    second_rider_height = float(input("What is the height of the second rider? "))

    if first_rider_age >= 12 and first_rider_age <= 17 or second_rider_age >= 12 and second_rider_age <= 17:
      golden_passport = input("Do you have a golden passport (yes/no)? ") == "yes"
      if (golden_passport):
        first_rider_age = 18
        second_rider_age = 18

    if (first_rider_age >= 18 and first_rider_height) >= 62 or (second_rider_age >= 18 and second_rider_height >= 62):
      print("Welcome to the ride. Please be safe and have fun!")
    else:
      if (first_rider_age == 12 and first_rider_height == 52 and first_rider_age == second_rider_age and first_rider_height == second_rider_height):
        print("Welcome to the ride. Please be safe and have fun!")
      else:
        print("Sorry, you may not ride.")
  else:
    if (first_rider_age >= 18 and first_rider_height >= 62):
      print("Welcome to the ride. Please be safe and have fun!")
    else:
      print("Sorry, you may not ride.")
