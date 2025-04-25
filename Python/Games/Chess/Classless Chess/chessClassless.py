board = [["br","bn","bb","bq","bk","bb","bn","br"],
         ["bp" for x in range(0,8)],
         ["__" for x in range(0,8)],
         ["__" for x in range(0,8)],
         ["__" for x in range(0,8)],
         ["__" for x in range(0,8)],
         ["wp" for x in range(0,8)],
         ["wr","wn","wb", "wq","wk","wb","wn","wr"]]
def artifyBoard(ChessBoard):
    boardArt = [[" ","a ", "b ", "c ", "d ", "e ", "f ", "g ", "h "],
            ["1"],
            ["2"],
            ["3"],
            ["4"],
            ["5"],
            ["6"],
            ["7"],
            ["8"]
            ]
    displayBoard = []
    for i in boardArt:
        displayBoard.append(i)
    for i,k in enumerate(ChessBoard):
        for j in k:
            displayBoard[i+1].append(j)
    return displayBoard
def displayCurrentBoard(ChessBoard):
    for i in artifyBoard(ChessBoard):
        print(i)
def selectionToPiece(selection):
    listSelect = [selection[0],selection[1]]
    match listSelect[0]:
        case "a":
            listSelect[0] = 0
        case "b":
            listSelect[0] = 1
        case "c":
            listSelect[0] = 2
        case "d":
            listSelect[0] = 3
        case "e":
            listSelect[0] = 4
        case "f":
            listSelect[0] = 5
        case "g":
            listSelect[0] = 6
        case "h":
            listSelect[0] = 7
        case _:
            listSelect = [0,0]
    try:
        return [int(listSelect[1])-1,int(listSelect[0])]
    except:
        return "BadSelection"
def ListToAlg(selection):
    #[0,0] = "a1", [2,3] = "c2"
    algNot = ""
    match selection[1]:
        case 0:
            algNot = algNot + "a"
        case 1:
            algNot = algNot + "b"
        case 2:
            algNot = algNot + "c"
        case 3:
            algNot = algNot + "d"
        case 4:
            algNot = algNot + "e"
        case 5:
            algNot = algNot + "f"
        case 6:
            algNot = algNot + "g"
        case 7:
            algNot = algNot + "h"
        case _:
            algNot = "BadSelection"
    return algNot + str(selection[0]+1)
def checkMoves(ChessBoard,selection):
    #User Input in algebraic chess notation for the piece they intend to move
    selected = selectionToPiece(selection)
    if selected != "BadSelection":
        possibleMoves = []
        match ChessBoard[selected[0]][selected[1]]:
            case "__":
                return"BadSelection"
            case "wp":
                if selected[0] == 6:
                    if ChessBoard[selected[0]-1][selected[1]] == "__":
                        possibleMoves.append(ListToAlg([selected[0]-1,selected[1]]))
                    if ChessBoard[selected[0]-2][selected[1]] == "__" and ChessBoard[selected[0]-1][selected[1]] == "__":
                        possibleMoves.append(ListToAlg([selected[0]-2,selected[1]]))
                else:
                    if ChessBoard[selected[0]-1][selected[1]] == "__":
                        possibleMoves.append(ListToAlg([selected[0]-1,selected[1]]))
                if selected[1] > 0 and selected[1] < 7 and selected[0]>0:
                    if ChessBoard[selected[0]-1][selected[1]-1] != "__" and ChessBoard[selected[0]-1][selected[1]-1][0] != "w":
                        possibleMoves.append(ListToAlg([selected[0]-1,selected[1]-1]))
                    if ChessBoard[selected[0]-1][selected[1]+1] != "__" and ChessBoard[selected[0]-1][selected[1]+1][0] != "w":
                        possibleMoves.append(ListToAlg([selected[0]-1,selected[1]+1]))
                elif selected[1] == 0 and selected[0]>0:
                    if ChessBoard[selected[0]-1][selected[1]+1] != "__" and ChessBoard[selected[0]-1][selected[1]+1][0] != "w":
                        possibleMoves.append(ListToAlg([selected[0]-1,selected[1]+1]))
                elif selected[1] == 7 and selected[0]>0:
                    if ChessBoard[selected[0]-1][selected[1]-1] != "__" and ChessBoard[selected[0]-1][selected[1]-1][0] != "w":
                        possibleMoves.append(ListToAlg([selected[0]-1,selected[1]-1]))
            case "bp":
                if selected[0] == 1:
                    if ChessBoard[selected[0]+1][selected[1]] == "__":
                        possibleMoves.append(ListToAlg([selected[0]+1,selected[1]]))
                    if ChessBoard[selected[0]+2][selected[1]] == "__" and ChessBoard[selected[0]+1][selected[1]] == "__":
                        possibleMoves.append(ListToAlg([selected[0]+2,selected[1]]))
                else:
                    if ChessBoard[selected[0]+1][selected[1]] == "__":
                        possibleMoves.append(ListToAlg([selected[0]+1,selected[1]]))
                if selected[1] > 0 and selected[1] < 7 and selected[0]>0:
                    if ChessBoard[selected[0]+1][selected[1]-1] != "__" and ChessBoard[selected[0]+1][selected[1]-1][0] != "b":
                        possibleMoves.append(ListToAlg([selected[0]+1,selected[1]-1]))
                    if ChessBoard[selected[0]+1][selected[1]+1] != "__" and ChessBoard[selected[0]+1][selected[1]+1][0] != "b":
                        possibleMoves.append(ListToAlg([selected[0]+1,selected[1]+1]))
                elif selected[1] == 0 and selected[0]<7:
                    if ChessBoard[selected[0]+1][selected[1]+1] != "__" and ChessBoard[selected[0]+1][selected[1]-1][0] != "b":
                        possibleMoves.append(ListToAlg([selected[0]+1,selected[1]+1]))
                elif selected[1] == 7 and selected[0]>0:
                    if ChessBoard[selected[0]+1][selected[1]-1] != "__" and ChessBoard[selected[0]+1][selected[1]-1][0] != "b":
                        possibleMoves.append(ListToAlg([selected[0]+1,selected[1]-1]))
            case "wr":
                Counter = 1
                hitFlag = True
                while hitFlag and selected[0]-Counter >=0:
                    if ChessBoard[selected[0]-Counter][selected[1]] == "__":
                        possibleMoves.append(ListToAlg([selected[0]-Counter,selected[1]]))
                    elif ChessBoard[selected[0]-Counter][selected[1]][0] == "b":
                        possibleMoves.append(ListToAlg([selected[0]-Counter,selected[1]]))
                        hitFlag = False
                    else:
                        hitFlag = False
                    Counter += 1
                Counter = 1
                hitFlag = True
                while hitFlag and selected[0]+Counter <=7:
                    if ChessBoard[selected[0]+Counter][selected[1]] == "__":
                        possibleMoves.append(ListToAlg([selected[0]+Counter,selected[1]]))
                    elif ChessBoard[selected[0]+Counter][selected[1]][0] == "b":
                        possibleMoves.append(ListToAlg([selected[0]+Counter,selected[1]]))
                        hitFlag = False
                    else:
                        hitFlag = False
                    Counter += 1
                Counter = 1
                hitFlag = True
                while hitFlag and selected[1]-Counter >=0:
                    if ChessBoard[selected[0]][selected[1]-Counter] == "__":
                        possibleMoves.append(ListToAlg([selected[0],selected[1]-Counter]))
                    elif ChessBoard[selected[0]][selected[1]-Counter][0] == "b":
                        possibleMoves.append(ListToAlg([selected[0],selected[1]-Counter]))
                        hitFlag = False
                    else:
                        hitFlag = False
                    Counter += 1
                Counter = 1
                hitFlag = True
                while hitFlag and selected[1]+Counter <= 7:
                    if ChessBoard[selected[0]][selected[1]+Counter] == "__":
                        possibleMoves.append(ListToAlg([selected[0],selected[1]+Counter]))
                    elif ChessBoard[selected[0]][selected[1]+Counter][0] == "b":
                        possibleMoves.append(ListToAlg([selected[0],selected[1]+Counter]))
                        hitFlag = False
                    else:
                        hitFlag = False
                    Counter += 1
            case "br":
                Counter = 1
                hitFlag = True
                while hitFlag and selected[0]-Counter >=0:
                    if ChessBoard[selected[0]-Counter][selected[1]] == "__":
                        possibleMoves.append(ListToAlg([selected[0]-Counter,selected[1]]))
                    elif ChessBoard[selected[0]-Counter][selected[1]][0] == "w":
                        possibleMoves.append(ListToAlg([selected[0]-Counter,selected[1]]))
                        hitFlag = False
                    else:
                        hitFlag = False
                    Counter += 1
                Counter = 1
                hitFlag = True
                while hitFlag and selected[0]+Counter <=7:
                    if ChessBoard[selected[0]+Counter][selected[1]] == "__":
                        possibleMoves.append(ListToAlg([selected[0]+Counter,selected[1]]))
                    elif ChessBoard[selected[0]+Counter][selected[1]][0] == "w":
                        possibleMoves.append(ListToAlg([selected[0]+Counter,selected[1]]))
                        hitFlag = False
                    else:
                        hitFlag = False
                    Counter += 1
                Counter = 1
                hitFlag = True
                while hitFlag and selected[1]-Counter >=0:
                    if ChessBoard[selected[0]][selected[1]-Counter] == "__":
                        possibleMoves.append(ListToAlg([selected[0],selected[1]-Counter]))
                    elif ChessBoard[selected[0]][selected[1]-Counter][0] == "w":
                        possibleMoves.append(ListToAlg([selected[0],selected[1]-Counter]))
                        hitFlag = False
                    else:
                        hitFlag = False
                    Counter += 1
                Counter = 1
                hitFlag = True
                while hitFlag and selected[1]+Counter <= 7:
                    if ChessBoard[selected[0]][selected[1]+Counter] == "__":
                        possibleMoves.append(ListToAlg([selected[0],selected[1]+Counter]))
                    elif ChessBoard[selected[0]][selected[1]+Counter][0] == "w":
                        possibleMoves.append(ListToAlg([selected[0],selected[1]+Counter]))
                        hitFlag = False
                    else:
                        hitFlag = False
                    Counter += 1
        return possibleMoves
    else:
        return "BadSelection"

displayCurrentBoard(board)
print(checkMoves(board,"a8"))