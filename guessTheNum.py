import random
while(True):
    n = int(input("Enter a number: "))
    m = int(input("Enter another number: "))
    if n <= m:
        break
    print("Please enter the values again.")

roop = 3
r = random.randint(n, m)

print(f"Guess the number between {n} and {m} within {roop} attempts")

for i in range(roop):
    print(f"Remaining attempts: {roop - i}")
    ans = int(input("Your guess: "))
    if ans == r:
        print(f"Congratulations! You guessed it right in {i + 1} attempts.")
        break

if ans != r:
    print(f"The correct answer was {r}")
