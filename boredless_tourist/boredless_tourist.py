# This program, briefly, matches the attractions in a given destination
# with the interests of a given tourist who is heading to that destination

# Making a list of destinations you want to cover in the following format:
# destinations = ['Paris, France', 'Shanghai, China']

destinations = []
destination = None

while destination != 'Done':

    # input example: Paris, France
    destination = input("Enter destination in the given format or enter Done when you are done:\ninput example: Paris, France\n ")
    if destination != 'Done':

        destinations.append(destination)

#print(destinations)

# This function matches the destination of a traveler to the list of destinations and returns
# the index of the traveler's destination in destinations list

def get_destination_index(destination):

    dest_index = None
    for i in range(len(destinations)):

        #print('i is: ', i)
        #print('destinations [i] is: ', destinations[i])
        if destinations[i] != destination: continue
        
        else:
            
            dest_index = i
            #print('dest_index is: ', dest_index)
            break
    
    #print('dest_index is: ', dest_index)
    return dest_index

# Maing a list of attractions per each destination; for now as a list of empty lists

attractions=[]
for i in destinations:
    
    attractions.append([])

#print(attractions)

# This funciton takes a destination and a list of attractions with their tags and adds
# each attraction with its tags to the corresponding index in the attractions list as
# the index of the destination in the destinations list. It returns the full attractions list

def add_attraction(destination, attraction):
      
  destination_index = None
  destination_index = get_destination_index(destination)
  #print('destination index is: ', destination_index)
  attractions_for_destination = attractions[destination_index]
  #print('attractions_for_destination is: ', attractions_for_destination)
  attractions_for_destination.append(attraction)
  #print('new attractions_for_destination is: ', attractions_for_destination)
  #print('attractions is: ', attractions)
  return attractions

# Making a list of attractions in the following format:
# attractions = [[["the Louvre", ["art", "museum"]], ["Arc de Triomphe", ["historical site", "monument"]]],
# [["Yu Garden", ["garden", "historcical site"]], ["Yuz Museum", ["art", "museum"]]]]

destination_attraction = None
while destination_attraction != 'Done':
    
    # input example: Paris, France-the Louvre-art-museum
    # input after transformation: ["Paris, France", ["the Louvre", ["art", "museum"]]]
    destination_attraction = input('Enter destination_attraction pair in the given format or enter Done when you are done:\ninput example: Paris, France-the Louvre-art-museum\n ')
    if destination_attraction != 'Done':
        
        dashpos1 = destination_attraction.find('-')
        #print('dashpos1 ', dashpos1)
        dashpos2 = destination_attraction.find('-', (dashpos1+1))
        #print('dashpos2 ', dashpos2)
        dest = destination_attraction[:dashpos1]
        #print('dest is', dest)
        attr_name = destination_attraction[(dashpos1+1):dashpos2]
        #print('attr_name is ', attr_name)
        attr_tags = destination_attraction[(dashpos2+1):].split('-')
        #print('attr_tags is ', attr_tags)
        attr = []
        attr.append(attr_name)
        attr.append(attr_tags)
        #print('attr is', attr)
        add_attraction(dest, attr)

# Making a list of tourists each of whch is in the following format:
# travelers = [['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']], ...]

travelers = []
traveler = None
while traveler != 'Done':
    
    # input example: Erin Wilkes-Shanghai, China-historical site-art
    # input after transformation: ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]
    traveler = input('Enter traveler in the given format or enter Done when you are done:\ninput example: Erin Wilkes-Shanghai, China-historical site-art\n ')
    if traveler != 'Done':
        
        dashpos1 = traveler.find('-')
        dashpos2 = traveler.find('-', dashpos1+1)
        traveler_name = traveler[:dashpos1]
        traveler_destination = traveler[dashpos1+1:dashpos2]
        traveler_interests = traveler[dashpos2+1:].split('-')
        traveler_info = []
        traveler_info.append(traveler_name)
        traveler_info.append(traveler_destination)
        traveler_info.append(traveler_interests)
        #print('traveler is ', traveler_info)
        travelers.append(traveler_info)
        #print('travelers is: ', travelers)

# We will use this list eventually to aggregate all suggestions in one place
Suggestions_list = []

for traveler in travelers:

    # This function uses the second element of traveler list as the destination and searches in the
    # destinations list for that destination and returns its index in the destinations list

    def get_traveler_destination(traveler):
  
        traveler_destination_index = None
  
        traveler_destination = traveler [1]
        traveler_destination_index = get_destination_index (traveler_destination)
        #print('traveler_destination_index is', traveler_destination_index)
        return traveler_destination_index
    
    # retrieving the index of traveler's destination

    traveler_destination_index = get_traveler_destination(traveler)

    # This function uses traveler's destination to find the corresponding attractions of that destination
    # and then, matches the interests of the traveler with the tags of the destination to find out the
    # attractions which might be of interest for the traveler. It returns a list of those attractions.

    def find_attractions(destination, interests):
        
        destination_index = None
        possible_attraction = None
        destination_index = get_destination_index(destination)
        #print('destination_index is: ', destination_index)
        attractions_in_city = attractions[destination_index]
        #print('attractions in city is: ', attractions_in_city)
        attractions_with_interest = []
        for i in attractions_in_city:
            
            possible_attraction = i
            #print('possible attraction is: ', possible_attraction)
            attraction_tags = i[1]
            #print('attraction_tags is: ', attraction_tags)
            for interest in interests:
                
                if interest in attraction_tags:
                    
                    attractions_with_interest.append(possible_attraction[0])
                    #print('attractions_with_interest is: ', attractions_with_interest)
        #print('attractions_with_interest is: ', attractions_with_interest)
        return attractions_with_interest

    # This function uses the information about each traveler to finally combine the first name, last name,
    # where he/she is going and his/her attractions of interest to suggest him/her visit those attractions
    # in a message. Note that the result string is added to the final list which includes the paisr of
    # (traveler first name last name, suggestion message)

    def get_attractions_for_traveler(traveler):
        
        traveler_destination = traveler[1]
        traveler_interests = traveler[2]
        traveler_attractions = find_attractions(traveler_destination, traveler_interests)
        #print('traveler_attractions is: ', traveler_attractions)
        interests_string = "Hi " + str(traveler[0]) + ", we think you'll like these places around " + str(traveler[1]) + ": "
        for item in traveler_attractions:
            
            #print('item is: ', item)
            interests_string += (str(item) + " ")
            #print('interests_string is: ', interests_string)
        #print('interests_string is: ', interests_string)
        return interests_string
    
    # retrieving the suggestion message for the traveler

    suggestion_message = get_attractions_for_traveler(traveler)
    #print('suggestion_message is: ', suggestion_message)

    # Adding the (traveler first name last name, suggestion message) pair to the suggestions_list

    Suggestions_list.append((traveler[0], suggestion_message))
    #print('suggestions_list is: ', Suggestions_list)

print(Suggestions_list[:3])

print('\nThanks for reviewing')

# Thanks for reviewing
