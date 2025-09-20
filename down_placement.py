

def down_placement(card, down):
    '''
    This is a function that tests the logic of placing the card onto the down pile.
    Inputs include the current card and the current down list.
    The card should be given in mathematical terms, the down list should be given as a list of cards (not mathematical).
    If the down pile's first value must be "empty".
    Outputs include True or False. True if the card fits, False if the card does not fit.
    '''

    #If the down pile is empty, a 6 can be taken
    if down[-1] == "empty" and card == 6:
        return True

    #If the last down card = card + 1, the card can be placed.
    elif down[-1] == card + 1:
        return True

    #If the down pile has an ace, a 6 can be taken
    elif down[-1] == "A" and card == 6:
        return True
    
    #The card cannot be placed on the down pile
    else:
        return False
