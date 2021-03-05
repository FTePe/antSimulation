from igraph import *
from tower_of_hanoi import *


size = 3

def generate_picture(maze,nb_vertices):
    g = Graph()
    g.add_vertices(nb_vertices)
    
    #Creating the vertices names
    list_name = []
    for node in maze.get_intersections():
        list_name.append(node)
    g.vs["name"]=list_name
    print(list_name)
    
    
    #Creating the edges
    for node in maze.get_intersections():
        print(node)
        vertex = maze.get_intersection(node)
        for neighbor in vertex.get_connections():
            frm = g.vs.find(vertex.id)
            to = g.vs.find(neighbor.id)
            path = vertex.adjacent[neighbor]
            if not 'reverse' in path.name: #Don't draw path in both directions
                g.add_edges([(frm,to)])
    
    #g.vs["label"] = g.vs["name"] #uncomment to add labels to the plot
    return g


hanoi = mirror_hanoi(size)
#hanoi = tower_hanoi(size)
#hanoi.show()
g = generate_picture(hanoi,hanoi.num_intersections)


#copy the following in console to get the image (works ok until size 4, messy after that)
layout = g.layout("kk")
plot(g, layout = layout, bbox = (700,700),vertex_size = 10)


