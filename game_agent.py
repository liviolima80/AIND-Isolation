"""This file contains all the classes you must complete for this project.

You can use the test cases in agent_test.py to help during development, and
augment the test suite with your own test cases to further test your code.

You must test your agent's strength against a set of agents with known
relative strength using tournament.py and include the results in your report.
"""
import random


class Timeout(Exception):
    """Subclass base exception for code clarity."""
    pass


def custom_score(game, player):
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

    return float(len(game.get_legal_moves(player)))    

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

        if(len(legal_moves) == (game.width * game.height)):
            # opening move of player 1: take the center of the board
            return ( int(game.width/2), int(game.height/2))
        if(len(legal_moves) == (game.width * game.height - 1)):
            # opening move of player 2
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
