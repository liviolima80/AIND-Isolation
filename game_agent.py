"""This file contains all the classes you must complete for this project.

You can use the test cases in agent_test.py to help during development, and
augment the test suite with your own test cases to further test your code.

You must test your agent's strength against a set of agents with known
relative strength using tournament.py and include the results in your report.
"""
import random
import math


class Timeout(Exception):
    """Subclass base exception for code clarity."""
    pass

def distance(p0, p1):
    return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)

def custom_score(game, player):
    """The "Improved" evaluation function discussed in lecture that outputs a
    score equal to the difference in the number of moves available to the
    two players.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : hashable
        One of the objects registered by the game object as a valid player.
        (i.e., `player` should be either game.__player_1__ or
        game.__player_2__).

    Returns
    ----------
    float
        The heuristic value of the current game state
    """
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    own_moves = len(game.get_legal_moves(player))
    opp_moves = len(game.get_legal_moves(game.get_opponent(player)))

    if(hasattr(player, 'q1')):
        available_spaces = game.get_blank_spaces()   
        available_q1 = len([x for x in available_spaces if x in player.q1])
        available_q2 = len([x for x in available_spaces if x in player.q2])
        available_q3 = len([x for x in available_spaces if x in player.q3])
        available_q4 = len([x for x in available_spaces if x in player.q4])
        
        better_place = max([(available_q1, player.b1), (available_q2, player.b2), (available_q3, player.b3), (available_q4, player.b4)])
        
        return float(own_moves - opp_moves) + \
                distance(better_place[1], game.get_player_location(game.get_opponent(player))) - \
                distance(better_place[1], game.get_player_location(player))
    else:
        return float(own_moves - opp_moves)
				 
def custom_score_center(game, player):
    """The "Improved" evaluation function discussed in lecture that outputs a
    score equal to the difference in the number of moves available to the
    two players.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : hashable
        One of the objects registered by the game object as a valid player.
        (i.e., `player` should be either game.__player_1__ or
        game.__player_2__).

    Returns
    ----------
    float
        The heuristic value of the current game state
    """
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    d = distance(game.get_player_location(player), (float(game.height)/2, float(game.width)/2))
    d2 = distance(game.get_player_location(game.get_opponent(player)), (float(game.height)/2, float(game.width)/2))

    return float(len(game.get_legal_moves(player)) - \
                 len(game.get_legal_moves(game.get_opponent(player)))) - d + d2
	
def custom_score_distance(game, player):
    """The "Improved" evaluation function discussed in lecture that outputs a
    score equal to the difference in the number of moves available to the
    two players.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : hashable
        One of the objects registered by the game object as a valid player.
        (i.e., `player` should be either game.__player_1__ or
        game.__player_2__).

    Returns
    ----------
    float
        The heuristic value of the current game state
    """
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    d = distance(game.get_player_location(player), game.get_player_location(game.get_opponent(player)))
    return d + float(len(game.get_legal_moves(player)) - len(game.get_legal_moves(game.get_opponent(player))))
	
def custom_score_h1_full_distance(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """

    # TODO: finish this function!

    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    available_spaces = game.get_blank_spaces()   
    available_q1 = len([x for x in available_spaces if x in player.q1])
    available_q2 = len([x for x in available_spaces if x in player.q2])
    available_q3 = len([x for x in available_spaces if x in player.q3])
    available_q4 = len([x for x in available_spaces if x in player.q4])
    
    better_place = max([(available_q1, player.b1), (available_q2, player.b2), (available_q3, player.b3), (available_q4, player.b4)])
    
    own_moves = len(game.get_legal_moves(player))
    opp_moves = len(game.get_legal_moves(game.get_opponent(player)))
    """return float(own_moves - opp_moves) + \
        distance(better_place[1], game.get_player_location(game.get_opponent(player))) - \
        distance(better_place[1], game.get_player_location(player))"""
    return distance(better_place[1], game.get_player_location(game.get_opponent(player))) - \
        distance(better_place[1], game.get_player_location(player))
        
def custom_score_h1_full_mixed(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """

    # TODO: finish this function!

    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    available_spaces = game.get_blank_spaces()   
    available_q1 = len([x for x in available_spaces if x in player.q1])
    available_q2 = len([x for x in available_spaces if x in player.q2])
    available_q3 = len([x for x in available_spaces if x in player.q3])
    available_q4 = len([x for x in available_spaces if x in player.q4])
    
    better_place = max([(available_q1, player.b1), (available_q2, player.b2), (available_q3, player.b3), (available_q4, player.b4)])
    
    own_moves = len(game.get_legal_moves(player))
    opp_moves = len(game.get_legal_moves(game.get_opponent(player)))
    return float(own_moves - opp_moves) + \
            distance(better_place[1], game.get_player_location(game.get_opponent(player))) - \
            distance(better_place[1], game.get_player_location(player))

def custom_score_h1_begin_mixed(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """

    # TODO: finish this function!

    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    available_spaces = game.get_blank_spaces()
    own_moves = len(game.get_legal_moves(player))
    opp_moves = len(game.get_legal_moves(game.get_opponent(player)))
    if(len(available_spaces) >= (game.width * game.height) / 2):
        available_q1 = len([x for x in available_spaces if x in player.q1])
        available_q2 = len([x for x in available_spaces if x in player.q2])
        available_q3 = len([x for x in available_spaces if x in player.q3])
        available_q4 = len([x for x in available_spaces if x in player.q4])

        better_place = max([(available_q1, player.b1), (available_q2, player.b2), (available_q3, player.b3), (available_q4, player.b4)])

        return float(own_moves - opp_moves) + \
            distance(better_place[1], game.get_player_location(game.get_opponent(player))) - \
            distance(better_place[1], game.get_player_location(player))
    else:
        return float(own_moves - opp_moves)
    
def custom_score_h1_begin_distance(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """

    # TODO: finish this function!

    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    available_spaces = game.get_blank_spaces()
    own_moves = len(game.get_legal_moves(player))
    opp_moves = len(game.get_legal_moves(game.get_opponent(player)))
    if(len(available_spaces) >= (game.width * game.height) / 2):
        available_q1 = len([x for x in available_spaces if x in player.q1])
        available_q2 = len([x for x in available_spaces if x in player.q2])
        available_q3 = len([x for x in available_spaces if x in player.q3])
        available_q4 = len([x for x in available_spaces if x in player.q4])

        better_place = max([(available_q1, player.b1), (available_q2, player.b2), (available_q3, player.b3), (available_q4, player.b4)])

        return distance(better_place[1], game.get_player_location(game.get_opponent(player))) - \
            distance(better_place[1], game.get_player_location(player))
    else:
        return float(own_moves - opp_moves)

class CustomPlayer:
    """Game-playing agent that chooses a move using your evaluation function
    and a depth-limited minimax algorithm with alpha-beta pruning. You must
    finish and test this player to make sure it properly uses minimax and
    alpha-beta to return a good move before the search time limit expires.

    Parameters
    ----------
    search_depth : int (optional)
        A strictly positive integer (i.e., 1, 2, 3,...) for the number of
        layers in the game tree to explore for fixed-depth search. (i.e., a
        depth of one (1) would only explore the immediate sucessors of the
        current state.)

    score_fn : callable (optional)
        A function to use for heuristic evaluation of game states.

    iterative : boolean (optional)
        Flag indicating whether to perform fixed-depth search (False) or
        iterative deepening search (True).

    method : {'minimax', 'alphabeta'} (optional)
        The name of the search method to use in get_move().

    timeout : float (optional)
        Time remaining (in milliseconds) when search is aborted. Should be a
        positive value large enough to allow the function to return before the
        timer expires.
    """

    def __init__(self, search_depth=3, score_fn=custom_score,
                 iterative=True, method='minimax', timeout=10.):
        self.search_depth = search_depth
        self.iterative = iterative
        self.score = score_fn
        self.method = method
        self.time_left = None
        self.TIMER_THRESHOLD = timeout
        self.q1 = None
        self.q2 = None
        self.q3 = None
        self.q4 = None
        self.b1 = None
        self.b2 = None
        self.b3 = None
        self.b4 = None

    def create_quarter(self, width, height):
        split_width = int(width/2)
        if( (width % 2) == 1): split_width = int(width/2) +1
        split_height = int(height/2)
        if( (height % 2) == 1): split_height = int(height/2) +1
        q1 = [(i,j) for i in range(0, split_width) for j in range(0, split_height)]
        q3 = [(i,j) for i in range(int(width/2), width) for j in range(0, split_height)]
        q2 = [(i,j) for i in range(0, split_width) for j in range(int(height/2), height)]
        q4 = [(i,j) for i in range(int(width/2), width) for j in range(int(height/2), height)]
        b1 = tuple([sum(x) for x in zip(*q1)])
        b2 = tuple([sum(x) for x in zip(*q2)])
        b3 = tuple([sum(x) for x in zip(*q3)])
        b4 = tuple([sum(x) for x in zip(*q4)])
        b1 = tuple([x/len(q1) for x in b1])
        b2 = tuple([x/len(q2) for x in b2])
        b3 = tuple([x/len(q3) for x in b3])
        b4 = tuple([x/len(q4) for x in b4])
        return q1, q2, q3, q4, b1, b2, b3, b4

    def get_move(self, game, legal_moves, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        This function must perform iterative deepening if self.iterative=True,
        and it must use the search method (minimax or alphabeta) corresponding
        to the self.method value.

        **********************************************************************
        NOTE: If time_left < 0 when this function returns, the agent will
              forfeit the game due to timeout. You must return _before_ the
              timer reaches 0.
        **********************************************************************

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        legal_moves : list<(int, int)>
            A list containing legal moves. Moves are encoded as tuples of pairs
            of ints defining the next (row, col) for the agent to occupy.

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """

        self.time_left = time_left

        # TODO: finish this function!

        # Perform any required initializations, including selecting an initial
        # move from the game board (i.e., an opening book), or returning
        # immediately if there are no legal moves
        
        # create positions for 4 quarter
        if(self.q1 == None):
            self.q1, self.q2, self.q3, self.q4, self.b1, self.b2, self.b3, self.b4 = \
                self.create_quarter(game.width, game.height)

        if(len(legal_moves) == (game.width * game.height)):
            # opening move of player 1: take the center of the board
            return ( int(game.width/2), int(game.height/2))
        if(len(legal_moves) == (game.width * game.height - 1)):
            # opening move of player 2: not required to be implemented for the project submission
            return (0,0)
        if(len(legal_moves) == 0):
            # end game
            return (-1,-1)
        else:
            best_move = legal_moves[0]

        try:
            # The search method call (alpha beta or minimax) should happen in
            # here in order to avoid timeout. The try/except block will
            # automatically catch the exception raised by the search method
            # when the timer gets close to expiring

            if(self.iterative):
                for idx in range(1, game.width * game.height):
                    if(self.method == 'minimax'):
                        score, best_move = self.minimax(game, idx)
                    if(self.method == 'alphabeta'):
                        score, best_move = self.alphabeta(game, idx)
            else:
                depth = game.width * game.height # max possible depth
                if(self.search_depth >= 1): depth = self.search_depth
                if(self.method == 'minimax'):
                    score, best_move = self.minimax(game, depth)
                if(self.method == 'alphabeta'):
                    score, best_move = self.alphabeta(game, depth)

        except Timeout:
            # Handle any actions required at timeout, if necessary
            if( (len(legal_moves) > 0) and (best_move == (-1, -1))):
                print('Timeout error condition')
            return best_move

        # Return the best move from the last completed search iteration
        if( (len(legal_moves) > 0) and (best_move == (-1, -1))):
                print('Normal error condition ', self.iterative)
        return best_move

    def minimax_max(self, game, depth, maximizing_player=True):

        if self.time_left() < self.TIMER_THRESHOLD:
            raise Timeout()

        # exit condition1 : leaf node
        if(len(game.get_legal_moves()) == 0):
            exit_score = self.score(game, self)
            if(exit_score == float('inf')):
                return exit_score, game.get_player_location(self)
            else:
                return exit_score, (-1, -1)

        #exit condition 2 : max fixed depth reached
        if(depth == 0):
           return self.score(game, self), game.get_player_location(self)

        score = float("-inf")
        move = game.get_player_location(self)

        legal_move = game.get_legal_moves()
        for m in legal_move:
            new_score, notmove = self.minimax_min(game.forecast_move(m), depth - 1, not maximizing_player)
            if( (new_score > score) or (new_score == float('inf'))):
                score = new_score
                move = m
        return score, move

    def minimax_min(self, game, depth, maximizing_player=True):

        if self.time_left() < self.TIMER_THRESHOLD:
            raise Timeout()

        # exit condition 1 : leaf node
        if(len(game.get_legal_moves()) == 0):
            exit_score = self.score(game, self)
            if(exit_score == float('inf')):
                return exit_score, game.get_player_location(self)
            else:
                return exit_score, (-1, -1)

        #exit condition 2 : max fixed depth reached
        if(depth == 0):
           return self.score(game, self), game.get_player_location(self)

        score = float("inf")
        move = game.get_player_location(self)

        legal_move = game.get_legal_moves()
        for m in legal_move:
            new_score, notmove = self.minimax_max(game.forecast_move(m), depth - 1, not maximizing_player)
            if( (new_score < score) or (new_score == float('-inf'))):
                score = new_score
                move = m

        return score, move

    def minimax(self, game, depth, maximizing_player=True):
        """Implement the minimax search algorithm as described in the lectures.

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        maximizing_player : bool
            Flag indicating whether the current search depth corresponds to a
            maximizing layer (True) or a minimizing layer (False)

        Returns
        -------
        float
            The score for the current search branch

        tuple(int, int)
            The best move for the current branch; (-1, -1) for no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project unit tests; you cannot call any other
                evaluation function directly.
        """

        if self.time_left() < self.TIMER_THRESHOLD:
            raise Timeout()

        if(len(game.get_legal_moves()) == 0):
            exit_score = self.score(game, self)
            if(exit_score == float('inf')):
                return exit_score, game.get_player_location(self)
            else:
                return exit_score, (-1, -1)

        # TODO: finish this function!
        return self.minimax_max(game, depth, maximizing_player)

    def alphabeta_max(self, game, depth, alpha, beta, maximizing_player=True):

        if self.time_left() < self.TIMER_THRESHOLD:
            raise Timeout()

        # exit condition 1 : leaf node
        if(len(game.get_legal_moves()) == 0):
            exit_score = self.score(game, self)
            if(exit_score == float('inf')):
                return exit_score, game.get_player_location(self)
            else:
                return exit_score, (-1, -1)

        #exit condition 2 : max fixed depth reached
        if(depth == 0):
            return self.score(game, self), game.get_player_location(self)

        score = float("-inf")
        move = game.get_player_location(self)

        legal_move = game.get_legal_moves()
        for m in legal_move:
            new_score, notmove = self.alphabeta_min(game.forecast_move(m), depth - 1, alpha, beta, not maximizing_player)
            if( (new_score > score) or (new_score == float('inf'))):
                score = new_score
                move = m
            if(score >= beta):
                return score, move
            alpha = max(alpha, score)

        return score, move

    def alphabeta_min(self, game, depth, alpha, beta, maximizing_player=True):

        if self.time_left() < self.TIMER_THRESHOLD:
            raise Timeout()

        # exit condition 1 : leaf node
        if(len(game.get_legal_moves()) == 0):
            exit_score = self.score(game, self)
            if(exit_score == float('inf')):
                return exit_score, game.get_player_location(self)
            else:
                return exit_score, (-1, -1)

        #exit condition 2 : max fixed depth reached
        if(depth == 0):
            return self.score(game, self), game.get_player_location(self)

        score = float("inf")
        move = game.get_player_location(self)

        legal_move = game.get_legal_moves()
        for m in legal_move:
            new_score, notmove = self.alphabeta_max(game.forecast_move(m), depth - 1, alpha, beta, not maximizing_player)
            if( (new_score < score) or (new_score == float('-inf'))):
                score = new_score
                move = m
            if(score <= alpha):
                return score, move
            beta = min(beta, score)

        return score, move

    def alphabeta(self, game, depth, alpha=float("-inf"), beta=float("inf"), maximizing_player=True):
        """Implement minimax search with alpha-beta pruning as described in the
        lectures.

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        alpha : float
            Alpha limits the lower bound of search on minimizing layers

        beta : float
            Beta limits the upper bound of search on maximizing layers

        maximizing_player : bool
            Flag indicating whether the current search depth corresponds to a
            maximizing layer (True) or a minimizing layer (False)

        Returns
        -------
        float
            The score for the current search branch

        tuple(int, int)
            The best move for the current branch; (-1, -1) for no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project unit tests; you cannot call any other
                evaluation function directly.
        """

        if self.time_left() < self.TIMER_THRESHOLD:
            raise Timeout()

        if(len(game.get_legal_moves()) == 0):
            exit_score = self.score(game, self)
            if(exit_score == float('inf')):
                return exit_score, game.get_player_location(self)
            else:
                return exit_score, (-1, -1)

        return self.alphabeta_max(game, depth, alpha, beta, maximizing_player)
