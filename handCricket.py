import random
import os
import time

#Some Inputs And Declarlization
playerScore = totalScore = leftScore = totalBalls = 0
playerName = str(input("Enter Your Name : "))
totalScore = int(input("Enter The Total Score : "))

#Game Start Function in for loop
for x in range(3,-1,-1):
        os.system('clear')
        print(f"Game Starts In {x}s.")
        time.sleep(1)
leftScore = totalScore
os.system('clear')
while True:
    computerBall = [0,1,2,3,4,5,6,7,8,9,10]
    random.shuffle(computerBall)
    computerBall = random.choice(computerBall)
    player = int(input("Enter Your Run >> "))

    #Checking For Player Balls and Computer Balls
    os.system('clear')
    if player == computerBall:
        print(f'Computer    : {computerBall} ')
        print(f'PlayerScore : {player}       ')
        print(f'Total Balls : {totalBalls}   ')
        print(f"\t {playerName} Has Out!!    ")
        break
    if player == 0:
        leftScore -= computerBall
        playerScore += computerBall
        totalBalls += 1
        print(f'{computerBall} is Added.')

    elif player >=1 and player <= 10:
        leftScore -= player
        playerScore += player
        totalBalls += 1
        print(f'{player} is Added.')
    else:
        pass

    #Checking for Player Score And Total Score For Winning Announce 
    if playerScore >= totalScore:
        print(f'\t\t{playerName} Has Won The Game!')
        print(f'Total Score : {totalScore}  ')
        break
    else:
        pass

    #Display 
    print(f'Total Score : {totalScore}  ')
    print(f'playerScore : {playerScore} ')
    print(f'Left Score  : {leftScore}   ')
    print(f'Total Balls : {totalBalls}  ')
