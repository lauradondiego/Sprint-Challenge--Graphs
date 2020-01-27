from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def adventure_traverse(self, starting_room):
        visited_rooms = set()
        path = []
        # add current_room to visited_rooms
        s = Stack()
        # print("s:", s)
        # s.push(player.current_room.id)
        s.push(starting_room) # from line 18
        # v - while there is something in the stack
        while s.size() > 0:
            current_room = s.pop()
            print("Current Room:", current_room)
            if current_room not in visited_rooms:
                visited_rooms.add(current_room) # set
                path.append(current_room) # array
                for vertices in self.get_neighbors(current_room):
                    if vertices not in visited_rooms: 
                        s.push(vertices) # add connecting neighbors
                    print("stack:", s.stack)

        return path

    def make_connections(self, t_path): # t_path is flexible
    #         # implement BFS
    #         # find verts(rooms) in traversal_path that do not connect 
    #         # and run the bfs on them to reverse and check for a new path
        # loop thru array to find rooms that aren't connect
        t_path_modified = t_path.copy()
        for index, room in enumerate(t_path_modified[:-1]): # stop right before last element
            # enumerate gives access to index called index 
            # print(index, room) # prints every room w. index
            neighbors = self.get_neighbors(t_path_modified[index]) # gets first index
            # check getneighbors of both of the rooms
            if t_path_modified[index + 1] not in neighbors: # if the second room is NOT in neighbors
                bfs_result = self.bfs(t_path_modified[index], t_path_modified[index +1]) # run BFS on room were in and room we need to go to 
                # results in an array so use array methods 
                bfs_result.pop() # pop removes last
                bfs_result.pop(0) # removes first element (0)
                print("bfs result", bfs_result)
                t_path_modified[index+1:index+1] = bfs_result # inserts bfs_result list at index+1
                print("t_path_modified", t_path_modified)
                return t_path_modified
                # everytime we modify we stop on line 54
        return t_path_modified
# t_path [0, 7, 8, 7, 0, 5, 6, 11, 10, 9, 8, 7, 0, 3, 4, 3, 0, 1, 15, 16, 17, 12, 13, 14, 2]


    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()


    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        If both exist, and a connection from v1 to v2
        """
        if v1 in  self.vertices  and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")


    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]


    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create a queue/stack as appropriate
        queue = Queue()
        # Put the starting point in that
        queue.enqueue(starting_vertex)
        # Make a set to keep track of where we've been
        visited = set()
        # While there is stuff in the queue/stack
        while queue.size() > 0:
        #    Pop the first item
            vertex = queue.dequeue()
        #    If not visited
            if vertex not in visited:
        #       DO THE THING!
                print(vertex)
                visited.add(vertex)
        #       For each edge in the item
                for next_vert in self.get_neighbors(vertex):
        #           Add that edge to the queue/stack
                    queue.enqueue(next_vert)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create a queue/stack as appropriate
        stack = Stack()
        # Put the starting point in that
        stack.push(starting_vertex)
        # Make a set to keep track of where we've been
        visited = set()
        # While there is stuff in the queue/stack
        while stack.size() > 0:
        #    Pop the first item
            vertex = stack.pop()
        #    If not visited
            if vertex not in visited:
        #       DO THE THING!
                print(vertex)
                visited.add(vertex)
        #       For each edge in the item
                for next_vert in self.get_neighbors(vertex):
        #           Add that edge to the queue/stack
                    stack.push(next_vert)


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create a queue/stack as appropriate
        queue = Queue()
        # Put the starting point in that
        # Enstack a list to use as our path
        queue.enqueue([starting_vertex])
        # Make a set to keep track of where we've been
        visited = set()
        # While there is stuff in the queue/stack
        while queue.size() > 0:
        #    Pop the first item
            path = queue.dequeue()
            vertex = path[-1]
        #    If not visited
            if vertex not in visited:
                if vertex == destination_vertex:
                    # Do the thing!
                    return path
                visited.add(vertex)
        #       For each edge in the item
                for next_vert in self.get_neighbors(vertex):
                # Copy path to avoid pass by reference bug
                    new_path = list(path) # Make a copy of path rather than reference
                    new_path.append(next_vert)
                    queue.enqueue(new_path)


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create a queue/stack as appropriate
        stack = Stack()
        # Put the starting point in that
        # Enstack a list to use as our path
        stack.push([starting_vertex])
        # Make a set to keep track of where we've been
        visited = set()
        # While there is stuff in the queue/stack
        while stack.size() > 0:
        #    Pop the first item
            path = stack.pop()
            vertex = path[-1]
        #    If not visited
            if vertex not in visited:
                if vertex == destination_vertex:
                    # Do the thing!
                    return path
                visited.add(vertex)
        #       For each edge in the item
                for next_vert in self.get_neighbors(vertex):
                # Copy path to avoid pass by reference bug
                    new_path = list(path) # Make a copy of path rather than reference
                    new_path.append(next_vert)
                    stack.push(new_path)
## ^ GRAPH CLASS ABOVE

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
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)
print("room graph:", room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)
print("player", player)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
# traversal_path = []
# directions are technically called "exits"
# `player.current_room.id`
# `player.current_room.get_exits()`
# `player.travel(direction)`
graph = Graph() # create a graph
for room in room_graph: #room.graph just gets keys
    graph.add_vertex(room) # this now has all 17 rooms in it
for room in room_graph:
    for edge in room_graph[room][1]:
        graph.add_edge(room, room_graph[room][1][edge])


traversal_path = graph.adventure_traverse(0)
print("traversal_path", traversal_path)
    
fixed_path = graph.make_connections(traversal_path)
# print("fiexpath", fixed_path)
while sum(fixed_path) != sum(traversal_path):
    traversal_path = fixed_path.copy() #make a copy
    fixed_path = graph.make_connections(traversal_path)
    print("traversal_path", traversal_path)
    print("fixed_path", fixed_path)
            
# convert #s to directions
directions = []
for index, room in enumerate(traversal_path[:-1]): # stop right before last element
    for neighbor in room_graph[traversal_path[index]][1]: # targets the obj (keys nswe)
        if room_graph[traversal_path[index]][1][neighbor] == traversal_path[index +1]:
            directions.append(neighbor)

print("directions", directions)
    # traversal_path[index] traversal_path[index +1]

# create the path thats not done yet and then pass in tp 
# call your adventure_traverse() function above

# connections = graph.make_connections(0)
# print("Connection function:", make_connections)
# 0 is starting room 
# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in directions:
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
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")

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
