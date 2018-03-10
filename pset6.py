#--------------------------- Helper Code ------------------------------#
import string

WORDLIST_FILENAME = "words.txt"
def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
##    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
##    print "  ", len(wordlist), "words loaded."
    return wordlist
#------------------------ end of Helper Code ---------------------------#

#-----------------------Create Players--------------------------------#
def createPlayers():
    """Asks for number of players and returns a dict of player details"""
    while True:
        try:
            num_players = abs(int(raw_input("How many players?: ")))
            if num_players == 0:
                raise ValueError
            break
        except KeyboardInterrupt:
            raise KeyboardInterrupt
        except ValueError:
            print "Invalid input"

    players = {}
    for player_key in xrange(1,num_players+1):
        players[player_key] = players.get(player_key,0)
    return players
#-----------------------------------------------------------------------#

#-----------------------Fragment search engine--------------------------#
def fragment_search_engine(search_frag,word_list,low,high):
    count = 0
    frag_found,high_found = False,None
    reset = {}
    while True and count < 100:
        middle = (low + high)/2
        count+=1
        if search_frag < word_list[middle][:len(search_frag)]: high = middle
        elif search_frag > word_list[middle][:len(search_frag)]: low = middle
        elif search_frag == word_list[middle] and len(search_frag) > 3:
            return False,"a Complete word"
        elif search_frag == word_list[middle][:len(search_frag)]:
            frag_found = True
            reset['high'] = reset.get('high',high)
            reset['low'] = reset.get('low',low)
            if not high_found:
                try:
                    next_word_frag = word_list[middle+1][:len(search_frag)]
                except IndexError:
                    next_word_frag = None
                if search_frag != next_word_frag:
                    high_found = middle
                    high = reset['high']
                    low = reset['low']
                else:
                    low = middle
            else:
                if search_frag != word_list[middle-1][:len(search_frag)]:
                    return low,high_found
                else:
                    high = middle
        if high - low < 2:
            if high > len(word_list) - 1: high = len(word_list) - 1
            if word_list[high][:len(search_frag)] == search_frag and not high_found:
                frag_found = True
                low = high
            if not frag_found:
                return False,"an Invalid Fragment"
    return False,low,middle,high,count
#----------------------------------------------------------------------------------#

#----------------------Get New Fragment ----------------------------------#
def getNewFrag(current_frag):
    """Returns new fragment. output is lowercase"""
    while True:
        player_input = raw_input("  Enter a letter: ")
        print
        if player_input in string.ascii_letters and len(player_input) == 1:
            return current_frag + player_input.lower()
        print " !!'" + player_input + "' not a valid input!!"
#------------------------------------------------------------------------#

#--------------------------Penalise Player--------------------------------#
def penalisePlayer(player,active_players,rounds):
    """Function called when a player loses a round.
    adds a +1 until player becomes ghost"""
    ghost_players = {}
    active_players[player] += 1
    if active_players[player] == len('ghost'):##
        ghost_players[player] = ghost_players.get(player,rounds)
        del active_players[player]
        print "  Boom! you are now a ghost"
        return ghost_players
    print "  Your status is: " + 'ghost'[:active_players[player]]
    return None
#------------------------------------------------------------------------#

##make it a function that returns useful info
def gameplay():
    print "\n\t\t\t - Welcome to GHOST WORDGAME -\n"
    ##Necessary Variable:
    word_list = load_words()
    #memory or perfomance
    active_players = createPlayers()

    game_round,game_over = 1,False
    current_frag = ""
    low_high = [0,len(word_list)]
    while True:
        ##turns
        for player in active_players.keys():
            print "\n  ROUND",game_round
            print "  Player %i's Turn" % player
            print " ","~"*15
            print "  Current fragment is: '" + current_frag.lower() + "'"
            current_frag = getNewFrag(current_frag)
            #check fragment
            low = low_high[0]
            high = low_high[1]
            low_high = fragment_search_engine(current_frag,word_list,low,high)
            if type(low_high[0]) != int:
                print "  !!'"+current_frag+"' is "+low_high[1]+"!!"
                ##The last round a player got penalised
                ##the lower the better? if active
                #--------Penalise Here-----------#
                ghosts = penalisePlayer(player,active_players,game_round)
                #--------------------------------#
                #---------Reset Round------------#
                if game_round == 7:
                    game_over = True
                    break                
                game_round += 1
                current_frag = ""
                low_high = [0,len(word_list)]
                #---------------------------------#
            else:
                print "  '" + current_frag + "'" + ": ok"
        if game_over or len(active_players) == 0: break
    print "-"*51
    print "  Game Over"
    print "  Survivors:",active_players
    print "  Ghosts:",ghosts

gameplay()
