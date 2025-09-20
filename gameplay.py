

def gameplay():
    '''
    This function defines the gameplay within the Spider Solitaire game and is directly nested under the top function spider_solitaire.
    This function initiates the cards, deals the initial hand, then uses nested functions to continue the game.
    These nested functions are under an iterating while loop until the deck runs out of cards.
    Also within the loop, a user input exists which asks which action the player would like to perform.
    Once the deck runs out, the nested function finish_sorting will make sure all applicable cards are placed.
    Inputs are not needed for this function, it is simply called.
    Outputs include the finished decks for calculation (up1, up2, up3, up4 and down).
    '''

    #Import libraries and functions
    import random
    import time
    from user_decision import user_decision
    from display_cards import display_cards
    from finish_sorting import finish_sorting

 

    #Initiate the different piles
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10,
            2, 3, 4, 5, 6, 7, 8, 9, 10,
            2, 3, 4, 5, 6, 7, 8, 9, 10,
            2, 3, 4, 5, 6, 7, 8, 9, 10,
            'J', 'Q', 'K', 'A',
            'J', 'Q', 'K', 'A',
            'J', 'Q', 'K', 'A',
            'J', 'Q', 'K', 'A',]
    hand = [] #This will be the 4 extra cards you can use at any time
    up1 = ['empty'] #This is the first 7 and up pile
    up2 = ['empty'] #This is the second 7 and up pile
    up3 = ['empty'] #This is the third 7 and up pile
    up4 = ['empty'] #This is the fourth 7 and up pile
    down = ['empty'] #This is the center 6 and down pile
    sixes = [] #The sixes pile off to the side
    drawn_cards = [] #These are the cards drawn and kept from the deck each turn



    #Deal out the cards
    #Use 4 random cards from the deck to build out the hand
    for i in range(4):
        card = random.choice(deck)
        hand.append(card)
        deck.remove(card)

    #Draw the first card
    card = random.choice(deck)
    drawn_cards.append(card)
    deck.remove(card)


 

    #User options loop begins. Loops until the deck is empty.
    while deck:

        #Display current situation
        display_cards(hand, up1, up2, up3, up4, down, sixes, drawn_cards)

        #Prompt the user how they would like to act. They have 4 choices and must respond with an integral 1 - 4.
        decision = input("What would you like to do?\n1 - Use the card you drew\n2 - Use one of the cards in your hand\n3 - Use one of your sixes\n4 - draw a new card \nYour selection --> ")
       
       
        #Error checking - Make sure the response is an integral.
        try:
            decision = int(decision)
        except ValueError:
            print("User must choose option 1, 2, 3, or 4. Try Again.")
            continue

        #Perform the user's decision
        if decision == 1 or decision == 2 or decision == 3 or decision == 4:
            deck, hand, up1, up2, up3, up4, down, sixes, drawn_cards = user_decision(decision, deck, hand, up1, up2, up3, up4, down, sixes, drawn_cards)
            continue

        #Error checking - invalid integral given.       
        else:
            print("User must choose option 1, 2, 3, or 4. Try Again.")
            continue

 

    #Once the deck is empty, finish sorting the remaining cards from the hand, sixes, and drawn_cards stack if applicable
    hand, up1, up2, up3, up4, down, sixes, drawn_cards = finish_sorting(hand, up1, up2, up3, up4, down, sixes, drawn_cards)

    #Create a 5 second pause to show that the game is done.
    print("The entire deck has been used...")
    time.sleep(5)
    
    #Show the player the finished stacks and the drawn card pile.
    print("Here are your finished stacks. Good game!")
    display_cards(hand, up1, up2, up3, up4, down, sixes, drawn_cards)
    print(f"For reference, the drawn card stack has: {drawn_cards}")
    
    
    
    
    #Return the finished decks including up1, up2, up3, up4 and down so results can be calculated.
    return up1, up2, up3, up4, down


    