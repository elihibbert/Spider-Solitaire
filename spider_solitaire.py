#This is the masterfile to play the spider solitaire game. Functionality will be written in different files.
 

#Run main function
def main():
    '''
    This is the main function at the head of the spider solitaire game
    The nested gameplay function operates through the game.
    The nested results function displays the users winnings and losings.
    This function takes no inputs and produces no outputs but prints how much money was made/lost.
    '''
    
    #Import functions
    from gameplay import gameplay
    from results import results

    
    #Run the gameplay function. return all the decks
    up1, up2, up3, up4, down = gameplay()

    #Display the results. input all the decks, return the total score.
    total_points = results(up1, up2, up3, up4, down)

    #Calculate the winnings based upon the total points. Each point is $10. $320 is the cost to play so each point more than 32 is $10 winnings.
    money = (total_points - 32) * 10

    #Print the results to the player
    print()
    print("----------------------------------------")
    if total_points >= 32:
        print(f"Good Game! You made ${money:.2f} this game.")
    else:
        negative_money = money * -1
        print(f"Better luck next time. You lost ${negative_money:.2f} this game.")



#Run the main function
if __name__ == "__main__":
    main()