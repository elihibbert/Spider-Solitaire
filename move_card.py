

def move_card(append_pile, remove_pile, card_index=-1):
    '''
    This supporting function will move a card from one pile to a different pile.
    The remove_pile should never be empty when this function is run.
    This function is intended to reduce lines of code and trivial errors.
    Inputs include two lists, first the pile that will be added to, and second the pile that will be subtracted from.
    The last input is the card index to be moved. This is given as an int. The function assumes the last card in the pile if not given.
    Outputs include the same two piles but after the card has been moved.
    '''

    #Remove the card from the original location and save to card variable. Using a try statement in case the card is not found.
    try:
        card = remove_pile.pop(card_index)
    except IndexError:
        print("The card was not found from the pile losing a card. If you are seeing this error, the program is broken.")

    #Add the card to the last spot in the append pile.
    append_pile.append(card)

    #Return the piles.
    return append_pile, remove_pile


# #Test the function
# drawn_cards = ['K', 4, 9, 10, 'Q', 10]
# up1 = ['empty', 7, 8, 9]
# up1, drawn_cards = move_card(up1, drawn_cards)
# print(drawn_cards)
# print(up1)