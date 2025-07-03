class student:
    def __init__(self, name, average):
        self.name = name
        self.average = average

    def __str__(self):
        return f"{self.name} ({self.average})"


input = input("enter name and average with a space")
inputs = input.split()
p1 = student(inputs[0], inputs[1])
print(p1)
