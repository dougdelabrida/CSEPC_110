with open('./hr_system.txt') as employees:
    for line in employees:
        name, id_number, job_title, salary = line.strip().split(" ")
        print(f"Name: {name}, Title: {job_title}")
