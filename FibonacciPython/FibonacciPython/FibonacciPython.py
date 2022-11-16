
first = 1
second = 0
sequence = [0,1]

for i in range(1,1000):
    value = first + second
    sequence.append(value)
    second = first
    first = value
running = True

while running:
    validating = True
    while validating:
        try:
            term = int(input("\nSelect an Nth term from 0 to 1000\n"))
            if term < 0 or term > 1000:
                print("Input is too low/high. Try again")
            else:
                validating = True
                break
        except ValueError:
            print("Input is not a valid number. Try again.")
    print("Nth term: {term}")
    print(f"Value: {sequence[term]}")
                