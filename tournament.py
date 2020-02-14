import random
import game
import agent
import alpha_beta_agent as aba


######################
# Play a single game #
######################

# Play a single game.
#
# PARAM [int]         w:  the board width
# PARAM [int]         h:  the board height
# PARAM [int]         n:  the number of tokens to line up to win
# PARAM [int]         l:  the time limit for a move in seconds
# PARAM [agent.Agent] p1: the agent for Player 1
# PARAM [agent.Agent] p2: the agent for Player 2
def play_game(w, h, n, l, p1, p2):
    g = game.Game(w,  # width
                  h,  # height
                  n,  # tokens in a row to win
                  p1,  # player 1
                  p2)  # player 2
    o = g.timed_go(l)
    print("    GAME:", p1.name, "vs.", p2.name, ": ", end='')
    if o == 0:
        print("tie")
    elif o == 1:
        print(p1.name, "won!")
    else:
        print(p2.name, "won!")
    return o


###########################################################
# Play a match between two players                        #
# Two games, with P1 and P2 inverted after the first game #
###########################################################

# Play a match.
#
# PARAM [int]         w:  the board width
# PARAM [int]         h:  the board height
# PARAM [int]         n:  the number of tokens to line up to win
# PARAM [int]         l:  the time limit for a move in seconds
# PARAM [agent.Agent] p1: the agent for Player 1
# PARAM [agent.Agent] p2: the agent for Player 2
def play_match(w, h, n, l, p1, p2):
    print("  MATCH:", p1.name, "vs.", p2.name)
    # Play the games
    o1 = play_game(w, h, n, l, p1, p2)
    o2 = play_game(w, h, n, l, p2, p1)
    # Calculate scores
    s1 = 0
    s2 = 0
    if o1 == 1:
        s1 = s1 + 1
        s2 = s2 - 1
    elif o1 == 2:
        s1 = s1 - 1
        s2 = s2 + 1
    if o2 == 1:
        s1 = s1 - 1
        s2 = s2 + 1
    elif o2 == 2:
        s1 = s1 + 1
        s2 = s2 - 1
    return (s1, s2)


####################################
# Play tournament and print scores #
####################################

# Play a tournament.
#
# PARAM [int]                 w:  the board width
# PARAM [int]                 h:  the board height
# PARAM [int]                 n:  the number of tokens to line up to win
# PARAM [int]                 l:  the time limit for a move in seconds
# PARAM [list of agent.Agent] ps: the agents in the tournament
def play_tournament(w, h, n, l, ps):
    print("TOURNAMENT START")
    # Initialize scores
    scores = {}
    for p in ps:
        scores[p] = 0
    # Play
    for i in range(0, len(ps) - 1):
        for j in range(i + 1, len(ps)):
            (s1, s2) = play_match(w, h, n, l, ps[i], ps[j])
            scores[ps[i]] = scores[ps[i]] + s1
            scores[ps[j]] = scores[ps[j]] + s2
    print("TOURNAMENT END")
    # Calculate and print scores
    sscores = sorted(((v, k.name) for k, v in scores.items()), reverse=True)
    print("\nSCORES:")
    for v, k in sscores:
        print(v, k)


#######################
# Run the tournament! #
#######################

# Set random seed for reproducibility
random.seed(1)

# Construct list of agents in the tournament
agents = [

    agent.InteractiveAgent("me", 1),

    # aba.AlphaBetaAgent("close2", 2, 0, -5),
    # aba.AlphaBetaAgent("close3", 3, 0, -5),
    # aba.AlphaBetaAgent("close4", 4, 0, -5),
    # aba.AlphaBetaAgent("close5", 5, 0, -5),
    # aba.AlphaBetaAgent("close6", 6, 0, -5),
    #aba.AlphaBetaAgent("close7", 7, 0, -5),
    aba.AlphaBetaAgent("close8", 8, 0, -5),
    aba.AlphaBetaAgent("close9", 9, 0, -5),
    aba.AlphaBetaAgent("close10", 10, 0, -5),
    #
    # aba.AlphaBetaAgent("far2", 2, 10, -5),
    # aba.AlphaBetaAgent("far3", 3, 10, -5),
    # aba.AlphaBetaAgent("far4", 4, 10, -5),
    # aba.AlphaBetaAgent("far5", 5, 10, -5),
    # aba.AlphaBetaAgent("far6", 6, 10, -5),
    # aba.AlphaBetaAgent("far7", 7, 10, -5),
    #aba.AlphaBetaAgent("far8", 8, 10, -5),
    # aba.AlphaBetaAgent("far9", 9, 10, -5),
    # aba.AlphaBetaAgent("far10", 10, 10, -5),
    #
    # aba.AlphaBetaAgent("default2", 2),
    # aba.AlphaBetaAgent("default3", 3),
    # aba.AlphaBetaAgent("default4", 4),
    # aba.AlphaBetaAgent("default5", 5),
    #aba.AlphaBetaAgent("default6", 6),
    aba.AlphaBetaAgent("default7", 7),
    #aba.AlphaBetaAgent("default8", 8),
    #aba.AlphaBetaAgent("default9", 9),
    aba.AlphaBetaAgent("default10", 10),

    # agent.RandomAgent("random1"),
    # agent.RandomAgent("random2"),
    # agent.RandomAgent("random3"),
    # agent.RandomAgent("random4"),
    # agent.RandomAgent("random5"),
    # agent.RandomAgent("random6"),
    # agent.RandomAgent("random7"),
    # agent.RandomAgent("random8"),
    # agent.RandomAgent("random9"),
    # agent.RandomAgent("random10"),
    # agent.RandomAgent("random11"),
    # agent.RandomAgent("random12"),
    # agent.RandomAgent("random13"),
    # agent.RandomAgent("random14"),
    # agent.RandomAgent("random15"),
    # agent.RandomAgent("random16"),
    # agent.RandomAgent("random17"),
    # agent.RandomAgent("random18"),
    # agent.RandomAgent("random19"),
    # agent.RandomAgent("random20"),
    #
    # agent.RandomAgent("random21"),
    # agent.RandomAgent("random22"),
    # agent.RandomAgent("random23"),
    # agent.RandomAgent("random24"),
    # agent.RandomAgent("random25"),
    # agent.RandomAgent("random26"),
    # agent.RandomAgent("random27"),
    # agent.RandomAgent("random28"),
    # agent.RandomAgent("random29"),
    # agent.RandomAgent("random30"),
    # agent.RandomAgent("random31"),
    # agent.RandomAgent("random32"),
    # agent.RandomAgent("random33"),
    # agent.RandomAgent("random34"),
    # agent.RandomAgent("random35"),
    # agent.RandomAgent("random36"),
    # agent.RandomAgent("random37"),
    # agent.RandomAgent("random38"),
    # agent.RandomAgent("random39"),
    # agent.RandomAgent("random40"),


]

# Run!
play_tournament(7,  # board width
                6,  # board height
                4,  # tokens in a row to win
                15,  # time limit in seconds
                agents)  # player list
