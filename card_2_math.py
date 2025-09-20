

def card_2_math(card):
    '''
    This is a quick function that will convert all playing deck cards into mathematical values
    I.e. if it is a Jack, the card will now be 11
    Inputs include the card in card form
    Outputs include the card in mathematical form
    '''

    if card == 'J':
        card = 11
    elif card == 'Q':
        card = 12
    elif card == 'K':
        card = 13
    elif card == 'A':
        card =1
    else:
        pass

    return card



