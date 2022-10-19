
# The if-statement
if False:
    print("It's true!")

# The non-empty string below is truthy in nature. 
# the condition/predicate will be implicitly converted to bool
if "eggs":
    print("Yes please!")

# The if-statement supports an optional else clause which goes in a block introduced by the
# else keyword (followed by a colon) which is indented to the same level as the if keyword.
h = 42
if h > 50:
    print("Greater than 50")
else:
    print("50 or smaller")

# if...elif...else
if h > 50:
    print("Greater than 50")
elif h < 20:
    print("Less than 20")
else:
    print("Between 20 and 50")

# the while-loop
c = 10
while c:
    print(c)
    c -= 1

while True:
    response = input("Enter a number:")
    if int(response) % 7 == 0:
        break


# for loop examples

# i. 
for i in reversed(range(0, 10, 2)):
    print(i)

# ii. Iterating over sequences (works the same over tuples, strings)
for index, item in enumerate(["A", "B", "C"]):
    print(index, item)
    if index == 1:
        break
    else:
        continue