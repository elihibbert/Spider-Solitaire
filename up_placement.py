

def up_placement(card, up1, up2, up3, up4):
    '''
    A function that tests the logic of placing the card onto one of the up piles.
    Inputs include the current card variable (as mathematical value) along with lists of the up piles 1-4.
    The up lists hold actual card values (not math values) and start with "empty".
    Outputs include a number. 0 if the card does not fit into any pile. 1, 2, 3, or 4 depending upon which pile the card fits into.
    '''
    #Import functions
    from card_2_math import card_2_math


    #Does the card fit in the up1 pile?
    #If up1 is empty and card is a 7
    if up1[-1] == "empty" and card == 7:
        return 1

    #If the last value of up1 = card -1
    elif card_2_math(up1[-1]) == card - 1:
        return 1



    #Does the card fit in the up2 pile?
    #If up2 is empty and card is a 7
    elif up2[-1] == "empty" and card == 7:
        return 2

    #If the last value of up2 = card -1
    elif card_2_math(up2[-1]) == card - 1:
        return 2



    #Does the card fit in the up3 pile?
    #If up3 is empty and card is a 7
    elif up3[-1] == "empty" and card == 7:
        return 3

    #If the last value of up3 = card -1
    elif card_2_math(up3[-1]) == card - 1:
        return 3



    #Does the card fit in the up4 pile?
    #If up4 is empty and card is a 7
    elif up4[-1] == "empty" and card == 7:
        return 4

    #If the last value of up4 = card -1
    elif card_2_math(up4[-1]) == card - 1:
        return 4
    

    
    #If the card does not fit into any of these piles, return 0
    else:
        return 0
    



# #Test the function
# up1 = ['empty', 7, 8] #This is the first 7 and up pile
# up2 = ['empty'] #This is the second 7 and up pile
# up3 = ['empty', 7, 8, 9, 10, "J", "Q", "K"] #This is the third 7 and up pile
# up4 = ['empty', 7, 8, 9, 10, "J"] #This is the fourth 7 and up pile

# card = 9

# result = up_placement(card, up1, up2, up3, up4)

# print(f"The card will be place in up pile {result}")
