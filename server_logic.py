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
      print("other Snake  - - - Dont go down")
      if "down" in possible_moves: possible_moves.remove("down")
    if (body_part["x"] == my_head["x"]) and ((body_part["y"]-1) == my_head["y"]):
      print("other Snake  - - - Dont go up")
      if "up" in possible_moves: possible_moves.remove("up")
    if (body_part["y"] == my_head["y"]) and ((body_part["x"]+1) == my_head["x"]):
      print("other Snake  - - - Dont go left")
      if "left" in possible_moves: possible_moves.remove("left")
    if (body_part["y"] == my_head["y"]) and ((body_part["x"]-1) == my_head["x"]):
      print("other Snake  - - - Dont go right")
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
      
"""Improving randomness"""
#Function to get movement direction out of dictionary having all possible moves witch chances
def get_move_with_highest_chance(possible_moves_chances:[dict]) -> str:
  bestmove_chance = 0
  for key in possible_moves_chances:
    if (possible_moves_chances[key] > bestmove_chance or bestmove_chance == 0):
      bestmove_chance = possible_moves_chances[key]
      bestmove = key
      print(f" {bestmove} mit Chance {possible_moves_chances[key]} ")
  return bestmove

#Function to get Coordinate for possible move
def get_coord_for_movedirection(head: Dict[str, int], move:[str]) -> Dict[str, int]:
    if move == "up":
      head["y"] = (head["y"] + 1)
      return head
    elif move == "down":
      head["y"] = (head["y"] - 1)
      return head
    elif move == "left":
      head["x"] = (head["x"] - 1)
      return head
    elif move == "right":
      head["x"] = (head["x"] + 1)
      return head
    else:
      return head

#Function to check if coordinate is in List of coordinates
def is_coord_in_coordlist(coord: [str, int], coord_list: List[dict]) -> str:
  bol_is_in_list = False
  for i in coord_list: #iterate through all items of the list
    if (i["x"] == coord["x"]) and (i["y"] == coord["y"]): # and set result var on true if coordinates are equal
      bol_is_in_list = True
  return bol_is_in_list

#Function to get list of neighbor-coords for a coord
def get_list_environmental_coords_for_coord(coord: [str, int]) -> List[dict]:
  result_coord_list = []
  
  upper_coord = {"x" : coord["x"], "y" : (coord["y"]+1)}
  upper_coord_copy = upper_coord.copy()
  result_coord_list.append(upper_coord_copy)

  lower_coord = {"x" : coord["x"], "y" : (coord["y"]-1)}
  lower_coord_copy = lower_coord.copy()
  result_coord_list.append(lower_coord_copy)

  right_coord = {"x" : (coord["x"]+1), "y" : coord["y"]}
  right_coord_copy = right_coord.copy()
  result_coord_list.append(right_coord_copy)
  
  left_coord = {"x" : (coord["x"]-1), "y" : coord["y"]}
  left_coord_copy = left_coord.copy()
  result_coord_list.append(left_coord_copy)
  
  return result_coord_list
      
#Function to manipulate the chance of a movement direction in a dict move / chance
def change_chance_of_movement(move:[str], chance_value:[int], possible_moves_chances:[dict]) -> dict:
  if move in possible_moves_chances: 
    possible_moves_chances[move] = (possible_moves_chances[move] + chance_value)
    print(f" Changed {move} by {chance_value} ")
  return possible_moves_chances

#Get movement direction based on near food and a ranking how far it is away - ranking by chance 100 - distance
def get_move_to_near_food(my_head: Dict[str, int], food_coord: [str, int]) -> dict:
  if (food_coord["x"] < my_head["x"]) and ((food_coord["y"]) == my_head["y"]):
      print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! FOOD is left")
      return ({"left":(100-(my_head["x"] - food_coord["x"]))})
  elif (food_coord["x"] > my_head["x"]) and ((food_coord["y"]) == my_head["y"]):
      print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! FOOD is right")
      return ({"right": (100-(food_coord["x"] - my_head["x"]))})
  elif (food_coord["x"] == my_head["x"]) and ((food_coord["y"]) > my_head["y"]):
      print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! FOOD is up")
      return ({"up": (100-(food_coord["y"]) - my_head["y"])})
  elif (food_coord["x"] == my_head["x"]) and ((food_coord["y"]) < my_head["y"]):
      print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! FOOD is down")
      return ({"down": (100-(my_head["y"]-food_coord["y"]))})
  return ({"false": 0})

def bad_idea_check(planned_coord: Dict[str, int], my_body: List[dict], board_height:[int], board_width:[int]) -> int: 
  return 0

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
    snakes = data["board"]["snakes"]
    
       
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
    for snake in snakes:
      if (snake["name"] != "daSchnake"):
          possible_moves = avoid_other_snakes(my_head, snake["body"], possible_moves)
   
    special_move = "false"
    # check if there is a move directly to food
    for food_coord in food:
      prio_move = direct_move_to_eat(my_head, food_coord)
      if prio_move != "false":
        special_move = "true"
        #if yes - eat it
        move = prio_move
        print(f"{data['game']['id']} PRIOMOVE {prio_move}")
  
    if special_move == "true":
      print(f"!!!!!  {data['game']['id']} Do the PRIO Move: {prio_move}")
    else:
      #create dict with chance per possible move from left possible moves
      possible_moves_chances = dict() #create the dict 
      for str_move in possible_moves:
        possible_moves_chances[str_move] = 0 #create all with chance 0
        print(f" {str_move} added to move/chance list")
      
      #print(f" {possible_moves_chances} ")

      """ Go to food if it is horizontalyl or vertically """
      for food_coord in food: #take all food coordinates
        improve_move_dic = get_move_to_near_food(my_head, food_coord) #check if it is directly vertically or horizontally and get distance
        """ take over direction and distance in possible moves """
      for key in improve_move_dic:
        if key != "false":
          possible_moves_chances = change_chance_of_movement(key, improve_move_dic[key], possible_moves_chances)      
       
      


      """reduce chance of movement, when other snakes head could go on that field"""
      for snake in snakes:
        if (snake["name"] != "daSchnake"):
          snake_body = snake["body"] # take other snakes body
          for possible_move in possible_moves_chances: # for all possible moves
            possible_coord_dic = get_coord_for_movedirection(my_head, possible_move) # get every target coord if you do the move
            envire_pos_coords_list = []
            envire_pos_coords_list = get_list_environmental_coords_for_coord(possible_coord_dic) # and get all neighbors to that target coord
            near_snake_head = is_coord_in_coordlist(snake_body[0], envire_pos_coords_list) # and now check, if on on of the neighbors is the head of another snake
            if (near_snake_head == True):
              print(f"SNAKE is near if I go {possible_move}")
              possible_moves_chances = change_chance_of_movement(possible_move, -100 ,possible_moves_chances) # reduce the chance by 100 if a snakes head is near
                
          #possible_moves = avoid_other_snakes(my_head, snake["body"], possible_moves)
          
      """get the best move option from dict with moves and chances"""
      bestmove = get_move_with_highest_chance(possible_moves_chances) 
      print(f"Selected {bestmove} as best move")
      
      
      move = bestmove
      #move = random.choice(possible_moves)
      print(f"{data['game']['id']} MOVE {data['turn']}: {move} picked from all valid options in {possible_moves}")
    
    # TODO: Explore new strategies for picking a move that are better than random
 
    

    return move
