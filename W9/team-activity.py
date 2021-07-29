numbers = []
total = 0
average = 0
largest = 0

entry = None

print("Enter a list of numbers, type 0 when finished.")

while entry != 0:
    entry = int(input("Enter number: "))
    if entry != 0:
        numbers.append(entry)

for number in numbers:
    total += number
    average = total / len(numbers)
    if (number > largest):
        largest = number

print(f"The sum is: {total}")
print(f"The average is: {average}")
print(f"The largest number is: {largest}")
