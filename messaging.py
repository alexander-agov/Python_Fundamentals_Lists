

sequence = input().split()
text = input().strip()
message = ''
while sequence:
    index = sum(int(digit) for digit in str(sequence.pop(0)))
    index %= len(text)
    message += text[index]
    text = text[:index] + text[index+1:]
print(message)
