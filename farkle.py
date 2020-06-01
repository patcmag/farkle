import tkinter as tk
import validate_roll
import time
# import random
# import dieObject

margin = 20
w = 800
h = 600

root = tk.Tk()
root.geometry("800x600")

gui_current_score = tk.IntVar(0)
gui_turn_score = tk.IntVar(0)

gui_p1_score = tk.IntVar(0)
gui_p2_score = tk.IntVar(0)
gui_p3_score = tk.IntVar(0)
gui_scores=[gui_p1_score,gui_p2_score,gui_p3_score]
gui_player_scores = {'Player 1':gui_p1_score, 'Player 2':gui_p2_score, 'Player 3':gui_p3_score}
# playerScores = {'Player 1':0, 'p2':0, 'p3':0}

gui_player_labels = ['Player 1','Player 2','Player 3']
player_index = 0 #keeps track of current player
current_player = gui_player_labels[player_index]

rec1 = [x+100 for x in [20,10,100,90]]
rec2 = [x+100 for x in [20,100,100,180]]
rec3 = [x+100 for x in [20,190,100,270]]
rec4 = [x+100 for x in [170,10,250,90]]
rec5 = [x+100 for x in [170,100,250,180]]
rec6 = [x+100 for x in [170,190,250,270]]
recList = [rec1,rec2,rec3,rec4,rec5,rec6]

dice_dict = {}
dieObject_list = []
current_score = 0
turn_score = 0
active_dice = 6
farkled = False
notInheriting = False



def nextPlayer():
    global player_index
    global current_player
    player_index = player_index + 1
    if player_index == len(gui_player_labels): player_index = 0
    current_player = gui_player_labels[player_index]


def create_game_space(r):
    gs = tk.Frame(r,width=w,height=h)
    gs.place(x=0,y=0)
    canvas = tk.Canvas(gs,width=w,height=h,name="gs_canvas")
    canvas.place(x=0,y=0)
    canvas.create_rectangle(margin,margin,w-margin,h-margin)
    tk.Label(gs,text='Most recent roll scored: ').place(x=400,y=400)
    tk.Label(gs,textvariable=str(gui_current_score)).place(x=650,y=400)
    tk.Label(gs,text='Current score for this turn: ').place(x=400,y=450)
    tk.Label(gs,textvariable=str(gui_turn_score)).place(x=650,y=450)
    i=0
    for p in gui_player_labels:
        y_val = 400+(i*50)
        tk.Label(gs,text=p).place(x=100,y=y_val)
        tk.Label(gs,textvariable=str(gui_scores[i])).place(x=250,y=y_val)
        i=i+1
    return gs

def inheritDice(event):
    # print 'inheritDice called'
    root.bind("<Return>",playerTurn)
    root.event_generate("<Return>")

def doNotInheritDice(event):
    # print 'doNotInheritDice called'
    global notInheriting
    notInheriting = True
    root.bind("<Return>",playerTransition)
    root.event_generate("<Return>")

def playerTransition(event):
    print '\nplayerTransition was called\tnotInheriting = ' + str(notInheriting)
    global turn_score
    global gui_player_scores
    global current_player

    if farkled or notInheriting:
        global active_dice
        active_dice = 6
        global current_score
        current_score = 0
        gui_current_score.set(0)
        turn_score = 0
        gui_turn_score.set(0)
        global notInheriting
        notInheriting = False
        root.bind("<Return>",playerTurn)
        root.event_generate("<Return>") #goes back to playerTurn
    else: #if no farkle, next player can keep the current dice or start with fresh dice
        gui_player_scores[current_player].set(gui_player_scores[current_player].get() + turn_score) #BANK POINTS
        nextPlayer()
        message = tk.Label(game_space,text=current_player + ", keep these dice? (Y/N)",bg="white")
        message.place(x=400,y=110,width=250,height=200)
        root.bind('y',inheritDice)
        root.bind('n',doNotInheritDice)


def validateSelection(event):
    print '\nvalidateSelection was called'
    global dieObject_list
    dice_to_keep = []
    # print 'dice_to_keep: ' + str(dice_to_keep)
    for d in dieObject_list:
        if d.get_selected_status() == True: dice_to_keep.append(d.get_dieID())
    print 'dice_to_keep: ' + str(dice_to_keep)
    
    #create list of rolled values to tabulate score for this roll
    global dice_dict
    print 'dice_dict: ' + str(dice_dict)
    scoreList = [dice_dict[die] for die in dice_to_keep]
    print 'scoreList: ' + str(scoreList)
    scoreList_IsValid = validate_roll.isValid([str(s) for s in scoreList])
    print 'scoreList_IsValid:' + str(scoreList_IsValid)

    if not scoreList_IsValid:
        print 'selection not valid'
        print 'scoreList = ' + str(scoreList)
        print 'turn_dice_dict: ' + str(turn_dice_dict)
        print 'dice_to_keep: ' + str(dice_to_keep)
        message = tk.Label(game_space,text="Selection not valid, choose new dice to keep\nPress ENTER to continue",bg="white")
        message.place(x=400,y=110,width=350,height=200)
        root.bind('<Return>',validateSelection)

    else: #if scoreList_IsValid: 
        turn_dice_dict = dice_dict
        print 'turn_dice_dict: ' + str(turn_dice_dict)
        for die in dice_to_keep: del turn_dice_dict[die] #reduce available dice to roll for this turn
        print 'dice_to_keep: ' + str(dice_to_keep)
        import return_score

        global current_score
        current_score = return_score.return_score(scoreList)
        gui_current_score.set(current_score)
        global turn_score
        turn_score = turn_score + current_score
        gui_turn_score.set(turn_score)
        global active_dice
        active_dice = len(turn_dice_dict)

        if active_dice==0:
            print 'You get a fresh set of dice'
            message = tk.Label(game_space,text="You get a fresh set of dice\nPress ENTER to roll again",bg="white")
            message.place(x=400,y=110,width=200,height=200)
            active_dice = 6
            root.bind('<Return>',playerTurn)
        else:
            message = tk.Label(game_space,text="Continue to roll (Y/N)?",bg="white")
            message.place(x=400,y=110,width=200,height=200)
            root.bind('y',playerTurn)
            root.bind('n',playerTransition)

    
def playerTurn(event):
    global game_space
    game_space.destroy()
    game_space = create_game_space(root)
    global farkled
    farkled = False
    global active_dice
    dice = [0]*active_dice
    global dice_dict
    dice_dict = {}
    import random
    i = 1
    for d in dice: #get random dice values
        roll = random.randrange(1,7)
        dice_dict[str(i)] = roll
        i = i+1

    # global current_roll
    current_roll = [dice_dict[str(j)] for j in range(1,active_dice+1)] #values of dice just rolled
    active_dice_IDs = [str(id) for id in range(1,active_dice+1)] #IDs (1-6) of dice just rolled

    # debug troublesome rolls - define current_roll
    # current_roll = [1,5,1,5,5,1]
    # active_dice_IDs = ['1','2','3','4','5','6']
    # r=0
    # for d_id in active_dice_IDs:
    #     dice_dict[d_id] = current_roll[r]
    #     r=r+1

    import dieObject
    global dieObject_list #holds refs to GUI dice objects
    dieObject_list = []
    i=0
    for id in active_dice_IDs: #visualize dice in GUI
        #create Die() instance and add to the dieObject_list
        #the die is drawn on game_space child canvas called gs_canvas
        dieObject_list.append(dieObject.Die(game_space.nametowidget("gs_canvas"), id, dice_dict[id], *recList[i]))
        i=i+1

    #FARKLE TEST 
    if validate_roll.farkled(current_roll):
        message = tk.Label(game_space,text="F A R K L E\nPress ENTER to continue",bg="white")
        message.place(x=400,y=110,width=200,height=200)
        farkled = True
        nextPlayer()
        root.bind('<Return>',playerTransition)
    else:
        message = tk.Label(game_space,text=current_player + ", select dice to keep\nPress ENTER to continue",bg="white")
        message.place(x=400,y=110,width=200,height=200)
        root.bind('<Return>',validateSelection)    


def startGame(event):
    global game_space
    game_space.destroy()
    game_space = create_game_space(root)
    message = tk.Label(game_space,text=current_player + ", press ENTER to roll dice",bg="pink")
    message.place(x=(w/2)-200,y=(h/2)-30,width=400,height=60)
    root.bind('<Return>',playerTurn)


def quitGame(event): 
    quit()

game_space = create_game_space(root)
welcomeMessage = tk.Label(game_space,text="Welcome to Farkle\tPress ENTER to play",bg="light blue")
welcomeMessage.place(x=(w/2)-200,y=(h/2)-30,width=400,height=60)

root.bind('<Return>',startGame)
root.bind('q',quitGame)
root.mainloop()