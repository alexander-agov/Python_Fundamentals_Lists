n = int(input())

numbers = []

for _ in range(n):
    number = int(input())
    numbers.append((number))

command = input()

filtered_numbers = []

if command == "even":
    for num in numbers:
        if num % 2 ==0:
            filtered_numbers.append(num)

elif command == "odd":
    for num in numbers:
        if num % 2 !=0:
            filtered_numbers.append(num)

elif command == "negative":
    for num in numbers:
        if num < 0:
            filtered_numbers.append(num)

elif command == "positive":
    for num in numbers:
        if num >= 0:
            filtered_numbers.append(num)

print(filtered_numbers)


# n = int(input())
# command_even = "even"
# command_odd = "odd"
# command_negative = "negative"
# command_positive = "positive"
#
# numbers = [int(input()) for _ in range(n)]
#
# filtered_numbers = []
#
# command = input()
# for num in numbers:
#     filtered_command = (
#         (command == command_even and num % 2 == 0) or
#         (command == command_odd and num % 2 != 0) or
#         (command == command_positive and num >= 0) or
#         (command == command_negative and num < 0)
#     )
#     if filtered_command:
#         filtered_numbers.append((num))
#
# print(filtered_numbers)