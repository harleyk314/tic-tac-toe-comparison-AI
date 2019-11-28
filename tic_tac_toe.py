import copy

wins = 0
losses = 0
draws = 0

mylist = []
evaluations = []
turns = []
evaluation = 0
lastEvalIndex = -1
#as some board states will not be assigned an evaluation immediately

maxEval = 0

startTurn = "AI"

while(True):

  A = [[0,0,0],[0,0,0],[0,0,0]]

  if (startTurn == "AI"):
    startTurn = "player"
    playerPiece = 1
    AIPiece = 2
  else:
    startTurn = "AI"
    playerPiece = 2
    AIPiece = 1

  turn = startTurn

  winner = "Undecided"

  while(winner == "Undecided"):
    if (turn == "player"):
      turnQuality = "invalid"
      while (turnQuality == "invalid"):
        if (turn == "player"):
          print()
          x = int(input("Choose an x co-ordinate: "))
          y = int(input("Choose a y co-ordinate: "))
        
          if (A[y][x] == 0):
            turnQuality = "valid"
            A[y][x] = playerPiece
          else:
            print()
            print("Invalid move, please try again.")
            print()
            print(A[0])
            print(A[1])
            print(A[2])

      #Now we check for rows

      if(A[1][1]==playerPiece):
        if(A[0][0]==playerPiece & A[2][2]==playerPiece):
          winner = "player"
        if(A[0][2]==playerPiece & A[2][0]==playerPiece):
          winner = "player"
        if(A[0][1]==playerPiece & A[2][1]==playerPiece):
          winner = "player"
        if(A[1][0]==playerPiece & A[1][2]==playerPiece):
          winner = "player"
      if(A[0][0]==playerPiece):
        if(A[0][1]==playerPiece & A[0][2]==playerPiece):
          winner = "player"
        if(A[1][0]==playerPiece & A[2][0]==playerPiece):
          winner = "player"
      if(A[2][2]==playerPiece):
        if(A[2][1]==playerPiece & A[2][0]==playerPiece):
          winner = "player"
        if(A[1][2]==playerPiece & A[0][2]==playerPiece):
          winner = "player"
      if (winner == "Undecided"):
        turn = "AI"

      if (winner == "Undecided"):
        keepSearching = True
        for i in range (3):
          for j in range (3):
            if (A[i][j] == 0):
              keepSearching = False
              break
        if (keepSearching == True):
          winner = "draw"
          turn = "null"
      print()
      print(A[0])
      print(A[1])
      print(A[2])
      mylist.append(copy.deepcopy(A))
      evaluations.append(0)
      #we know turn = player
      if (startTurn == "player"):
        #represents player 1's turn
        turns.append(1)
      else:
        turns.append(2)


    bestEval = -999999999

    if (turn == "AI"):
      for i in range (3):
        for j in range (3):
          if(A[i][j] == 0):
            #for each possible move
            evaluation = 0

            B = copy.deepcopy(A)
            #create a copy of the A array

            B[i][j] = AIPiece

            for k in range (len(mylist)):
              #for each comparable array
              if((startTurn=="AI" and turns[k]==1)or(startTurn=="player" and turns[k]==2)):
                evalFactor = 1
                C = copy.deepcopy(mylist[k])
                #C is the matrix to compare to
                for a in range(3):
                  for b in range(3):
                    if (B[a][b] != C[a][b]):
                      evalFactor = evalFactor/2.01
                evaluation += evalFactor * evaluations[k]
              else:
                evalFactor = -1 #should be -1
                C = copy.deepcopy(mylist[k])
                for a in range(3):
                  for b in range(3):
                    if (C[a][b]==1):
                      C[a][b]=2
                    elif (C[a][b]==2):
                      C[a][b]=1
                #C is the matrix to compare to
                for a in range(3):
                  for b in range(3):
                    if (B[a][b] != C[a][b]):
                      evalFactor = evalFactor/2.01
                evaluation += evalFactor * evaluations[k]
              
            #after k iterations we now have the evaluation for that hypothetical move
            if (startTurn == "player"): #also double check
              evaluation = -evaluation
            #print(evaluation)
            if (evaluation > bestEval):
              bestEval = evaluation
              bestX = i
              bestY = j
      A[bestX][bestY] = AIPiece

      #Now we check for rows

      if(A[1][1]==AIPiece):
        if(A[0][0]==AIPiece & A[2][2]==AIPiece):
          winner = "AI"
        if(A[0][2]==AIPiece & A[2][0]==AIPiece):
          winner = "AI"
        if(A[0][1]==AIPiece & A[2][1]==AIPiece):
          winner = "AI"
        if(A[1][0]==AIPiece & A[1][2]==AIPiece):
          winner = "AI"
      if(A[0][0]==AIPiece):
        if(A[0][1]==AIPiece & A[0][2]==AIPiece):
          winner = "AI"
        if(A[1][0]==AIPiece & A[2][0]==AIPiece):
          winner = "AI"
      if(A[2][2]==AIPiece):
        if(A[2][1]==AIPiece & A[2][0]==AIPiece):
          winner = "AI"
        if(A[1][2]==AIPiece & A[0][2]==AIPiece):
          winner = "AI"
      if (winner == "Undecided"):
        turn = "player"

      if (winner == "Undecided"):
        keepSearching = True
        for i in range (3):
          for j in range (3):
            if (A[i][j] == 0):
              keepSearching = False
              break
        if (keepSearching == True):
          winner = "draw"
          turn = "null"
      print()
      print(A[0])
      print(A[1])
      print(A[2])
      mylist.append(copy.deepcopy(A))
      evaluations.append(0)
      #we know turn = AI
      if (startTurn == "AI"):
        #represents player 1's turn
        turns.append(1)
      else:
        turns.append(2)
    


  print()
  print(len(mylist))
  if(winner == "player"):
    losses += 1
    print("You win!")

    if (startTurn == "player"):
      #player 1 won so all evaluations are positive
      evaluationReflector = 1
    else:
      #player 2 won so all evaluations are negative
      evaluationReflector = -1

  elif (winner == "AI"):
    wins += 1
    print("AI wins!")

    if (startTurn == "player"):
      #player 2 won so all evaluations are negative
      evaluationReflector = -1
    else:
      #player 1 won so all evaluations are positive
      evaluationReflector = 1
  else:
    print("It's a tie!")
    print()

  if (winner == "draw"):
    #delete recent board evaluations and states
    draws += 1
    #lastEvalIndex = len(mylist) - 1
    index = len(mylist) - 1
    
    while (index > lastEvalIndex):
      evaluations.pop()
      mylist.pop()
      turns.pop()
      index -= 1

  else:
    index = len(mylist) - 1
    #create board evaluations
    divider = 1
    while (index > lastEvalIndex):
      evaluations[index] = evaluationReflector/divider
      divider += 1
      index -= 1
    lastEvalIndex = len(mylist) - 1
  

  for i in range(len(mylist)):
    print()
    print(mylist[i][0])
    print(mylist[i][1])
    print(mylist[i][2])
    print(evaluations[i])
    print(turns[i])
  

  print()
  print("Length of array: " + str(len(mylist)))
  print("AI: " + str(wins))
  print("Player: " + str(losses))
  print("Draws: " + str(draws))
