# Spider-Solitaire
This project creates the digital version of the card game Spider Solitaire.

Overview:
    Each time the game is played (the main function is run), a full deck of 52 cards is initiated. From here cards are dealt.
    Each iteration, the player is prompt if they would like to use one of their cards or draw a new card.
    This continues until the deck runs out of cards. At this time, the remaining cards on the table are automatically placed and
    the totals are calculated and presented to the player.

    The challenge of this project was to create the programming logic that we as humans take for granted when playing a card game.
    For example, teaching the computer that a Jack fits on top of a 10 is easy for a human but difficult in code.


This project uses many nested functions. These are listed below in parent/child order
    Main branch: main (file is spider_solitaire.py)
    Branch 2: gameplay - results
    Branch 3: user_decision - display_cards - finish_sorting
    Branch 4: card_2_math - down_placement - up_placement - move_card



 



To Improve:
    - Better user interface. This would be done by remaking the display cards function.
    - Can I tabulate the results using excel to track winnings over time? This would be done by remaking the results function.
