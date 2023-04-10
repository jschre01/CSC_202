from stack_array import * #Needed for Depth First Search
from queue_array import * #Needed for Breadth First Search

class Vertex:
    '''Add additional helper methods if necessary.'''
    def __init__(self, key):
        '''Add other attributes as necessary'''
        self.id = key
        self.adjacent_to = []
        self.color = None


class Graph:
    '''Add additional helper methods if necessary.'''
    def __init__(self, filename):
        '''reads in the specification of a graph and creates a graph using an adjacency list representation.  
           You may assume the graph is not empty and is a correct specification.  E.g. each edge is 
           represented by a pair of vertices.  Note that the graph is not directed so each edge specified 
           in the input file should appear on the adjacency list of each vertex of the two vertices associated 
           with the edge.'''
        self.adjacency_list = {}
        self.added_list = []
        file = open(filename, "r")
        vertices = []
        for line in file:
            vertices += line.split()
        file.close()
        for i in range(len(vertices)):
            if(vertices[i] in self.adjacency_list):
                if(i % 2 == 0):
                    self.adjacency_list[vertices[i]].adjacent_to.append(vertices[i+1])
                else:
                    self.adjacency_list[vertices[i]].adjacent_to.append(vertices[i-1])
            else:
                if(i % 2 == 0):
                    self.added_list.append(vertices[i])
                    new_vertex = Vertex(vertices[i])
                    new_vertex.adjacent_to.append(vertices[i+1])
                    self.adjacency_list[vertices[i]] = new_vertex
                else:
                    self.added_list.append(vertices[i])
                    new_vertex = Vertex(vertices[i])
                    new_vertex.adjacent_to.append(vertices[i-1])
                    self.adjacency_list[vertices[i]] = new_vertex
            

    def add_vertex(self, key):
        '''Add vertex to graph, only if the vertex is not already in the graph.'''
        if not(key in self.adjacency_list):
            self.added_list.append(key)
            new_vertex = Vertex(key)
            self.adjacency_list[key] = new_vertex

    def get_vertex(self, key):
        '''Return the Vertex object associated with the id. If id is not in the graph, return None'''
        return self.adjacency_list[key]

    def add_edge(self, v1, v2):
        '''v1 and v2 are vertex id's. As this is an undirected graph, add an 
           edge from v1 to v2 and an edge from v2 to v1.  You can assume that
           v1 and v2 are already in the graph'''
        self.adjacency_list[v1].adjacent_to.append(v2)
        self.adjacency_list[v2].adjacent_to.append(v1)

    def get_vertices(self):
        '''Returns a list of id's representing the vertices in the graph, in ascending order'''
        self.added_list.sort()
        return self.added_list

    def conn_components(self): 
        '''Returns a list of lists.  For example, if there are three connected components 
           then you will return a list of three lists.  Each sub list will contain the 
           vertices (in ascending order) in the connected component represented by that list.
           The overall list will also be in ascending order based on the first item of each sublist.
           This method MUST use Depth First Search logic!'''
        vertices = self.get_vertices()
        stack = Stack(len(vertices))
        visited = {}
        vis_num = 0
        conn_list = []
        while(vis_num != len(vertices)):
            i = 0
            while(vertices[i] in visited):
                i += 1
            curr = vertices[i]
            stack.push(vertices[i])
            visited[vertices[i]] = self.adjacency_list[vertices[i]]
            vis_num += 1
            new_list = []
            while(stack.is_empty() == False):
                next_list = self.adjacency_list[curr].adjacent_to
                done = False
                i = 0
                while(i < len(next_list) and done == False):
                    if not(next_list[i] in visited):
                        curr = next_list[i]
                        stack.push(curr)
                        visited[curr] = self.adjacency_list[curr]
                        vis_num += 1
                        done = True
                    else:
                        i += 1
                if(done == False):
                    new_add = stack.pop()
                    new_list.append(new_add)
                    if(stack.is_empty() == False):
                        curr = stack.peek()
            new_list.sort()
            conn_list.append(new_list)
        conn_list.sort()
        return conn_list
        

    def is_bipartite(self):
        '''Returns True if the graph is bicolorable and False otherwise.
           This method MUST use Breadth First Search logic!'''
        vertices = self.get_vertices()
        queue = Queue(len(vertices))
        visited = {}
        vis_num = 0
        while(vis_num != len(vertices)):
            i = 0
            while(vertices[i] in visited):
                i += 1
            curr = vertices[i]
            queue.enqueue(curr)
            visited[curr] = self.adjacency_list[curr]
            vis_num += 1
            self.adjacency_list[curr].color = 'G'
            while(queue.is_empty() == False):
                curr = queue.dequeue()
                next_list = self.adjacency_list[curr].adjacent_to
                for i in next_list:
                    if(i in visited):
                        if(self.adjacency_list[i].color == self.adjacency_list[curr].color):
                            return False
                    else:
                        visited[i] = self.adjacency_list[i]
                        vis_num += 1
                        queue.enqueue(i)
                        if(self.adjacency_list[curr].color == 'G'):
                            self.adjacency_list[i].color = 'B'
                        else:
                            self.adjacency_list[i].color = 'G'
        return True
        
