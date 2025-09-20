#A file to run unit tests on all the Spider Solitaire nested functions.

#Import the functions for testing
#Branch 4 functions
from down_placement import down_placement
from up_placement import up_placement
from card_2_math import card_2_math
from move_card import move_card
#Branch 3 functions
from user_decision import user_decision
from finish_sorting import finish_sorting
from display_cards import display_cards
#Branch 2 functions
from gameplay import gameplay
from results import results





#---------------------------TEST DOWN PLACEMENT FUNCTION---------------------------------------------------------------
#Correct situations (card converted to number for ace)
def test_down_placement():
    assert down_placement(card=6, down=['empty']) == True
    assert down_placement(card=5, down=['empty', 6]) == True
    assert down_placement(card=4, down=['empty', 6, 5]) == True
    assert down_placement(card=3, down=['empty', 6, 5, 4]) == True
    assert down_placement(card=2, down=['empty', 6, 5, 4, 3]) == True
    assert down_placement(card=1, down=['empty', 6, 5, 4, 3, 2]) == True
    assert down_placement(card=6, down=['empty', 6, 5, 4, 3, 2, 'A']) == True

#Test invalid situations
def test_down_placement_invalid():
    assert down_placement(card=6, down=['empty', 6]) == False
    assert down_placement(card=1, down=['empty']) == False
    assert down_placement(card=5, down=['empty']) == False
    assert down_placement(card=6, down=['empty', 6, 5, 4, 3, 2]) == False
    assert down_placement(card=7, down=['empty']) == False
    assert down_placement(card=12, down=['empty', 6, 5]) == False


#---------------------------TEST UP PLACEMENT FUNCTION------------------------------------------------------------------------
#Correct situations
def test_up_placement():
    assert up_placement(card=7, up1=['empty'], up2=['empty'], up3=['empty'], up4=['empty']) == 1
    assert up_placement(card=7, up1=['empty', 7, 8, 9, 10, 'J', 'Q'], up2=['empty'], up3=['empty'], up4=['empty']) == 2
    assert up_placement(card=7, up1=['empty', 7, 8, 9, 10, 'J', 'Q'], up2=['empty', 7, 8, 9], up3=['empty'], up4=['empty']) == 3
    assert up_placement(card=7, up1=['empty', 7, 8, 9, 10, 'J', 'Q'], up2=['empty', 7, 8, 9], up3=['empty', 7], up4=['empty']) == 4
    assert up_placement(card=13, up1=['empty', 7, 8, 9, 10, 'J', 'Q'], up2=['empty', 7, 8, 9], up3=['empty', 7], up4=['empty']) == 1
    assert up_placement(card=10, up1=['empty', 7, 8, 9, 10, 'J', 'Q'], up2=['empty', 7, 8, 9], up3=['empty', 7], up4=['empty']) == 2
    assert up_placement(card=8, up1=['empty', 7, 8, 9, 10, 'J', 'Q'], up2=['empty', 7, 8, 9], up3=['empty', 7], up4=['empty']) == 3

#Test invalid situations
def test_up_placement_invalid():
    assert up_placement(card=8, up1=['empty'], up2=['empty'], up3=['empty'], up4=['empty']) == 0
    assert up_placement(card=6, up1=['empty'], up2=['empty'], up3=['empty'], up4=['empty']) == 0
    assert up_placement(card=12, up1=['empty', 7, 8, 9, 10, 'J', 'Q'], up2=['empty', 7, 8, 9], up3=['empty', 7], up4=['empty']) == 0
    assert up_placement(card=9, up1=['empty', 7, 8, 9, 10, 'J', 'Q'], up2=['empty', 7, 8, 9], up3=['empty', 7], up4=['empty']) == 0


#---------------------------TEST CARD 2 MATH FUNCTION------------------------------------------------------------------------
#Correct situations
def test_card_2_math():
    assert card_2_math(card=9) == 9
    assert card_2_math(card=3) == 3
    assert card_2_math(card=6) == 6
    assert card_2_math(card='J') == 11
    assert card_2_math(card='Q') == 12
    assert card_2_math(card='K') == 13
    assert card_2_math(card='A') == 1


#---------------------------TEST MOVE CARD FUNCTION------------------------------------------------------------------------
def test_move_card():
    #Test drawn card to down pile movement
    assert move_card(['empty', 6, 5, 4], ['Q', 7, 3]) == (['empty', 6, 5, 4, 3], ['Q', 7])
    assert move_card(['empty'], ['Q', 7, 3, 6]) == (['empty', 6], ['Q', 7, 3])
    assert move_card(['empty', 6, 5, 4, 3, 2], ['A']) == (['empty', 6, 5, 4, 3, 2, 'A'], [])

    #Test drawn card to up pile movement
    assert move_card(['empty'], [4, 'J', 'Q', 7]) == (['empty', 7], [4, 'J', 'Q'])
    assert move_card(['empty', 7, 8, 9, 10], [4, 'J']) == (['empty', 7, 8, 9, 10, 'J'], [4])
    assert move_card(['empty', 7, 8, 9, 10, 'J', 'Q'], [4, 'J', 'Q', 'K']) == (['empty', 7, 8, 9, 10, 'J', 'Q', 'K'], [4, 'J', 'Q'])

    #Test drawn card to sixes pile movement
    assert move_card([6], ['Q', 8, 6]) == ([6, 6], ['Q', 8])
    
    #Test sixes to down pile movement
    assert move_card(['empty'], [6, 6]) == (['empty', 6], [6])

    #Test hand to down pile movement
    assert move_card(['empty', 6, 5, 4], ['Q', 8, 3, 10], 2) == (['empty', 6, 5, 4, 3], ['Q', 8, 10])

    #Test hand to up pile movement
    assert move_card(['empty', 7, 8, 9, 10, 'J'], ['Q', 8, 3, 10], 0) == (['empty', 7, 8, 9, 10, 'J', 'Q'], [8, 3, 10])


#---------------------------TEST USER DECISION FUNCTION------------------------------------------------------------------------
#I WOULD LIKE TO EXPAND THIS TEST
def test_user_decision():
    #Create random decks - 52 cards verified.
    deck = [2, 3,
            2, 3, 4, 9,
            2, 3, 4, 7, 8, 9, 10,
            'K',
            'J', 'Q', 'K',
            'J', 'Q', 'K', 'A',
            'J', 'Q', 'K', 'A',] #This has all the other cards removed.
    hand = [5, 'A', 10, 4] #This will be the 4 extra cards you can use at any time
    up1 = ['empty', 7, 8, 9, 10, 'J'] #This is the first 7 and up pile
    up2 = ['empty', 7, 8, 9, 10] #This is the second 7 and up pile
    up3 = ['empty', 7, 8] #This is the third 7 and up pile
    up4 = ['empty'] #This is the fourth 7 and up pile
    down = ['empty', 6, 5, 4, 3, 2, 'A', 6, 5] #This is the center 6 and down pile
    sixes = [6, 6] #The sixes pile off to the side
    drawn_cards = [5, 'Q'] #These are the cards drawn and kept from the deck each turn
 
    #Test use drawn card (decision 1)
    decision = 1
    updated_drawn_cards = [5]
    updated_up1 = ['empty', 7, 8, 9, 10, 'J', 'Q']
    assert user_decision(decision, deck, hand, up1, up2, up3, up4, down, sixes, drawn_cards) == (deck, hand, updated_up1, up2, up3, up4, down, sixes, updated_drawn_cards)

    #Test use hand card (decision 2)
    decision = 2
    updated_hand = [5, 'A', 10]
    updated_down = ['empty', 6, 5, 4, 3, 2, 'A', 6, 5, 4]
    assert user_decision(decision, deck, hand, up1, up2, up3, up4, down, sixes, drawn_cards) == (deck, updated_hand, up1, up2, up3, up4, updated_down, sixes, drawn_cards)

    #Test use a six (decision 3)
    decision = 3
    different_down = ['empty', 6, 5, 4, 3, 2, 'A'] #This needs to be different so a 6 can be used.
    updated_sixes = [6]
    updated_different_down = ['empty', 6, 5, 4, 3, 2, 'A', 6]
    assert user_decision(decision, deck, hand, up1, up2, up3, up4, different_down, sixes, drawn_cards) == (deck, hand, up1, up2, up3, up4, updated_different_down, updated_sixes, drawn_cards)
    
    #Test draw a new card (decision 4)
    #I'm not sure how to test this...


#---------------------------TEST FINISH SORTING FUNCTION------------------------------------------------------------------------
#Test correct situations - fully sorted
def test_finish_sorting():
    #Starting decks
    up1 = ['empty', 7, 8, 9, 10, 'J', 'Q', 'K']
    up2 = ['empty', 7, 8, 9, 10, 'J', 'Q', 'K']
    up3 = ['empty', 7, 8, 9, 10, 'J']
    up4 = ['empty', 7, 8]
    down = ['empty', 6, 5, 4, 3, 2, 'A', 6, 5, 4, 3, 2, 'A', 6, 5, 4]
    hand = ['K', 'Q', 10, 2]
    sixes = [6]
    drawn_cards = ['J', 'A', 3, 2, 9, 4, 'Q', 'K', 'A', 5, 3]
    #Decks after sorting
    up1_finished = up1
    up2_finished = up2
    up3_finished = ['empty', 7, 8, 9, 10, 'J', 'Q', 'K']
    up4_finished = ['empty', 7, 8, 9, 10, 'J', 'Q', 'K']
    down_finished = ['empty', 6, 5, 4, 3, 2, 'A', 6, 5, 4, 3, 2, 'A', 6, 5, 4, 3, 2, 'A', 6, 5, 4, 3, 2, 'A']
    hand_finished = []
    sixes_finished = []
    drawn_cards_finished = []
    assert finish_sorting(hand, up1, up2, up3, up4, down, sixes, drawn_cards) == (hand_finished, up1_finished, up2_finished, up3_finished, up4_finished, down_finished, sixes_finished, drawn_cards_finished)

#Partially sorted
def test_finish_sorting_2():
    #Starting decks
    up1 = ['empty', 7, 8, 9, 10, 'J', 'Q', 'K']
    up2 = ['empty', 7, 8, 9, 10, 'J', 'Q', 'K']
    up3 = ['empty', 7, 8, 9, 10, 'J']
    up4 = ['empty', 7, 8]
    down = ['empty', 6, 5, 4, 3, 2, 'A', 6, 5, 4, 3, 2, 'A', 6, 5, 4]
    hand = ['K', 'K', 10, 2]
    sixes = [6]
    drawn_cards = ['J', 'A', 5, 2, 9, 'Q', 'Q', 4, 'A', 3, 3]
    #Decks after sorting
    up1_finished = up1
    up2_finished = up2
    up3_finished = up3
    up4_finished = up4
    down_finished = ['empty', 6, 5, 4, 3, 2, 'A', 6, 5, 4, 3, 2, 'A', 6, 5, 4, 3, 2, 'A', 6]
    hand_finished = ['K', 'K', 10, 3]
    sixes_finished = []
    drawn_cards_finished = ['J', 'A', 5, 2, 9, 'Q', 'Q', 4]
    assert finish_sorting(hand, up1, up2, up3, up4, down, sixes, drawn_cards) == (hand_finished, up1_finished, up2_finished, up3_finished, up4_finished, down_finished, sixes_finished, drawn_cards_finished)


#---------------------------TEST DISPLAY CARDS FUNCTION------------------------------------------------------------------------
#I do not think this can be pytested because there is no output, only print statements


#---------------------------TEST GAMEPLAY FUNCTION------------------------------------------------------------------------
#I do not think this can be tested as it is currently written becuase it has no inputs, it is only called.

#---------------------------TEST RESULTS FUNCTION------------------------------------------------------------------------
def test_results():
    #Piles if the game is won
    up1 = ['empty', 7, 8, 9, 10, 'J', 'Q', 'K']
    up2 = ['empty', 7, 8, 9, 10, 'J', 'Q', 'K']
    up3 = ['empty', 7, 8, 9, 10, 'J', 'Q', 'K']
    up4 = ['empty', 7, 8, 9, 10, 'J', 'Q', 'K']
    down = ['empty', 6, 5, 4, 3, 2, 'A', 6, 5, 4, 3, 2, 'A', 6, 5, 4, 3, 2, 'A', 6, 5, 4, 3, 2, 'A']
    assert results(up1, up2, up3, up4, down) == 52

    #Piles for a random different game
    up1 = ['empty', 7, 8, 9, 10, 'J', 'Q', 'K']
    up2 = ['empty', 7, 8, 9, 10, 'J', 'Q', 'K']
    up3 = ['empty', 7, 8]
    up4 = ['empty', 7, 8]
    down = ['empty', 6, 5, 4, 3, 2]
    assert results(up1, up2, up3, up4, down) == 23



test_user_decision()