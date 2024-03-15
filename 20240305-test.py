user_input = input('Please input: ')
list = []

print(f"You've said {user_input}")

def Fun(name):
    print(name)

if user_input == "0":
    print("First")
    list = ['A', 'B', 'C']
    condition = False

elif user_input == "1":
    print("Second")
    list = ['D', 'E', 'F']
    condition = False

else:
    print("others")
    list = ['Y', 'I', 'N']
    condition = True

for letters in list:
    print(letters)

while condition == True:
    print("Passed")
    Fun('Hapi')
    break

