# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, 
# print out a message of congratulations to the winner, and ask if the players want to start a new game)
#Remember the rules:

# Rock beats scissors          Rock > scissors
# Scissors beats paper         Scissors > paper
# Paper beats rock             Paper > Rock





player1Counter = 0
player2Counter = 0

possiblechoice = ['rock','scissors','paper']

while True :
    player1 = input('Please write your choice (Player 1)\n')
    player2 = input('Please write your choice (Player 2)\n')
    
    if player1 == possiblechoice and player2 == possiblechoice:

        #player1's choice rock situation
        if player1 == 'rock':
            if player2 == 'rock':
                print('Round is tie')
        if player1 == 'rock':
            if player2 == 'paper':
                print('Won player 2')
                player2Counter +=1
                print(player2Counter)
        if player1 == 'rock':
            if player2 == 'scissors':
                print('Won player 1')
                player1Counter +=1
                print(player1Counter)
        #player1's choice paper situation
        if player1 == 'paper':
            if player2 == 'rock':
                print('Won player 1')
                player1Counter +=1
        if player1 == 'paper':
            if player2 == 'paper':
                print('Round is tie')
        if player1 == 'paper':
            if player2 == 'scissors':
                print('Won player 2')
                player2Counter +=1
        #player1's choice scissors situation
        if player1 == 'scissors':
            if player2 == 'rock':
                print('Won player 2')
                player2Counter +=1
        if player1 == 'scissors':
            if player2 == 'paper':
                print('Won player 1')
                player1Counter +=1
        if player1 == 'scissors':
            if player2 == 'scissors':
                print('Round is tie')
        
        
        if player1Counter == 3 or player2Counter == 3:
            print('Match is over ')
            if player1Counter > player2Counter:
                print('Winner Player 1')
            else:
                print('Winner Player 2')
            break
    else:
        print('You can choose rock,scissors,paper')
        break