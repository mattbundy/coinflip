import random as rand
choices = ["Heads", "Tails"]
log = []
number_of_flips = int(input("How many flips would you like to perform?: "))
flips = 0

def flip(flips):
    result = rand.choice(choices)
    log.append(result)
    return flips + 1

while flips < number_of_flips:
    flips = flip(flips)

tails = log.count("Tails")
heads = log.count("Heads")

print("Out of " + str(number_of_flips) + " flips, " + str(tails) + " were tails and " + str(heads) + " were heads!")
percentage = input("Would you like to view that in a percentage format? (yes or no): ").lower()
tails_percentage = round(((tails/(tails + heads))*100),2)
heads_percentage = round(((heads/(tails + heads))*100),2)

if percentage == "yes":
    print("Out of " + str(number_of_flips) + " flips, " + str(tails_percentage) + "% were tails and " + str(heads_percentage) + "% were heads!")
else:
    exit()
