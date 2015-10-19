## Program Assignment: 2
## Program Title: Baseball
## Program Description: This program asks for a team name,
##      number of games won, and number of games lost as input.   
##      It outputs the percentage of games won.

teamName = input("Enter the name of your favorite baseball team: ")
gamesWon = eval(input("How many games did they win? "))
gamesLost = eval(input("How many games did they lose? "))
totalGames = (gamesWon + gamesLost)
answer = round((gamesWon / totalGames) * 100, 2)

print("The " + teamName + " won " + str(answer) + "%" + " of their games.")
