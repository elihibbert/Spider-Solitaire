#This is a remake of the function display_cards. This second version will use tkinter library to create a better user interface
#Additionally, rather than no outputs returned, this function will return the user decision variable

 


def display_cards(hand, up1, up2, up3, up4, down, sixes, drawn_cards):
    '''
    This is a function which will display the cards at the current point in the game for the user to see.
    The tkinter library will be used as the graphic user interface.
    The application will display the up and down piles.
    The player can also click on the hand cards, the top drawn card, or the top 6 to use it.
    Inputs include all the current piles
    Outputs include the user decision which should be 1, 2, 3, or 4.
    This will be generated based upon what pile the player clicks on.
    '''

    #Import the needed ui classes. Do I need to import the child class as well?
    from ui_classes import Application

    #Create an instance of the application
    user_interface = Application(hand, up1, up2, up3, up4, down, sixes, drawn_cards)
    user_interface.mainloop()

    #Return the user decision
    # return decision
























#Test the function
hand = ['J', 3, 'K'] #This will be the 4 extra cards you can use at any time
up1 = ['empty', 7, 8, 9] #This is the first 7 and up pile
up2 = ['empty'] #This is the second 7 and up pile
up3 = ['empty', 7, 8, 9, 10, 'J', 'Q'] #This is the third 7 and up pile
up4 = ['empty', 7] #This is the fourth 7 and up pile
down = ['empty', 6, 5, 4, 3, 2, 'A', 6, 5] #This is the center 6 and down pile
sixes = [6, 6] #The sixes pile off to the side
drawn_cards = [7, 9, 'Q'] #These are the cards drawn and kept from the deck each turn

# decision = display_cards(hand, up1, up2, up3, up4, down, sixes, drawn_cards)
display_cards(hand, up1, up2, up3, up4, down, sixes, drawn_cards)

# print(f"This given user decision is: {decision}")
