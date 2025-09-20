 

def user_decision(decision, deck, hand, up1, up2, up3, up4, down, sixes, drawn_cards):
    '''
    This is a function that helps the player make decisions and implements card movement.
    The meat of this project is located under the gameplay function.
    This function takes user input of 1, 2, 3, or 4 which is how the user decides which card movement to perform.
    Based upon the selection, the card automatically transfers piles if acceptable.
    Inputs include the user decision integral (should be a number 1-4), and all card piles in the game.
    Outputs include all updated card piles in the game based upon the users decision.
    '''
     
 
    #Import assisting functions
    from card_2_math import card_2_math
    from down_placement import down_placement
    from up_placement import up_placement
    from move_card import move_card
    import random



    #Use drawn card
    if decision == 1:
        #Error check - are there any drawn cards?
        if not drawn_cards:
            print("There are no drawn cards to use. Re-try and select a different option.")
            return deck, hand, up1, up2, up3, up4, down, sixes, drawn_cards
        
        else:
            #Pull out the current card to use.
            card = drawn_cards[-1] 
            #Convert card to mathematical value
            card = card_2_math(card)

            #How many cards are currently in the hand - info needed for later
            cards_in_hand = len(hand)

             
            #Can the card be used on one of the up piles? If so, move it there and return the updated piles.
            if up_placement(card, up1, up2, up3, up4): #This will return 0 and if statement will be skipped if card does not fit into any of the up piles.
                #Up pile #1
                if up_placement(card, up1, up2, up3, up4) == 1:
                    up1, drawn_cards = move_card(up1, drawn_cards)
                    return deck, hand, up1, up2, up3, up4, down, sixes, drawn_cards
                #Up pile #2
                elif up_placement(card, up1, up2, up3, up4) == 2:
                    up2, drawn_cards = move_card(up2, drawn_cards)
                    return deck, hand, up1, up2, up3, up4, down, sixes, drawn_cards
                #Up pile #3
                elif up_placement(card, up1, up2, up3, up4) == 3:
                    up3, drawn_cards = move_card(up3, drawn_cards)
                    return deck, hand, up1, up2, up3, up4, down, sixes, drawn_cards
                #Up pile #4
                elif up_placement(card, up1, up2, up3, up4) == 4:
                    up4, drawn_cards = move_card(up4, drawn_cards)
                    return deck, hand, up1, up2, up3, up4, down, sixes, drawn_cards

            #Can the card be used on the down pile? If so, move it there and return the updated piles.
            elif down_placement(card, down) == True:
                down, drawn_cards = move_card(down, drawn_cards)
                return deck, hand, up1, up2, up3, up4, down, sixes, drawn_cards

            #Can the card be used on the sixes pile - make sure this option is after the down placement option.
            elif card == 6:
                sixes, drawn_cards = move_card(sixes, drawn_cards)
                return deck, hand, up1, up2, up3, up4, down, sixes, drawn_cards

            #Can the drawn card be added to the hand? - make sure this is the last option for using the drawn card.
            elif cards_in_hand < 4: 
                hand, drawn_cards = move_card(hand, drawn_cards)
                return deck, hand, up1, up2, up3, up4, down, sixes, drawn_cards

            #If the drawn card can't be used, tell the user and send the loop again.
            else:
                print("The drawn card cannot be used, select a different option.")
                return deck, hand, up1, up2, up3, up4, down, sixes, drawn_cards
        





    #Use hand cards
    elif decision == 2:
        #How many cards are currently in the hand?
        cards_in_hand = len(hand)

        #If no cards are found in the hand
        if not cards_in_hand:
            print("No cards were found in your hand. Select a different option.")
            return deck, hand, up1, up2, up3, up4, down, sixes, drawn_cards
        
        #If cards are found in the hand
        else:
            #Loop for each card to check where it can fit. Break loop when/if a card is placed
            for i in range(cards_in_hand):
                #Pull the card of interest
                card = hand[i]
                #Convert card to mathematical value
                card = card_2_math(card)  

                
                #Can the card be used on one of the up piles?
                if up_placement(card, up1, up2, up3, up4): #This will return 0 if card does not fit into any of the up piles.
                    #Up pile #1
                    if up_placement(card, up1, up2, up3, up4) == 1:
                        up1, hand = move_card(up1, hand, i)
                        return deck, hand, up1, up2, up3, up4, down, sixes, drawn_cards
                    #Up pile #2
                    elif up_placement(card, up1, up2, up3, up4) == 2:
                        up2, hand = move_card(up2, hand, i)
                        return deck, hand, up1, up2, up3, up4, down, sixes, drawn_cards
                    #Up pile #3
                    elif up_placement(card, up1, up2, up3, up4) == 3:
                        up3, hand = move_card(up3, hand, i)
                        return deck, hand, up1, up2, up3, up4, down, sixes, drawn_cards
                    #Up pile #4
                    elif up_placement(card, up1, up2, up3, up4) == 4:
                        up4, hand = move_card(up4, hand, i)
                        return deck, hand, up1, up2, up3, up4, down, sixes, drawn_cards

                #Can the card be used on the down pile?
                elif down_placement(card, down) == True:
                    down, hand = move_card(down, hand, i)
                    return deck, hand, up1, up2, up3, up4, down, sixes, drawn_cards

                #Can the card be used on the sixes pile - make sure this option is after the down placement option.
                elif card == 6:
                    sixes, hand = move_card(sixes, hand, i)
                    return deck, hand, up1, up2, up3, up4, down, sixes, drawn_cards
                
                #If the card can't be used, continue to the next card in the hand.
                else:
                    pass

            #If all the cards in the hand have been looped through and don't fit anywhere.
            print("None of the cards in your hand fit in a pile. Select a different option.")
            return deck, hand, up1, up2, up3, up4, down, sixes, drawn_cards




    #Use one of the sixes
    elif decision == 3:
        #If there are no sixes in the sixes pile, tell the user to try again.
        if not sixes:
            print("No sixes were found in the sixes pile. Please select a different option.")
            return deck, hand, up1, up2, up3, up4, down, sixes, drawn_cards
        
        #If there are sixes present
        else:
            #Pull the last six in the pile
            card = sixes[-1]
            #Can the card be used on the down pile?
            if down_placement(card, down) == True:
                down, sixes = move_card(down, sixes)
                return deck, hand, up1, up2, up3, up4, down, sixes, drawn_cards
            else:
                print("It looks like the 6 cannot be placed at this time.")
                return deck, hand, up1, up2, up3, up4, down, sixes, drawn_cards






    #Draw a new card   
    elif decision == 4:
        card = random.choice(deck)
        drawn_cards.append(card)
        deck.remove(card)
        return deck, hand, up1, up2, up3, up4, down, sixes, drawn_cards



    #Error - the user input was not a valid selection
    else:
        print("Invalid user decision given. This error should not arise, the program is now broken.")
        return deck, hand, up1, up2, up3, up4, down, sixes, drawn_cards


