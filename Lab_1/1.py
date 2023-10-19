numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]


for i in range(len(numbers)):
    if numbers[i] == None:
        s = i
        break
numbers[s] = 0
for i in range(len(numbers)):
    if i != s:
        numbers[s] = numbers[i] + numbers[s]
numbers[s] = numbers[s] / len(numbers)



print("Измененный список:", numbers)
