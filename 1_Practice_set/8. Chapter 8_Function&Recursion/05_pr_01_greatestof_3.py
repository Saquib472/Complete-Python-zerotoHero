def greatest(numbers):
    if numbers[0] > numbers[1]:
        f1 = numbers[0]
    else:
        f1 = numbers[1]

    if f1 > numbers[2]:
        print(f"The greatest number among three is {f1}")
    else:
        print(f"The greatest number among three is {numbers[2]}")

num = []
for i in range(3):
    nm = int(input(f"enter the {i+1}st number: "))
    num.append(nm)

greatest(num)
