from room import Room
from player import Player
from world import World

import random
from ast import literal_eval


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)
print("player", player)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = ['n', 's', 'e', 'w']
# directions are technically called "exits"
# `player.current_room.id`
# `player.current_room.get_exits()`
# `player.travel(direction)`
graph = {}  # empty dict


def traverse(player, q=None):
    visited_rooms = {}
    if q == None: # so you dont reset it 
        s = Stack()
    # print("s:", s)
    s.push([player.current_room.id])
    # v - while there is something in the queue
    while s.size() > 0:
        path = q.pop()
        print("path:", path)
        # v - find the last vertex in the path
        current_room = path[-1]
        if current_room not in visited_rooms:
            # v - create a copy w built in python method copy()
            visited_rooms[current_room] = path.copy()
            for exit in graph[last_room]:
                if graph[last_room][exit] == "?":
                    return path
                else:
                    # COMPLETE ELSE (go back to nearest unvisited path)(handles duplicate paths)
                    #BFS queue
                    # print("currentroom:", current_room)
                    return visited_rooms

            traverse(player, q)
            print("traverse", traverse)

    # # v - pick a random direction from traversal_path to move and set to new_curr_room
    # new_curr_room = random.shuffle(traversal_path)
    # # v - add that new_curr)room to the visited_rooms
    # visited_rooms.append(new_curr_room)

traverse(player)
# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")

# NOTE:
# UPER
# PLAN OF ATTACK:
# 1. pick a RANDOM (hint: random method) direction to move from the
# current room (current room = I think = player.current_room)
# 2. go to that room (NEW CURRENT ROOM) and LOG (hint: append) the direction
# 3. go back and LOOP (hint: while or for loop)
# 4. ^ This causes player to walk (STACK) Depth-First Traversal (hint: implement above)
# 5. Reached dead end(node w only 1 path)?
# Reverse(loop? go back?) to nearest room with unexplored path
# using Bredth-First Search (see hw) for a room with the
# value of "?" for the EXIT
# 5. search for exit with value "?" (hint: if exit value == ?)
# or if exit has been explored already:
# put it in your BFS QUEUE
# 6. this BFS from step #5 will return the path as a list of room IDs(001, 015, etc)
# you must convert the list to characters/directions n/s/e/w
# BEFORE adding it to your traversal path
# 7. YOU ARE DONE WHEN ALL PATHS HAVE BEEN EXPLORED!
