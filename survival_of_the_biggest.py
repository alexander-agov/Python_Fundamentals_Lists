list_of_integer = [int(num) for num in input().split(" ")]
number = int(input())
smallest_number = min(list_of_integer)
for count in range(number):
    list_of_integer.remove(min(list_of_integer))
print(', '.join(map(str, list_of_integer)))