#This file will create the classes used in the V2 display_cards function.

#Import the built in Python library for applications
from tkinter import ttk
import customtkinter
from PIL import Image, ImageTk
from card_images import card_images





#Create a re-useable parent class to build the application
class Application(customtkinter.CTk):
    #Import all the piles to be used
    def __init__(self, hand, up1, up2, up3, up4, down, sixes, drawn_cards):
        #Pull the init function from the tk library to use in my application
        super().__init__()

        #Save all the decks into the class to use for later
        self.hand = hand
        self.up1 = up1
        self.up2 = up2
        self.up3 = up3
        self.up4 = up4
        self.down = down 
        self.sixes = sixes
        self.drawn_cards = drawn_cards

        #Name the application
        self.title("Spider Solitaire")

        #This makes the root take up all the space when the window is expanded.
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        #Create one frame. The card piles will be divided by buttons within the same frame.
        frame = FrameButtons(self)
        frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        


        



#Create a child class to build the frame with all the cards
class FrameButtons(ttk.Frame):

    def __init__(self, parent):

        #Pull the init function from the Application class with all the attributes
        super().__init__(parent)

        #Allow each card pile to expand evenly as the window is expanded (4 rows x 3 columns).
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)

        #Initialize the decision to 0
        self.decision = 0

        #-------------------CREATE THE DISPLAY BUTTONS--------------------------------
        #Create the up1 button
        print(up1)
        up1_card = card_images(up1[-1])
        self.up1_btn = customtkinter.CTkButton(master=self, image=up1_card, text="", width=80, height=40)
        self.up1_btn.grid(row=0, column=0)

        #Create the up2 button
        up2_card = card_images(up2[-1])
        self.up2_btn = customtkinter.CTkButton(master=self, image=up2_card, text="", width=80, height=40)
        self.up2_btn.grid(row=0, column=2)

        #Create the up3 button
        up3_card = card_images(up3[-1])
        self.up3_btn = customtkinter.CTkButton(master=self, image=up3_card, text="", width=80, height=40)
        self.up3_btn.grid(row=2, column=0)

        #Create the up4 button
        up4_card = card_images(up4[-1])
        self.up4_btn = customtkinter.CTkButton(master=self, image=up4_card, text="", width=80, height=40)
        self.up4_btn.grid(row=2, column=2)

        #Create the down button
        down_card = card_images(down[-1])
        self.down_btn = customtkinter.CTkButton(master=self, image=down_card, text="", width=80, height=40)
        self.down_btn.grid(row=1, column=1)



        #-------------------CREATE THE FUNCTIONAL BUTTONS--------------------------------
        #Create the hand card pile #1 (funtionality included, return decision = 2)
        try:
            hand_card_1_image = card_images(hand[0])
        except IndexError:
            hand_card_1_image = card_images(0)
        self.hand_card_1_btn = customtkinter.CTkButton(master=self, image=hand_card_1_image, text="", width=80, height=40, command=self.use_hand_card)
        self.hand_card_1_btn.grid(row=0, column=1)

        #Create the hand card pile #2 (funtionality included, return decision = 2)
        try:
            hand_card_2_image = card_images(hand[1])
        except IndexError:
            hand_card_2_image = card_images(0)
        self.hand_card_2_btn = customtkinter.CTkButton(master=self, image=hand_card_2_image, text="", width=80, height=40, command=self.use_hand_card)
        self.hand_card_2_btn.grid(row=1, column=0)

        #Create the hand card pile #3 (funtionality included, return decision = 2)
        try:
            hand_card_3_image = card_images(hand[2])
        except IndexError:
            hand_card_3_image = card_images(0)
        self.hand_card_3_btn = customtkinter.CTkButton(master=self, image=hand_card_3_image, text="", width=80, height=40, command=self.use_hand_card)
        self.hand_card_3_btn.grid(row=1, column=2)

        #Create the hand card pile #4 (funtionality included, return decision = 2)
        try:
            hand_card_4_image = card_images(hand[3])
        except IndexError:
            hand_card_4_image = card_images(0)
        self.hand_card_4_btn = customtkinter.CTkButton(master=self, image=hand_card_4_image, text="", width=80, height=40, command=self.use_hand_card)
        self.hand_card_4_btn.grid(row=2, column=1)

        #Create the deck pile (funtionality included, return decision = 4)
        card_back_image = card_images(0)
        self.deck_btn = customtkinter.CTkButton(master=self, image=card_back_image, text="Deck", width=80, height=40, command=self.use_deck)
        self.deck_btn.grid(row=3, column=0)

        #Create the drawn cards pile (funtionality included, return decision = 1)
        try:
            drawn_cards_image = card_images(drawn_cards[-1])
        except IndexError:
            drawn_cards_image = card_images(0)
        self.drawn_cards_btn = customtkinter.CTkButton(master=self, image=drawn_cards_image, text="Drawn Card", width=80, height=40, command=self.use_drawn_cards)
        self.drawn_cards_btn.grid(row=3, column=1)

        #Create the sixes pile (funtionality included, return decision = 3)
        try:
            sixes_image = card_images(sixes[-1])
        except IndexError:
            sixes_image = card_images(0)
        self.sixes_btn = customtkinter.CTkButton(master=self, image=sixes_image, text="Sixes", width=80, height=40, command=self.use_sixes)
        self.sixes_btn.grid(row=3, column=2)







    #Create the function to use a hand card
    def use_hand_card(self):
        self.decision = 2 #How can I reset this variable then change it each iteration?
        # print(f"The desicion variable is now: {self.decision}")

    #Create the function to draw a new card from the deck
    def use_deck(self):
        self.decision = 4 #How can I reset this variable then change it each iteration?

    #Create the function to use the most recent drawn card
    def use_drawn_cards(self):
        self.decision = 1

    #Create the function to use a six
    def use_sixes(self):
        self.decision = 3


    #Create an application wide function that will return the decision variable and run when the decision is changed.
    def user_decision(self):
        return self.decision
    
    if self.decision == 1 or self.decision == 2 or self.decision == 3 or self.decision == 4:
        user_decision()
    













#Test the application
hand = ['J', 3, 'K'] #This will be the 4 extra cards you can use at any time
up1 = ['empty', 7, 8, 9] #This is the first 7 and up pile
up2 = ['empty'] #This is the second 7 and up pile
up3 = ['empty', 7, 8, 9, 10, 'J', 'Q'] #This is the third 7 and up pile
up4 = ['empty', 7] #This is the fourth 7 and up pile
down = ['empty', 6, 5, 4, 3, 2, 'A', 6, 5] #This is the center 6 and down pile
sixes = [6, 6] #The sixes pile off to the side
drawn_cards = [7, 9, 'Q'] #These are the cards drawn and kept from the deck each turn

app = Application(hand, up1, up2, up3, up4, down, sixes, drawn_cards)
app.mainloop()