from room import Room
from player import Player
from world import World
from util import Stack
import random
from ast import literal_eval

# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "projects/adventure/maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

###############################################################################

backtrack = False
s = Stack()
journal = {}
my_visited_rooms = set()
for i in range(len(room_graph)):
    journal[i] = {'n': '?', 's': '?', 'w': '?', 'e': '?'}



def get_opposite(direction):
    if direction == 'n':
        return 's'
    if direction == 's':
        return 'n'
    if direction == 'e':
        return 'w'
    if direction == 'w':
        return 'e'

print('STARTING ROOM ID: ', player.current_room.id)
# print('CURRENT EXITS: ', player.current_room.get_exits())
# print('CURRENT EXITS STRING: ', player.current_room.get_exits_string())
# print('GRAPH LENGTH: ', len(room_graph))
# print('tRAVERSAL PATH LENGTH: ', len(traversal_path)) 
print('STARTING JOURNAL: ', journal)
# print('\n')

my_visited_rooms.add(player.current_room.id)

# print('current room stuff: ', journal[player.current_room.id]['n'])

while len(my_visited_rooms) < len(room_graph):

    # Get current Room ID
    first_room = player.current_room.id

    backtrack = False

    # Fill NONE Directions
    first_room_directions = player.current_room.get_exits()

    for direction in journal[first_room]:
        if direction not in first_room_directions:
            journal[first_room][direction] = None

    # Check which rooms unexplored
    num_known_rooms = 0
    for direction in journal[first_room]:
        if journal[first_room][direction] != '?':
            num_known_rooms += 1
        # if a room is unexplored
        elif not None:
            move_to_room = direction
    # If all rooms are explored
    if num_known_rooms == 4:        
        backtrack = True

    #Start Backtracking
    if backtrack is True:
        last_move = s.pop()
        move_to_room = get_opposite(last_move)
        # Add to traversal path Where i am about to Go
        traversal_path.append(move_to_room)
        # Go There
        player.travel(move_to_room)

    # If no backtrack
    else:
        # print(f'Room {first_room} Directions: ', journal[first_room])
        # print(f'Moving from room {first_room} in direction {move_to_room}')

        # Add to Stack where I am about to Go
        s.push(move_to_room)

        # Add to traversal path Where i am about to Go
        traversal_path.append(move_to_room)

        # Go There
        player.travel(move_to_room)

        # fill in journal For first and second room
        second_room = player.current_room.id

        journal[first_room][move_to_room] = second_room
        opposite_dir = get_opposite(move_to_room)
        journal[second_room][opposite_dir] = first_room

        # add to my visited rooms
        my_visited_rooms.add(second_room)

print('ENDING JOURNAL: ', journal)
print('VISITED ROOMS: ', len(my_visited_rooms))
print('GRAPH LENGTH: ', len(room_graph))
print('ENDING ROOM ID: ', player.current_room.id)

###############################################################################

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")