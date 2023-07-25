import random

# Open text file with tarot card info
with open('tarotInfo.txt', 'r') as f:
    cards = 0
    card_names = []
    card_desc = []
    
    # obtain tarot card info into vectors
    for line in f:
        if line.strip()[0] != '-':
            #print(line.strip())
            card_names.append(line.strip())
            cards += 1
        elif line.strip()[0] == '-':
            card_desc.append(line.strip())
    
    
    
    # Choose between two types of readings
    # Past, Present, Future (3 cards)
    # Week ahead (7 cards)
    
    choice = None
    while choice != 'p' and choice != 'w':
        print("Do you wish to have your (p)ast, present, and future read?")
        print("Do you wish to have your (w)eek read?")
        choice = input("Which will it be: ")


    to_read = 0
    if choice == 'p':
        to_read = 3
        print("Your past, present, and future will be read")
    elif choice == 'w':
        to_read = 7
        print("Your week to come will be read")
    print("Press enter to proceed with each card")
    
    for i in range(to_read):
        input()
        # generate random card + its description
        rand_num = random.randint(1,cards)
        print(card_names[rand_num])
        print(card_desc[rand_num])