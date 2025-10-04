

def card_images(card):
    '''
    This function will create the library of card images to help the UI display the proper card.
    if card is input as 0, the backside of a card image will be given.
    Inputs include the card desired (given as a card number or A, J, Q, K).
    Outputs include the correct image associated.
    '''

    #Import the needed libraries
    import customtkinter
    from PIL import Image, ImageTk

    #Import the image associated with each card
    if card == 'A':
        #Import the needed images
        card_image = customtkinter.CTkImage(light_image=Image.open("card_images/AH.png"), size=(40, 80))
    elif card == 2:
        #Import the needed images
        card_image = customtkinter.CTkImage(light_image=Image.open("card_images/2H.png"), size=(40, 80))
    elif card == 3:
        #Import the needed images
        card_image = customtkinter.CTkImage(light_image=Image.open("card_images/3H.png"), size=(40, 80))
    elif card == 4:
        #Import the needed images
        card_image = customtkinter.CTkImage(light_image=Image.open("card_images/4H.png"), size=(40, 80))
    elif card == 5:
        #Import the needed images
        card_image = customtkinter.CTkImage(light_image=Image.open("card_images/5H.png"), size=(40, 80))
    elif card == 6:
        #Import the needed images
        card_image = customtkinter.CTkImage(light_image=Image.open("card_images/6H.png"), size=(40, 80))
    elif card == 7:
        #Import the needed images
        card_image = customtkinter.CTkImage(light_image=Image.open("card_images/7H.png"), size=(40, 80))
    elif card == 8:
        #Import the needed images
        card_image = customtkinter.CTkImage(light_image=Image.open("card_images/8H.png"), size=(40, 80))
    elif card == 9:
        #Import the needed images
        card_image = customtkinter.CTkImage(light_image=Image.open("card_images/9H.png"), size=(40, 80))
    elif card == 10:
        #Import the needed images
        card_image = customtkinter.CTkImage(light_image=Image.open("card_images/10H.png"), size=(40, 80))
    elif card == 'J':
        #Import the needed images
        card_image = customtkinter.CTkImage(light_image=Image.open("card_images/JH.png"), size=(40, 80))
    elif card == 'Q':
        #Import the needed images
        card_image = customtkinter.CTkImage(light_image=Image.open("card_images/QH.png"), size=(40, 80))
    elif card == 'K':
        #Import the needed images
        card_image = customtkinter.CTkImage(light_image=Image.open("card_images/KH.png"), size=(40, 80))

    #If the card is not found, return the back of card image. When desired, input the card as 0
    else:
        card_image = customtkinter.CTkImage(light_image=Image.open("card_images/gray_back.png"), size=(40, 80))



    #Return the card image
    return card_image

