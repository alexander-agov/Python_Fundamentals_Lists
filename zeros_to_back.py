string_of_integers = input().split(", ")
count_zeros = string_of_integers.count('0')
while '0' in string_of_integers:
    string_of_integers.pop(string_of_integers.index('0'))
for num in range(count_zeros):
    string_of_integers.append('0')
print([int(num) for num in string_of_integers])