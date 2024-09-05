a = 5
def change():
    global a
    a = 6

change()
print(a)

b = "abc"
b.upper()
print(b)

c = True

match c:
    case 5:
        print("no change")
    case 6:
        print("changed")
    case True:
        print("works for boolean also")

x = [1,2,3]
for i, e in enumerate(x):
    print(i, e)

try:
    total_value = float(input("Enter total value: "))
    value = float(input("Enter value: "))

    percentage = (value / total_value) * 100

    print(f"{percentage:.1f}")
except ValueError:
    print("You need to enter a number. Run the program again.")