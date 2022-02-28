import random
from typing import List, Dict

"""
This file can be a nice home for your move logic, and to write helper functions.

We have started this for you, with a function to help remove the 'neck' direction
from the list of possible moves!
"""


""" Avoiding biting your body to take out moves on fields your own body is on """
def avoid_my_body(my_head: Dict[str, int], my_body: List[dict], possible_moves: List[str]) -> List[str]:
  for body_part in my_body:
    if (body_part["x"] == my_head["x"]) and ((body_part["y"]+1) == my_head["y"]):
      print("body  - - - Dont go down")
      if "down" in possible_moves: possible_moves.remove("down")
    if (body_part["x"] == my_head["x"]) and ((body_part["y"]-1) == my_head["y"]):
      print("body  - - - Dont go up")
      if "up" in possible_moves: possible_moves.remove("up")
    if (body_part["y"] == my_head["y"]) and ((body_part["x"]+1) == my_head["x"]):
      print("body  - - - Dont go left")
      if "left" in possible_moves: possible_moves.remove("left")
    if (body_part["y"] == my_head["y"]) and ((body_part["x"]-1) == my_head["x"]):
      print("body  - - - Dont go right")
      if "right" in possible_moves: possible_moves.remove("right")
  return possible_moves

""" Avoiding biting other snakes by taking out moves on fields another snake is on """
def avoid_other_snakes(my_head: Dict[str, int], other_snake_body: List[dict], possible_moves: List[str]) -> List[str]:
  for body_part in other_snake_body:
    if (body_part["x"] == my_head["x"]) and ((body_part["y"]+1) == my_head["y"]):
      print("body  - - - Dont go down")
      if "down" in possible_moves: possible_moves.remove("down")
    if (body_part["x"] == my_head["x"]) and ((body_part["y"]-1) == my_head["y"]):
      print("body  - - - Dont go up")
      if "up" in possible_moves: possible_moves.remove("up")
    if (body_part["y"] == my_head["y"]) and ((body_part["x"]+1) == my_head["x"]):
      print("body  - - - Dont go left")
      if "left" in possible_moves: possible_moves.remove("left")
    if (body_part["y"] == my_head["y"]) and ((body_part["x"]-1) == my_head["x"]):
      print("body  - - - Dont go right")
      if "right" in possible_moves: possible_moves.remove("right")
  return possible_moves

""" Avoiding biting your neck by taking out a move 'back' """
def avoid_my_neck(my_head: Dict[str, int], my_body: List[dict], possible_moves: List[str]) -> List[str]:
    my_neck = my_body[1]  # The segment of body right after the head is the 'neck'

    if my_neck["x"] < my_head["x"]:  # my neck is left of my head
        if "left" in possible_moves: possible_moves.remove("left")
    elif my_neck["x"] > my_head["x"]:  # my neck is right of my head
        if "right" in possible_moves: possible_moves.remove("right")
    elif my_neck["y"] < my_head["y"]:  # my neck is below my head
        if "down" in possible_moves: possible_moves.remove("down")
    elif my_neck["y"] > my_head["y"]:  # my neck is above my head
        if "up" in possible_moves: possible_moves.remove("up")
    return possible_moves

""" Avoiding leaving the field by taking out a moves if head is on 'outer lines' """
def avoid_edges(my_head: Dict[str, int], board_height:[int], board_width:[int], my_body: List[dict], possible_moves: List[str]) -> List[str]:

    # check width
    if my_head["x"] == 0:  # already on the very left dont go left
        if "left" in possible_moves: possible_moves.remove("left")
        print("edge - - - Dont go left")
    elif my_head["x"] == (board_width-1):  # already on the very right dont go right
        if "right" in possible_moves: possible_moves.remove("right")
        print("edge - - - Dont go right")
    #check height
    if my_head["y"] == 0:  # already on lowest lane dont go down
        if "down" in possible_moves: possible_moves.remove("down")
        print("edge - - - Dont go down")
    elif my_head["y"] == (board_height-1):  # already on uppest lane dont go up
        if "up" in possible_moves: possible_moves.remove("up")
        print("edge - - - Dont go up")

    return possible_moves

""" Eat food that can be reached directly """
def direct_move_to_eat(my_head: Dict[str, int], food_coord: [str, int]) -> str: 
    #print(f" priomatch food_coord {food_coord} vs {my_head}")
    if (food_coord["x"] == my_head["x"]) and ((food_coord["y"]-1) == my_head["y"]):
      print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! PRIO - eat up")
      return "up"
    elif (food_coord["x"] == my_head["x"]) and ((food_coord["y"]+1) == my_head["y"]):
      print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! PRIO - eat down")
      return "down"
    elif (food_coord["y"] == my_head["y"]) and ((food_coord["x"]+1) == my_head["x"]):
      print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! PRIO - eat left")
      return "left"
    elif (food_coord["y"] == my_head["y"]) and ((food_coord["x"]-1) == my_head["x"]):
      print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! PRIO - eat right")
      return "right"
    else: return "false"
    

    


def choose_move(data: dict) -> str:
    """
    data: Dictionary of all Game Board data as received from the Battlesnake Engine.
    For a full example of 'data', see https://docs.battlesnake.com/references/api/sample-move-request

    return: A String, the single move to make. One of "up", "down", "left" or "right".

    Use the information in 'data' to decide your next move. The 'data' variable can be interacted
    with as a Python Dictionary, and contains all of the information about the Battlesnake board
    for each move of the game.

    """
    my_head = data["you"]["head"]  # A dictionary of x/y coordinates like {"x": 0, "y": 0}
    my_body = data["you"]["body"]  # A list of x/y coordinate dictionaries like [ {"x": 0, "y": 0}, {"x": 1, "y": 0}, {"x": 2, "y": 0} ]
    board_height = data["board"]["height"] #int board_height
    #print (board_height)
    board_width = data["board"]["width"] #int board width
    #print (board_width)
    food = data["board"]["food"] #A list of x/y coordinate dictionaries like [ {"x": 0, "y": 0}, {"x": 1, "y": 0}, {"x": 2, "y": 0} ] 
    #snakes = data["snakes"]
    
       
    # TODO: uncomment the lines below so you can see what this data looks like in your output!
    # print(f"~~~ Turn: {data['turn']}  Game Mode: {data['game']['ruleset']['name']} ~~~")
    # print(f"All board data this turn: {data}")
    # print(f"My Battlesnakes head this turn is: {my_head}")
    # print(f"My Battlesnakes body this turn is: {my_body}")

    possible_moves = ["up", "down", "left", "right"]

    # Don't allow your Battlesnake to move back in on it's own neck
    possible_moves = avoid_my_neck(my_head, my_body, possible_moves)
  
    #  Using information from 'data', find the edges of the board and don't let your Battlesnake move beyond them
    possible_moves = avoid_edges(my_head, board_height, board_width, my_body, possible_moves)

    # Don't bite your own body
    possible_moves = avoid_my_body(my_head, my_body, possible_moves)

    # Don't bite other snakes
    #other_snake_body = 
   # possible_moves = avoid_other_snakes(my_head, other_snake_body, possible_moves)
    special_move = "false"
    # check if there is a move directly to food
    for food_coord in food:
      prio_move = direct_move_to_eat(my_head, food_coord)
      if prio_move != "false":
        special_move = "true"
        move = prio_move
        print(f"{data['game']['id']} PRIOMOVE {prio_move}")
  
    if special_move == "true":
      print(f"!!!!!  {data['game']['id']} Do the PRIO Move: {prio_move}")
    else:
      move = random.choice(possible_moves)
      print(f"{data['game']['id']} MOVE {data['turn']}: {move} picked from all valid options in {possible_moves}")
    
    # TODO: Explore new strategies for picking a move that are better than random
 
    

    return move
