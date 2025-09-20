#This is a function that will calculate the results of the game and display it to the user

def results(up1, up2, up3, up4, down):
    '''
    This function will add up the total score from the game
    Each card placed will be 1 point so the maximum total score is 52
    Inputs include the relevant piles (the ups and the down).
    Output includes the total_points.
    '''

    #Make sure to subtract 1 from each deck because the first value will be "empty"
    length_up1 = len(up1) - 1
    length_up2 = len(up2) - 1
    length_up3 = len(up3) - 1
    length_up4 = len(up4) - 1
    length_down = len(down) - 1

    #Add up the totals
    total_points = length_up1 + length_up2 + length_up3 + length_up4 + length_down

    #Return the total points
    return total_points
