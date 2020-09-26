# In this project (a big one I believe), we help commuters get from one landmark to another via metro stations using BFS, 
# and DFS. We assume that it takes the same amount of time to get from each station to each of its 
# connected neighboring stations.

# At first, we define BFS and DFS as below. Further explanation on wht these functions do
# is available at:
# https://github.com/kamyarpakdaman/ComputerScience-Mathematics/tree/master/Algorithms/graph_search_bfs_dfs

def bfs(graph, start_vertex, target_value):
    
    path = [start_vertex]
    vertex_and_path = [start_vertex, path]
    bfs_queue = [vertex_and_path]
    visited = set()
  
    while bfs_queue:

        current_vertex, path = bfs_queue.pop(0)
        visited.add(current_vertex)
      
        for neighbor in graph[current_vertex]:

            if neighbor not in visited:

                if neighbor == target_value:
                    
                    return path + [neighbor]
              
                else:
                    
                    bfs_queue.append([neighbor, path + [neighbor]])


def dfs(graph, current_vertex, target_value, visited = None):

    if visited is None:
        
        visited = []
    
    visited.append(current_vertex)
    
    if current_vertex == target_value:
        
        return visited
    
    for neighbor in graph[current_vertex]:
        
        if neighbor not in visited:
            
            path = dfs(graph, neighbor, target_value, visited)
        
            if path:
                
                return path

# Below, we have the data for all metro stations in Vancouver, Canada. This is actually our graph
# of Vancouver's metro system.

vc_metro = {
  'Richmond-Brighouse': set(['Lansdowne']),
  'Lansdowne': set(['Richmond-Brighouse', 'Aberdeen']),
  'Aberdeen': set(['Lansdowne', 'Bridgeport']),
  'Bridgeport': set(['Aberdeen', 'Templeton', 'Marine Drive']),
  'YVR-Airport': set(['Sea Island Centre']),
  'Sea Island Centre': set(['YVR-Airport', 'Templeton']),
  'Templeton': set(['Sea Island Centre', 'Bridgeport']),
  'Marine Drive': set(['Bridgeport', 'Langara-49th Avenue']),
  'Langara-49th Avenue': set(['Marine Drive', 'Oakbridge-41st Avenue']),
  'Oakbridge-41st Avenue': set(['Langara-49th Avenue', 'King Edward']),
  'King Edward': set(['Oakbridge-41st Avenue', 'Broadway-City Hall']),
  'Broadway-City Hall': set(['King Edward', 'Olympic Village']),
  'Olympic Village': set(['Broadway-City Hall', 'Yaletown-Roundhouse']),
  'Yaletown-Roundhouse': set(['Olympic Village', 'Vancouver City Centre']),
  'Vancouver City Centre': set(['Yaletown-Roundhouse', 'Waterfront']),
  'Waterfront': set(['Vancouver City Centre', 'Burrard']),
  'Burrard': set(['Waterfront', 'Granville']),
  'Granville': set(['Burrard', 'Stadium-Chinatown']),
  'Stadium-Chinatown': set(['Granville', 'Main Street-Science World']),
  'Main Street-Science World': set(['Stadium-Chinatown', 'Commercial-Broadway']),
  'Commercial-Broadway': set(['VCC-Clark', 'Main Street-Science World', 'Renfrew', 'Nanaimo']),
  'VCC-Clark': set(['Commercial-Broadway']),
  'Nanaimo': set(['Commercial-Broadway', '29th Avenue']),
  '29th Avenue': set(['Nanaimo', 'Joyce-Collingwood']),
  'Joyce-Collingwood': set(['29th Avenue', 'Patterson']),
  'Patterson': set(['Joyce-Collingwood', 'Metrotown']),
  'Metrotown': set(['Patterson', 'Royal Oak']),
  'Royal Oak': set(['Metrotown', 'Edmonds']),
  'Edmonds': set(['Royal Oak', '22nd Street']),
  '22nd Street': set(['Edmonds', 'New Westminster']),
  'New Westminster': set(['22nd Street', 'Columbia']),
  'Columbia': set(['New Westminster', 'Sapperton', 'Scott Road']),
  'Scott Road': set(['Columbia', 'Gateway']),
  'Gateway': set(['Scott Road', 'Surrey Central']),
  'Surrey Central': set(['Gateway', 'King George']),
  'King George': set(['Surrey Central']),
  'Sapperton': set(['Columbia', 'Braid']),
  'Braid': set(['Sapperton', 'Lougheed Town Centre']),
  'Lougheed Town Centre': set(['Braid', 'Production Way / University', 'Burquitlam']),
  'Burquitlam': set(['Lougheed Town Centre', 'Moody Centre']),
  'Moody Centre': set(['Burquitlam', 'Inlet Centre']),
  'Inlet Centre': set(['Moody Centre', 'Coquitlam Central']),
  'Coquitlam Central': set(['Inlet Centre', 'Lincoln']),
  'Lincoln': set(['Coquitlam Central', 'Lafarge Lake-Douglas']),
  'Lafarge Lake-Douglas': set(['Lincoln']),
  'Production Way / University': set(['Lougheed Town Centre', 'Lake City Way']),
  'Lake City Way': set(['Production Way / University', 'Sperling / Burnaby Lake']),
  'Sperling / Burnaby Lake': set(['Lake City Way', 'Holdom']),
  'Holdom': set(['Sperling / Burnaby Lake', 'Brentwood Town Centre']),
  'Brentwood Town Centre': set(['Holdom', 'Gilmore']),
  'Gilmore': set(['Brentwood Town Centre', 'Rupert']),
  'Rupert': set(['Gilmore', 'Renfrew']),
  'Renfrew': set(['Rupert', 'Commercial-Broadway'])
  }

# Here, we have a graph mapping the landmarks to their nearest metro station.

vc_landmarks = {
  'Marine Building': set(['Burrard', 'Waterfront']),
  'Scotiabank Field at Nat Bailey Stadium': set(['King Edward']),
  'Vancouver Aquarium': set(['Burrard']),
  'Vancouver Lookout': set(['Waterfront']),
  'Canada Place': set(['Burrard', 'Waterfront']),
  'Cathedral of Our Lady of the Holy Rosary': set(['Vancouver City Centre', 'Granville']),
  'Library Square': set(['Vancouver City Centre', 'Stadium-Chinatown']),
  'B.C. Place Stadium': set(['Stadium-Chinatown']),
  'Lions Gate Bridge': set(['Burrard']),
  'Gastown Steam Clock': set(['Waterfront']),
  'Waterfront Station': set(['Waterfront']),
  'Granville Street': set(['Granville', 'Vancouver City Centre']),
  'Pacific Central Station': set(['Main Street-Science World']),
  'Prospect Point Lighthouse': set(['Burrard']),
  'Queen Elizabeth Theatre': set(['Stadium-Chinatown']),
  'Stanley Park': set(['Burrard']),
  'Granville Island Public Market': set(['Yaletown-Roundhouse']),
  'Kitsilano Beach': set(['Olympic Village']),
  'Dr. Sun Yat-Sen Classical Chinese Garden': set(['Stadium-Chinatown']),
  'Museum of Vancouver': set(['Yaletown-Roundhouse']),
  'Science World': set(['Main Street-Science World']),
  'Robson Square': set(['Vancouver City Centre']),
  'Samson V Maritime Museum': set(['Columbia']),
  'Burnaby Lake': set(['Sperling / Burnaby Lake', 'Lake City Way', 'Production Way / University']),
  'Nikkei National Museum & Cultural Centre': set(['Edmonds']),
  'Central Park': set(['Patterson', 'Metrotown'])
}

# Finally, for the sake of simplicity, we have a dictionary in which we have mapped the landmarks to
# alphabet letters.

landmark_choices = {
  'a': 'Marine Building',
  'b': 'Scotiabank Field at Nat Bailey Stadium',
  'c': 'Vancouver Aquarium',
  'd': 'Vancouver Lookout',
  'e': 'Canada Place',
  'f': 'Cathedral of Our Lady of the Holy Rosary',
  'g': 'Library Square',
  'h': 'B.C. Place Stadium',
  'i': 'Lions Gate Bridge',
  'j': 'Gastown Steam Clock',
  'k': 'Waterfront Station',
  'l': 'Granville Street',
  'm': 'Pacific Central Station',
  'n': 'Prospect Point Lighthouse',
  'o': 'Queen Elizabeth Theatre',
  'p': 'Stanley Park',
  'q': 'Granville Island Public Market',
  'r': 'Kitsilano Beach',
  's': 'Dr. Sun Yat-Sen Classical Chinese Garden',
  't': 'Museum of Vancouver',
  'u': 'Science World',
  'v': 'Robson Square',
  'w': 'Samson V Maritime Museum',
  'x': 'Burnaby Lake',
  'y': 'Nikkei National Museum & Cultural Centre',
  'z': 'Central Park'
}

# Here we go. B-)

# At first, we create a variable that will be a string joining all the landmarks together using their mapped alphabet codes.

landmark_string = ""

for letter, landmark in landmark_choices.items():
    
    landmark_string += "{} - {}\n".format(letter, landmark)

# Further, some stations might be closed. We take care of them here. Using the below function, we omit the closed stations from our data of stations.

stations_under_construction = []

def get_active_stations():

    updated_metro = vc_metro

    for station_under_construction in stations_under_construction:

        for current_station, neighboring_station in vc_metro.items():

            if current_station != station_under_construction:

                updated_metro[current_station] -= set(stations_under_construction)
            
            else:

                updated_metro[current_station] = set([])
    
    return updated_metro

# Simply a welcome function.

def greet():

    print("Hi there! We'll help you find the shortest route between the following Vancouver landmarks:\n" + landmark_string)

# This function handles setting the selected origin and destination points.

def set_start_and_end(start_point, end_point):

    if start_point is not None:

        change_point = input("What would you like to change? You can enter 'o' for 'origin', 'd' for 'destination', or 'b' for 'both': ")

        if change_point == 'b':

            start_point = get_start()
            end_point = get_end()
        
        elif change_point == 'o':

            start_point = get_start()
        
        elif change_point == 'd':

            end_point = get_end()
        
        else:

            print('Wrong answer though!')
            return set_start_and_end(start_point, end_point)
    
    else:

        start_point = get_start()
    
    end_point = get_end()

    return start_point, end_point

# These two functions are respectively used for requesting the origin and the destination from the user.

def get_start():

    start_point_letter = input("Where are you coming from? Type in the corresponding letter: ")

    if start_point_letter in landmark_choices.keys():

        start_point = landmark_choices[start_point_letter]

        return start_point
    
    else:

        print("Sorry, that's not a landmark we have data on. Let's try this again...")
        return get_start()

def get_end():

    end_point_letter = input("Ok, where are you headed? Type in the corresponding letter: ")

    if end_point_letter in landmark_choices.keys():

        end_point = landmark_choices[end_point_letter]

        return end_point
    
    else:

        print("Sorry, that's not a landmark we have data on. Let's try this again...")
        return get_end()

# This function finds the nearest metro stations to origin and destination. Note that, because some landmarks have more than one station, there is sometimes more than one route between landmarks. That means it’s our job to collect all of the shortest routes between stations and then compare them based on path length.

def get_route(start_point, end_point):
    
    start_stations = vc_landmarks[start_point]
    end_stations = vc_landmarks[end_point]

    routes = []

    for start_station in start_stations:

        for end_station in end_stations:
            
            # Updating the metro stations if there are any closed stations.

            if len(stations_under_construction) > 0:

                metro_system = get_active_stations()
            
            else:

                metro_system = vc_metro
            
            # Let's first check if a route exists using dfs().

            if len(stations_under_construction) > 0:

                possible_route = dfs(metro_system, start_station, end_station)

                if possible_route is None:

                    return None

            # Here, we find the shortest path using bfs(). Note that, this route returned from bfs() is a list that represents the path.
            
            route = bfs(metro_system, start_station, end_station)

            if route is not None:

                routes.append(route)
    
    shortest_route = min(routes, key=len)

    return shortest_route

# This function simply display the landmarks.

def show_landmarks():

    see_landmarks = input("Would you like to see the list of landmarks again? Enter y/n: ")

    if see_landmarks == 'y':

        print(landmark_string)
# A recap function for our work so far. We set default values of None because start_point and end_point may need to be defined for the first time or redefined.

def new_route(start_point = None, end_point = None):

    start_point, end_point = set_start_and_end(start_point, end_point)

    shortest_route = get_route(start_point, end_point)

    # Making the shortest route look better.

    if shortest_route:

        shortest_route_string = '\n'.join(shortest_route)

        print("The shortest metro route from {} to {} is:\n{}".format(start_point, end_point, shortest_route_string))
    
    else:

        print("Unfortunately, there is currently no route between {} and {} due to maintenance.".format(start_point, end_point))

    again = input("Would you like to see another route? Enter y/n: ")

    if again == 'y':

        show_landmarks()

        return new_route(start_point, end_point)

# This function makes the ending of the main function smoother. D:

def goodbye():

    print('Thanks for reviewing the landmarks and routes!')

# This is our main program to do the job.

def router():

    greet()

    new_route()

    goodbye()

router()

print('\nThanks for reviewing')

# Thanks for reviewing  
