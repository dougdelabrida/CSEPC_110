print("Please enter the following information:")
print()

def start():
  first_name = input("First name: ")
  last_name = input("Last name: ")
  email = input("Email address: ")
  phone = input("Phone number: ")
  job_title = input("Job title: ")
  id_number = input("ID Number: ")

  if "" in [first_name, last_name]:
    return print("\033[93m" + "First and last can't be empty.")

  print("\nThe ID Card is")
  print("----------------------------------------")
  print(f"{last_name.upper()}, {first_name.capitalize()}")
  print(job_title or "N/A")
  print("ID: " + id_number or "N/A")
  print()
  print(email.lower() or "N/A")
  print(phone or "N/A")
  print()
  print("----------------------------------------")

start()
