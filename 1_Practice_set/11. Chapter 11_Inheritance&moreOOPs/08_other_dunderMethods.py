class Number:
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return f"Decimal number: {self.num}"

    def __len__(self):
        return 1

n1 = Number(4)
print(n1)
print(len(n1))