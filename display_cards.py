

def display_cards(hand, up1, up2, up3, up4, down, sixes, drawn_cards):
    '''
    This is a function which helps the player visualize the current standings of cards on the table.
    Currently this is a very basic visual representation and will be improved at a later date.
    This function will be called directly before the player makes a decision. 
    This function is nested under the gameplay function.
    Inputs include all current pile lists.
    This function technically has no outputs however it will print each pile for the player to see.
    Each pile will simply show the top card in brackets.
    '''
 

    print()
    print("----------------------------------------------")
    print(f"The up stacks are showing: [{up1[-1]}]  [{up2[-1]}]  [{up3[-1]}]  [{up4[-1]}]")
    print()
    print(f"The down stack is showing: [{down[-1]}]")
    print()
    print(f"You have {len(sixes)} sixes available to use.")
    print("           --------------")
    if not hand:
        print("You currently have no cards in your hand.")
    else:
        hand_length = len(hand)
        print(f"Your current hand is showing: ", end='')
        for i in range(hand_length):
            print(f"[{hand[i]}] ", end='')
    print()
    print()
    if not drawn_cards:
        print("You have no cards currently drawn.")
    else:
        print(f"The card you drew is: [{drawn_cards[-1]}]")
    print("----------------------------------------------")





# #Test this file
# hand = ['J', 3, 'K'] #This will be the 4 extra cards you can use at any time
# up1 = ['empty', 7, 8, 9] #This is the first 7 and up pile
# up2 = ['empty'] #This is the second 7 and up pile
# up3 = ['empty', 7, 8, 9, 10, 'J', 'Q'] #This is the third 7 and up pile
# up4 = ['empty', 7] #This is the fourth 7 and up pile
# down = ['empty', 6, 5, 4, 3, 2, 'A', 6, 5] #This is the center 6 and down pile
# sixes = [6, 6] #The sixes pile off to the side
# drawn_cards = [7, 9, 'Q'] #These are the cards drawn and kept from the deck each turn

# display_cards(hand, up1, up2, up3, up4, down, sixes, drawn_cards)