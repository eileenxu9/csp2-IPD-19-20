####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'E0'
strategy_name = 'Betray when other player betrayed'
strategy_description = 'Betray first. Betray when other players last move was betray. Otherwise, look at previous rounds and copy what they did in the same situation. If the previous rounds result never has happened, collude except after being severly punished.'

def probability_that_other_player_will_betray(my_history, their_history, my_score, their_score):
  their_previous_round = their_history[-1]
  my_previous_round = my_history[-1]
  
# Look at rounds before that one
  for round in range(len(my_history)-1):
    their_prior_round = their_history[round]
    my_prior_round = my_history[round]
    # If one matches
    if (my_prior_round == my_previous_round) and (their_prior_round == their_previous_round):
      return their_history[round]
        # No match found
  if my_history[-1]=='c' and their_history[-1]=='b':
    return 'b' # Betray if we were severely punished last time.
  else:
    return 'c' # Otherwise collude.

def move(my_history, their_history, my_score, their_score):
  '''Make my move based on the history with this player.
  
  history: a string with one letter (c or b) per round that has been played with this opponent.
  their_history: a string of the same length as history, possibly empty. 
  The first round between these two players is my_history[0] and their_history[0]
  The most recent round is my_history[-1] and their_history[-1]
  
  Returns 'c' or 'b' for collude or betray.
  '''
  if len(my_history)==0: # It's the first round; betray.
    return 'b'
  elif their_history[-1]=='b':
    return 'b' # Betray if their last move was betray.
  else:
    probability_that_other_player_will_betray(my_history, their_history, my_score, their_score) # otherwise call probability_that_other_player_will_betray() function