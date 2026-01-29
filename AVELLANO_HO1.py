# Hands-On 1. Word vs Number Average 

rndwrd = input("\nEnter a word: ")
length = len (rndwrd)

nmbr = []

for i in range(length):
    rndnmbr = int(input(f"Enter the number {i + 1 }: "))
    nmbr.append(rndnmbr)

print(nmbr)
print(f"The length of the word is {i + 1}.")

avrg = sum(nmbr) / len(nmbr)

print(f"The average of the numbers is {avrg}.")

if length < avrg:
    print(f"The length of the word '{rndwrd}' is less than the average.\n")
elif length < avrg:
    print(f"The length of the word '{rndwrd}' is greater than the average.\n")
else:
    print(f"The length of the word '{rndwrd}' is equal to the average.\n")