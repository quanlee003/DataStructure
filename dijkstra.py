import math

def create_graph_list_from_file():
    f = open('doc.txt')
    num_of_vertex = int(f.readline().strip()) #strip is used to remove to first line of the file
    num_of_edge = f.readlines()
    f.close()

    graph_list = [[0 for _ in range(num_of_vertex)] for _ in range(num_of_vertex)]
    
    for item in num_of_edge:
        item = item.strip() #strip to delete space if not the item will = '0   2   5\n'
        item_list = item.split()
        # This if is to check if the value input is in the correct format or not
        # In this case it has to be 3 value need to be filled 
        if len(item_list) != 3:
            continue
        rows = int(item_list[0])
        cols = int(item_list[1])
        distance = int(item_list[2])
        graph_list[rows][cols] = distance # Distance from one way travel in the list
        graph_list[cols][rows] = distance # Distance from the back way travel in the list
    # End for
    return graph_list
    #Graph list is an array [[0, 10, 5, 15, 9],[10, 0, 15, 7, 8],[5, 15, 0, 40, 25],[15, 7, 40, 0, 2],[9, 8, 25, 2, 0]]
#End def


def path_travel(list_of_previous_vertex, end_point):
    # Create a list have an endpoint but no previous point just to add the path travel from backwards
    list = [end_point]
    vertex = end_point
    while True:
        vertex = list_of_previous_vertex[vertex]

        #The if command is to check if the vertex path travel has the previous vertex or not
        if vertex == None: #if the vertex has no previous vertex
            break
        # End if

        #Because it has no previous vertex so we insert it to the list with the index 0
        list.insert(0, vertex)

    # End while
    list = [str(x) for x in list]
    return '->'.join(list)
# End def



def shortest_path(list_of_distance, list_of_shortest_path):
    mininum_path = math.inf # Set min path is equal to infinity now
    for vertex in range(len(list_of_distance)):

        # Check if the current point has less distance travel than the previous minimum path
        #and also it has not been check in the shortest list path
        if (list_of_distance[vertex] < mininum_path and list_of_shortest_path[vertex] == False):
            mininum_path = list_of_distance[vertex]
            mininum_vertex = vertex
        # End if
    # End for
    return mininum_vertex
# End def



def dijkstra(graph, start_point):
    num_of_vertex = len(graph)
    list_of_distance = [math.inf] * num_of_vertex # Create a list with a distance
    list_of_distance[start_point] = 0 # Set distance to start point is 0 because its from start point to start point
    
    # List of shortest path has the index is the distance path travel, when this index is this minimum path the value is True, other wise 
    #its False
    list_of_shortest_path = [False] * num_of_vertex 

    # Create a list of previous path full of none because of the none travel
    list_of_previous_path = [None] * num_of_vertex  

    # Check all the distance to other vertexes from the start point
    for i in range(num_of_vertex):

        # Take the shortest path to assign as the previous path
        x = shortest_path(list_of_distance, list_of_shortest_path)

        # Approve the shortest path the approve the list of shortest path
        list_of_shortest_path[x] = True

        # Update the distance from the approved point above to all the adjacent point (represent as y) 
        for y in range(num_of_vertex):
            # First condition is to check that between the X point and the Y point has the path or not
            # Second condition is to check that y are approved or not in the list of shortest path
            # Final condition is to check that if distance to Y that is not approved is greater than the distance that we want to approve 
            #then update the smaller path 
            # Cycle the loop until the list of distance cannot update anymore so we out loop to approved it
            if graph[x][y] > 0 and list_of_shortest_path[y] == False and list_of_distance[y] > list_of_distance[x] + graph[x][y]:
                list_of_distance[y] = list_of_distance[x] + graph[x][y]
                list_of_previous_path[y] = x

            # End if
        # End for
    # End for
                
    list_of_minimum_path=[]

    for end_point in range(num_of_vertex):
        output = str(end_point) + " : "
        output += path_travel(list_of_previous_path, end_point) + " : "
        output += str(list_of_distance[end_point])
        print(output)
        # list_of_minimum_path.append(list_of_distance[end_point])
    # End for
        
    # return list_of_minimum_path
# End def
    

def optimum_path(number_of_vertex, list_of_minimum_path, unvisited_list, optimum_path_list):
    for i in range(number_of_vertex):
        if list_of_minimum_path[i] == 0:
            list_of_minimum_path[i] = math.inf
        elif i in optimum_path_list:
            list_of_minimum_path[i] = math.inf
    
    end_point = list_of_minimum_path.index(min(list_of_minimum_path))
    unvisited_list.remove(end_point)
    optimum_path_list.append(end_point)

    
    return optimum_path_list

def main():
    graph = create_graph_list_from_file()
    unvisited_list = []
    for i in range(len(graph)):
        unvisited_list.append(i)
    unvisited_list.pop(0)
    optimum_path_list = [0]

    # while unvisited_list != []:
    # for i in range(len(graph)-1):
    #     print("Start point: " + str(optimum_path_list[-1]))
    #     optimum_path(len(graph), dijkstra(graph, optimum_path_list[-1]), unvisited_list, optimum_path_list)
    #     print("---------")
    # # End for
    # print("Start point: " + str(optimum_path_list[-1]))
    # dijkstra(graph, optimum_path_list[-1])
    # print("---------")

    for i in range(len(graph)):
        print("Start point: " + str(i))
        dijkstra(graph, i)
        print("---------")


    optimum_path_list.append(0)
    optimum_list = []
    
    optimum_list = [str(x) for x in optimum_path_list]
    path = " -> ".join(optimum_list)
    print("Optimum path: " + path)
# End def


if __name__ == '__main__':
    main()
# End if
