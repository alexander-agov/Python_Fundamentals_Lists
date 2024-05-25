n = int(input())
word = input()
sentence = []
for _ in range(n):
    strings = input()
    sentence.append(strings)
print(sentence)
for i in range(len(sentence)-1, -1, -1):
    element = sentence[i]
    if word not in element:
        sentence.remove(element)
print(sentence)
