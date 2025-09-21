#This is a function that will calculate the results of the game and display it to the user

def results(up1, up2, up3, up4, down):
    '''
    This function will add up the total score from the game.
    Each card placed will be 1 point so the maximum total score is 52.
    This function will also edit the scores.csv file to add this game to all historical games.
    Inputs include the relevant piles (the ups and the down).
    Output includes the game_points from this game and the total money made over time (including this game).
    '''

    #Import libraries
    import csv
    from datetime import date

    #Make sure to subtract 1 from each deck because the first value will be "empty"
    length_up1 = len(up1) - 1
    length_up2 = len(up2) - 1
    length_up3 = len(up3) - 1
    length_up4 = len(up4) - 1
    length_down = len(down) - 1

    #Add up the total score for this game.
    game_points = length_up1 + length_up2 + length_up3 + length_up4 + length_down



    #Get today's date to add with the score from this game.
    todays_date = str(date.today())

    #Write this game's score to the scores.csv file
    with open("scores.csv", "a", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["date", "score"])
        writer.writerow({"date": todays_date, "score": game_points})


    #Calculate the all time total average score
    #Set the score and counter to 0 so the average historical score can be calculated.
    scores = 0
    counter = 0

    #Read the file
    with open("scores.csv", newline='') as file:
        #Use the dictReader to read the data.
        reader = csv.DictReader(file)
        #Loop through rows of data imported
        for row in reader:
            #Update the counter
            counter = counter + 1
            #Save each historical score and add it to the scores total
            row_score = int(row["score"])
            scores = scores + row_score #This will effectively find the total money made

    #Calculate the total money made / lost over time.
    total_money = round((scores - counter * 32) * 10, ndigits=1)
    

    #Return the total points from this game and the scores total found in the scores.csv
    return game_points, total_money












# #Test the function
# up1 = ['empty', 7, 8, 9, 10, 'J'] #This is the first 7 and up pile
# up2 = ['empty', 7, 8, 9, 10] #This is the second 7 and up pile
# up3 = ['empty', 7, 8, 9] #This is the third 7 and up pile
# up4 = ['empty', 7, 8] #This is the fourth 7 and up pile
# down = ['empty', 6, 5, 4, 3, 2, 'A', 6, 5, 4, 3, 2, 'A', 6, 5, 4, 3, 2] #This is the center 6 and down pile

# total_points, avg_score = results(up1, up2, up3, up4, down)
# print(f"This game's points were: {total_points}") #Should be 31 points
# print(f"Total points from all time are: {avg_score}")
