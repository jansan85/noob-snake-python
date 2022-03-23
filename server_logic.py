import random
from typing import List, Dict

"""
This file can be a nice home for your move logic, and to write helper functions.

We have started this for you, with a function to help remove the 'neck' direction
from the list of possible moves!
"""


""" Avoiding biting your body to take out moves on fields your own body is on """

def avoid_my_body(my_head: Dict[str, int], my_body: List[dict], possible_moves: List[str], my_tail:Dict[str, int]) -> List[str]:
  for body_part in my_body:
    if are_these_coords_equal(body_part, my_tail):
      print("My Tail is a friend...")
    else:
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
      #print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! PRIO - eat up")
      return "up"
    elif (food_coord["x"] == my_head["x"]) and ((food_coord["y"]+1) == my_head["y"]):
      #print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! PRIO - eat down")
      return "down"
    elif (food_coord["y"] == my_head["y"]) and ((food_coord["x"]+1) == my_head["x"]):
      #print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! PRIO - eat left")
      return "left"
    elif (food_coord["y"] == my_head["y"]) and ((food_coord["x"]-1) == my_head["x"]):
      #print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! PRIO - eat right")
      return "right"
    else: return "false"
      
"""Improving randomness"""
#Function to get movement direction out of dictionary having all possible moves witch chances
def get_move_with_highest_chance(possible_moves_chances:[dict]) -> str:
  bestmove_chance = -5000
  for key in possible_moves_chances:
    if (possible_moves_chances[key] > bestmove_chance or bestmove_chance == -5000):
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
      print("BIG ERROR")
      return head

# Check if our snake is the longest - return Bool
def i_am_longest(snakes: List[dict], my_length:[int], my_name:[str]):
  global longest
  longest = True
  for snake in snakes:
      other_snake_name = snake["name"]
      other_snake_length = snake["length"]
      if other_snake_name != my_name and other_snake_length >= my_length:
        longest = False      

# If health < height+width (max steps to reach food) or 
def i_am_hungry(my_health: [int]):
  global hungry
  if my_health > (board_height + board_width) and longest:
    hungry = False
  else:
    hungry = True

def get_move_to_leave_outerline_if_i_am_on_it(head: Dict[str, int]):
  global own_head_outerline #set global own_head_on_outerline boolean
  if (head["x"] == 0 or (head["x"] == (board_width-1)) or head["y"] == 0 or (head["y"] == (board_height-1))):
    own_head_outerline = True
    if head["x"] == 0:
      return "right"
    elif (head["x"] == (board_width-1)):
      return "left"
    elif head["y"] == 0:
      return "up"
    elif (head["y"] == (board_height-1)):
      return "down"
  else:
    own_head_outerline = False
    return False  
  
      
#Function to check if coordinate is in List of coordinates
def is_coord_in_coordlist(coord: [str, int], coord_list: List[dict]):
  bol_is_in_list = False
  for i in coord_list: #iterate through all items of the list
    #print(f"create coord for {i}")
    if (i["x"] == coord["x"]) and (i["y"] == coord["y"]): 
      bol_is_in_list = True
  return bol_is_in_list

#Function are two coords the same return Bool
def are_these_coords_equal(coord1: [str, int], coord2: [str, int]):
  if (coord1["x"] == coord2["x"]) and (coord1["y"] == coord2["y"]):
    return True
  else:
    return False

#Function to check if that coordination is a dead_end
def are_all_coords_of_cordlist_blocked_by_snakes(coord_list: List[dict], all_snake_bodies: List[dict]): 
  all_blocked = False
  for i in coord_list:
    if is_coord_in_coordlist(i, all_snake_bodies):
      print("Snakes everywhere!!!")
      all_blocked = True
  return all_blocked

def add_single_list_of_coords_to_other_list_of_coords(coord_list: List[dict], glo_coord_list: List[dict]) -> List[dict]:
  for i in coord_list:
    i_copy = i.copy()
    glo_coord_list.append(i_copy)
  return glo_coord_list


#get Tail of a snake by taking coord of last list item of snakes body
def get_tail_of_snake(snake: List[dict]) -> Dict[str, int]:
  tail = snake.pop()
  print(f"{tail} is a tail")
  return tail
  
#Function to get list of neighbor-coords for a coord respecting edges
def get_list_environmental_coords_for_coord(coord: [str, int], board_height:[int], board_width:[int]) -> List[dict]:
  result_coord_list = []

  if (coord["y"]+1) <= board_height:
    upper_coord = {"x" : coord["x"], "y" : (coord["y"]+1)}
    upper_coord_copy = upper_coord.copy()
    result_coord_list.append(upper_coord_copy)
    
  if (coord["y"]-1) >= 0:
    lower_coord = {"x" : coord["x"], "y" : (coord["y"]-1)}
    lower_coord_copy = lower_coord.copy()
    result_coord_list.append(lower_coord_copy)

  if (coord["x"]+1) <= board_width:
    right_coord = {"x" : (coord["x"]+1), "y" : coord["y"]}
    right_coord_copy = right_coord.copy()
    result_coord_list.append(right_coord_copy)

  if (coord["x"]-1) >= 0:
    left_coord = {"x" : (coord["x"]-1), "y" : coord["y"]}
    left_coord_copy = left_coord.copy()
    result_coord_list.append(left_coord_copy)
    
  return result_coord_list

# get all coord neighbors in a list for a given coor
def get_all_moves(coord):
    return [{'x': coord['x'], 'y': coord['y'] + 1}, {'x': coord['x'], 'y': coord['y'] - 1}, {'x': coord['x'] + 1, 'y': coord['y']}, {'x': coord['x'] - 1, 'y': coord['y']}]


#Function retturn True if coord is on outerline
def is_coord_on_outerline(coord: [str, int]):
  if (coord["x"] == 0 or (coord["x"] == (board_height-1)) or coord["y"] == 0 or (coord["y"] == (board_width-1))):
    return True
  else:
    return False
  
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

# Manipulate the chances of moves to outerlines by -10 - own_health * 2 (max -210)
def lower_outerline_chances(my_head: Dict[str, int],my_health: [int], board_height:[int], board_width:[int], possible_moves_chances:[dict]) -> [dict]:
  chancereduction = (-10 - (my_health * 2))
  if my_head["x"] == 1: 
    if "left" in possible_moves_chances: 
      possible_moves_chances = change_chance_of_movement("left", chancereduction ,possible_moves_chances)
      print("optimization - left would lead to outline")
  elif my_head["x"] == (board_width-2):  
    if "right" in possible_moves_chances: 
      possible_moves_chances = change_chance_of_movement("right", chancereduction ,possible_moves_chances)
      print("optimization - right would lead to outline")

  if my_head["y"] == 1:  
        if "down" in possible_moves_chances: 
          possible_moves_chances = change_chance_of_movement("down", chancereduction ,possible_moves_chances)
          print("optimization - down would lead to outline")
  elif my_head["y"] == (board_height-2):
        if "up" in possible_moves_chances: 
          possible_moves_chances = change_chance_of_movement("up", chancereduction ,possible_moves_chances)
          print("optimization - up would lead to outline")
  return possible_moves_chances



def bad_idea_check(planned_coord: Dict[str, int], my_body: List[dict], board_height:[int], board_width:[int]) -> int: 
  return 0

def choose_move(data: dict) -> str:
  """
  data: Dictionary of all Game Board data as received from the Battlesnake Engine.
  For a full example of 'data', see https://docs.battlesnake.com/references/api/sample-  move-request

  return: A String, the single move to make. One of "up", "down", "left" or "right".

  Use the information in 'data' to decide your next move. The 'data' variable can be 
  interacted with as a Python Dictionary, and contains all of the information about   
  the Battlesnake board
  for each move of the game.
  """
  my_name = data["you"]["name"]
  my_head = data["you"]["head"]  # dict of head {"x": 0, "y": 0}
  my_body = data["you"]["body"]  # A list of x/y coordinate dictionaries like [ {"x": 0, "y": 0}, {"x": 1, "y": 0}, {"x": 2, "y": 0} ]
  my_tail = get_tail_of_snake(my_body)
  global board_height
  board_height = data["board"]["height"] #int board_height
  global board_width
  board_width = data["board"]["width"] #int board width
  food = data["board"]["food"] #A list of x/y coordinate dictionaries like [ {"x": 0, "y": 0}, {"x": 1, "y": 0}, {"x": 2, "y": 0} ] 
  snakes = data["board"]["snakes"]
  turn_id = data["turn"]
  
  """delete own snake from list of othersnakes"""
  othersnakes = snakes[:]
  for i in range(len(othersnakes)):
    if othersnakes[i]["name"] == my_name:
        del othersnakes[i]
        break

  #print(f"other snakes are {othersnakes}")
  
  my_length = data["you"]["length"] #int length
  my_health = data["you"]["health"] 
    
       
  possible_moves = ["up", "down", "left", "right"]

  i_am_longest(othersnakes, my_length, my_name)
  i_am_hungry(my_health)

  """ Don't allow your Battlesnake to move back in on it's own neck"""
  possible_moves = avoid_my_neck(my_head, my_body, possible_moves)
  
  """ Using information from 'data', find the edges of the board and don't let your Battlesnake move beyond them"""
  possible_moves = avoid_edges(my_head, board_height, board_width, my_body, possible_moves)

  """Avoid biting your own body"""
  possible_moves = avoid_my_body(my_head, my_body, possible_moves, my_tail)

  """Avoid to bite another snake"""
  for enemy_snake in othersnakes:
    #enemy_snake_name = enemy_snake["name"]
    possible_moves = avoid_other_snakes(my_head, enemy_snake["body"], possible_moves)
    #print(f"avoided bite other snake {enemy_snake_name}")
  
  """create dict with chance per possible move from left possible moves"""
  possible_moves_chances = dict() #create the dict 
  for str_move in possible_moves:
    possible_moves_chances[str_move] = 0 #create all with chance 0
    #print(f" {str_move} added to move/chance list")

  """better avoid outer lines if you are not hungry"""
  if turn_id > 20 and not hungry:
    possible_moves_chances = lower_outerline_chances(my_head, my_health, board_height, board_width, possible_moves_chances)
    #print(f" {possible_moves_chances} ")

  """better leave outerline if ia am on it"""
  global own_head_outerline
  leave_outerline_move = get_move_to_leave_outerline_if_i_am_on_it(my_head)
  if leave_outerline_move != False:
    print(f" better leave outerline with {leave_outerline_move}")
    possible_moves_chances = change_chance_of_movement(leave_outerline_move, 50 ,possible_moves_chances)
  
  """check if there is a move directly to food"""
  for food_coord in food:
    prio_move = direct_move_to_eat(my_head, food_coord)
    if prio_move != "false":
      possible_moves_chances = change_chance_of_movement(prio_move, (200 - (my_health * 2)) ,possible_moves_chances)

        
  """ Go to food if it is horizontalyl or vertically """
  for food_coord in food: #take all food coordinates
    improve_move_dic = get_move_to_near_food(my_head, food_coord) #check if it is directly vertically or horizontally and get distance
    """ take over direction and distance in possible moves """
    for key in improve_move_dic:
      if key != "false":
        possible_moves_chances = change_chance_of_movement(key, improve_move_dic[key], possible_moves_chances)      
            
  """reduce chance of movement, when other snakes head could go on that field - except I am longer - than kill it"""
  for possible_move in possible_moves_chances: # for all possible moves
      possible_coord_dic = get_coord_for_movedirection(my_head, possible_move) # get every target coord if you do the move
      envire_pos_coords_list = []
      envire_pos_coords_list = get_list_environmental_coords_for_coord(possible_coord_dic, board_height, board_width)
      for othersnake in othersnakes:
        othersnake_body = othersnake["body"]
        print(f"near_snake check for head at :{othersnake_body[0]}")
        if is_coord_in_coordlist(othersnake_body[0],envire_pos_coords_list):
          print(f"SNAKE is near if I go {possible_move}")
          #if (i_am_longest(snakes, my_length, my_name)):
          if (othersnake["length"] < my_length):
            print(f"KILLER -- -- -- With {my_length} I am longer than {othersnake['name']} with {othersnake['length']}")
            possible_moves_chances = change_chance_of_movement(possible_move, +2000 ,possible_moves_chances)
          else:
            possible_moves_chances = change_chance_of_movement(possible_move, -1000 ,possible_moves_chances) # reduce the chance by 500 if a snakes head is near

          
  """get the best move option from dict with moves and chances"""
  bestmove = get_move_with_highest_chance(possible_moves_chances) 
  print(f"Selected {bestmove} as best move for MOVE {data['turn']}")
      
     
  move = bestmove
    #move = random.choice(possible_moves)
  print(f"{data['game']['id']} MOVE {data['turn']}: {move} picked from all valid options in {possible_moves_chances}")
    
  # TODO: Explore new strategies for picking a move that are better than random
 
    

  return move
