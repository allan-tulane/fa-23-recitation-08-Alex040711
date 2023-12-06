from collections import deque
from heapq import heappush, heappop 

def shortest_shortest_path(graph, source):
    """
    Params: 
      graph.....a graph represented as a dict where each key is a vertex
                and the value is a set of (vertex, weight) tuples (as in the test case)
      source....the source node
      
    Returns:
      a dict where each key is a vertex and the value is a tuple of
      (shortest path weight, shortest path number of edges). See test case for example.
    """
    # Initialize dictionaries to hold the shortest distance and shortest path count for each vertex
    distances = {vertex: float('infinity') for vertex in graph}
    shortest_paths = {vertex: 0 for vertex in graph}
    # The source vertex distance to itself is always 0 and has 0 edges
    distances[source] = 0
    shortest_paths[source] = 0

    # Priority queue to hold the vertices to visit, initialized with the source vertex
    queue = [(0, 0, source)] # (distance, edges, vertex)

    # Process the queue
    while queue:
        # Pop the vertex with the smallest distance (and then by the smallest edge count)
        current_distance, current_edges, current_vertex = heappop(queue)

        # Check all neighbors of the current vertex
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            # If a shorter path is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                shortest_paths[neighbor] = current_edges + 1
                heappush(queue, (distance, current_edges + 1, neighbor))
            # If a path with the same distance but fewer edges is found
            elif distance == distances[neighbor] and current_edges + 1 < shortest_paths[neighbor]:
                shortest_paths[neighbor] = current_edges + 1
                heappush(queue, (distance, current_edges + 1, neighbor))

    # Create the result dictionary
    result = {vertex: (distances[vertex], shortest_paths[vertex]) for vertex in graph}

    return result
    

    
    
def bfs_path(graph, source):
    """
    Returns:
      a dict where each key is a vertex and the value is the parent of 
      that vertex in the shortest path tree.
    """
    # Initialize the queue with the source node
    queue = deque([source])
    # Initialize the parents dictionary. The source has no parent.
    parents = {source: None}
    # While there are elements in the queue
    while queue:
        # Take one element out from the queue
        current = queue.popleft()
        # For all neighbors of the current node
        for neighbor in graph[current]:
            # If the neighbor hasn't been visited yet
            if neighbor not in parents:
                parents[neighbor] = current  # The current node is the parent of the neighbor
                queue.append(neighbor)  # Add the neighbor to the queue for further exploration
    return parents

def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }


    
def get_path(parents, destination):
    """
    Returns:
      The shortest path from the source node to this destination node 
      (excluding the destination node itself). See test_get_path for an example.
    """
    path = []
    # Start from the destination node and work back to the source
    while destination is not None:
        path.append(destination)
        # Move to the next parent node
        destination = parents[destination]
    # Reverse the path to start from the source and exclude the destination itself
    path = path[:-1]  # Exclude the destination node itself if required
    return ' -> '.join(reversed(path))
