

def finish_sorting(hand, up1, up2, up3, up4, down, sixes, drawn_cards):
    '''
    This is a function that will finish placing cards into the up and down piles once the deck is empty.
    The process will loop until no more cards can be placed using a while true loop.
    Within the while true loop, there are two main steps. First, test if a card fits somewhere and second, place the card.
    Inputs include all the piles (except the deck because it is assumed to be empty).
    Outputs include the same piles but updated.
    '''

    #Import libraries
    from card_2_math import card_2_math
    from up_placement import up_placement
    from down_placement import down_placement
    from move_card import move_card
    

 

    #Loop until no more cards can be placed
    while True:

        #Find how many cards are in each relevant pile
        length_drawn_cards = len(drawn_cards)
        length_hand = len(hand)
        length_sixes = len(sixes)

        #Set the match indicators to False to start a new loop
        sixes_match = False
        hand_match = False
        drawn_cards_match = False



 


        #-------------PART 1 - TEST IF A CARD CAN BE PLACED ---------------------------------------------
        #Does the sixes pile have a match?
        #Obtain the last 6
        if length_sixes:
            card = sixes[-1]
            #Can the card be used on the down pile?
            if down_placement(card, down) == True:
                sixes_match = True
 

        #Does the hand pile have a match?
        #Loop for each card to check. Return True if a match is found
        for i in range(length_hand):
            #Obtain the card of interest
            card = hand[i]
            #Convert card to mathematical value
            card = card_2_math(card)  

            #Can the card be used on one of the up piles?
            if up_placement(card, up1, up2, up3, up4): #This will return 0 if card does not fit into any of the up piles.
                hand_match = True
            #Can the card be used on the down pile?
            elif down_placement(card, down) == True:
                hand_match = True
            #Can the card be used on the sixes pile - make sure this option is after the down placement option.
            elif card == 6:
                hand_match = True


        #Does the last drawn card have a match?
        if length_drawn_cards:
            #Obtain the top drawn card
            card = drawn_cards[-1]
            #Convert card to mathematical value
            card = card_2_math(card)

            #Can the card be used on one of the up piles? 
            if up_placement(card, up1, up2, up3, up4): #This will return 0 if card does not fit into any of the up piles.
                drawn_cards_match = True
            #Can the card be used on the down pile?
            elif down_placement(card, down) == True:
                drawn_cards_match = True
            #Can the card be used on the sixes pile - make sure this option is after the down placement option.
            elif card == 6:
                drawn_cards_match = True
            #Can the drawn card be added to the hand? - make sure this is the last option.
            elif length_hand < 4: 
                drawn_cards_match = True



        #-----------PART 2 - PLACE THE CARD OR EXIT WHILE LOOP -------------------------------------
        #If a 6 from the sixes pile fits on the down
        if sixes_match == True:
            #Move the card
            down, sixes = move_card(down, sixes)
            #Continue while true loop
            continue
            

        #Elif one of the cards in the hand fits somewhere
        elif hand_match == True:
            #Find where the card fits, append, and remove the card. Once the card is moved, break the for loop.
            for i in range(length_hand):
                #obtain the card of interest
                card = hand[i]
                #Convert card to mathematical value
                card = card_2_math(card)  

                #Can the card be used on one of the up piles?
                if up_placement(card, up1, up2, up3, up4): #This will return 0 if card does not fit into any of the up piles.
                    #Up pile #1
                    if up_placement(card, up1, up2, up3, up4) == 1:
                        up1, hand = move_card(up1, hand, i)
                        #Break for loop
                        break
                    #Up pile #2
                    elif up_placement(card, up1, up2, up3, up4) == 2:
                        up2, hand = move_card(up2, hand, i)
                        #Break for loop
                        break
                    #Up pile #3
                    elif up_placement(card, up1, up2, up3, up4) == 3:
                        up3, hand = move_card(up3, hand, i)
                        #Break for loop
                        break
                    #Up pile #4
                    elif up_placement(card, up1, up2, up3, up4) == 4:
                        up4, hand = move_card(up4, hand, i)
                        #Break for loop
                        break

                #Can the card be used on the down pile?
                elif down_placement(card, down) == True:
                    down, hand = move_card(down, hand, i)
                    #Break for loop
                    break

                #Can the card be used on the sixes pile - make sure this option is after the down placement option.
                elif card == 6:
                    sixes, hand = move_card(sixes, hand, i)
                    #Break for loop
                    break
            
            #Continue while true loop after the hand card has been placed.
            continue


        #Elif the most recent drawn card fits somewhere
        elif drawn_cards_match == True:
            #Obtain the card of interest
            card = drawn_cards[-1]
            #Convert card to mathematical value
            card = card_2_math(card)

            #Can the card be used on one of the up piles? 
            if up_placement(card, up1, up2, up3, up4): #This will return 0 if card does not fit into any of the up piles.
                #Up pile #1
                if up_placement(card, up1, up2, up3, up4) == 1:
                    up1, drawn_cards = move_card(up1, drawn_cards)
                    #Continue the while true loop
                    continue
                #Up pile #2
                elif up_placement(card, up1, up2, up3, up4) == 2:
                    up2, drawn_cards = move_card(up2, drawn_cards)
                    #Continue the while true loop
                    continue
                #Up pile #3
                elif up_placement(card, up1, up2, up3, up4) == 3:
                    up3, drawn_cards = move_card(up3, drawn_cards)
                    #Continue the while true loop
                    continue
                #Up pile #4
                elif up_placement(card, up1, up2, up3, up4) == 4:
                    up4, drawn_cards = move_card(up4, drawn_cards)
                    #Continue the while true loop
                    continue

            #Can the card be used on the down pile?
            elif down_placement(card, down) == True:
                down, drawn_cards = move_card(down, drawn_cards)
                #Continue the while true loop
                continue

            #Can the card be used on the sixes pile - make sure this option is after the down placement option.
            elif card == 6:
                sixes, drawn_cards = move_card(sixes, drawn_cards)
                #Continue the while true loop
                continue

            #Can the drawn card be added to the hand? - Make sure this is the last option.
            elif length_hand < 4: 
                hand, drawn_cards = move_card(hand, drawn_cards)
                #Continue the while true loop
                continue

        #If there are no cards that match.
        else:
            #Break while true loop
            break

        
        
        
        
        
        



    #Return the finished piles
    return hand, up1, up2, up3, up4, down, sixes, drawn_cards




# #Test the function
# hand = [3, 10, 'Q', 'K'] #This will be the 4 extra cards you can use at any time
# up1 = ['empty', 7, 8, 9] #This is the first 7 and up pile
# up2 = ['empty', 7, 8] #This is the second 7 and up pile
# up3 = ['empty', 7, 8] #This is the third 7 and up pile
# up4 = ['empty', 7] #This is the fourth 7 and up pile
# down = ['empty', 6, 5, 4] #This is the center 6 and down pile
# sixes = [6] #The sixes pile off to the side
# drawn_cards = [9, 'Q', 2, 3, 'J'] #These are the cards drawn and kept from the deck each turn

# finish_sorting(hand, up1, up2, up3, up4, down, sixes, drawn_cards)

# from display_cards import display_cards
# display_cards(hand, up1, up2, up3, up4, down, sixes, drawn_cards)


