# In this program, we are going to play with some dictionaries made from hurricanes data.

# Names of hurricanes

names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 
'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 
'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# Months of hurricanes

months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 
'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 
'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# Years of hurricanes

years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992,
 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# Maximum sustained winds (mph) of hurricanes

max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 
165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# Areas affected by each hurricane

areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 
'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], 
['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 
'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], 
['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], 
['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 
'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 
'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 
'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], 
['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 
'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 
'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], 
['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 
'United States Gulf Coast (especially Florida Panhandle)']]

# Damages (USD($)) of hurricanes

damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', 
'208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', 
'1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# Deaths for each hurricane

deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# This function converts string damage values to float ones. B indicates 1000000000 and M indicates 1000000

def damage_update(list):
    
    new_damages = []
    
    for item in list:
        if item[-1] == 'B':
            new_damages.append(float(item[:-1])*1000000000)
        elif item[-1] == 'M':
            new_damages.append(float(item[:-1])*1000000)
        else:
            new_damages.append(item)

    return new_damages

new_damages_list = damage_update(damages)

# This function gathers all data together in one dictionary in the below format:

# { 'Cuba I': {'Name': 'Cuba I', 
# 'Month': 'October', 
# 'Year': 1924, 
# 'Max Sustained Wind': 165, 
# 'Areas Affected': ['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], 
# 'Damage': 'Damages not recorded', 
# 'Deaths': 90}}

def construct_hurricane_dict(names, months, years, max_sustained_winds, areas_affected, damages, deaths):

    hurricanes = {}

    for i in range(len(names)):
        hurricanes[names[i]] = {
          'Name': names[i],
          'Month': months[i],
          'Year': years[i],
          'Max Sustained Wind': max_sustained_winds[i],
          'Areas Affected': areas_affected[i],
          'Damage': damages[i],
          'Death': deaths[i],
        }
    
    return hurricanes

hurricanes = construct_hurricane_dict(names, months, years, max_sustained_winds, areas_affected, new_damages_list, deaths)

# print(hurricanes)

# This function gathers hurricanes data using years as keys. The format is as below:

# {1932: [
# {'Name': 'Bahamas', 'Month': 'September', 'Year': 1932, 'Max Sustained Wind': 160, 
# 'Areas Affected': ['The Bahamas', 'Northeastern United States'], 'Damage': 'Damages not recorded', 'Deaths': 16}, 
# {'Name': 'Cuba II', 'Month': 'November', 'Year': 1932, 'Max Sustained Wind': 175, 
# 'Areas Affected': ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], 'Damage': 40000000.0, 'Deaths': 3103}
# ]
# }

def convert_hurricanes (hurricanes):

    new_dict = {}

    for key in hurricanes.keys():
        year = hurricanes[key]['Year']
        
        if year in new_dict.keys():
            new_dict[year].append(hurricanes[key])
        else:
            new_dict[year] = [hurricanes[key]]
        
    return new_dict

hurricanes_by_year = convert_hurricanes(hurricanes)

# print(hurricanes_by_year)

# This function counts how often each area is listed as an affected area of a hurricane.

def area_counter(areas_affected):

    counter = {}

    for item in areas_affected:
        
        for area in item:
            already_counted = counter.get(area, 0)
            
            if already_counted == 0:
                counter[area] = 1
            else:
                counter[area] += 1
    
    return counter

areas_counts = area_counter(areas_affected)

# print(areas_counts)

# This function finds the area affected by the most hurricanes, and how often it was hit.

def max_impact_area(areas_counts):

    max_val = max(list(areas_counts.values()))
    max_areas = []

    for key, value in areas_counts.items():

        if value == max_val:
            max_areas.append(key)
    
    return max_val, max_areas

max_val, max_areas = max_impact_area(areas_counts)

# print(max_val, max_areas)

# This function finds the hurricane that caused the greatest number of deaths, and how many deaths it caused.

def max_death_finder(hurricanes):

    death_counts = []
    
    for key in hurricanes:
        death_counts.append(hurricanes[key]['Death'])
    
    max_val = max(death_counts)
    max_death_hurricanes = []

    for key in hurricanes:

        if hurricanes[key]['Death'] == max_val:
            max_death_hurricanes.append(hurricanes[key]['Name'])
    
    return max_val, max_death_hurricanes

max_val, max_death_hurricanes = max_death_finder(hurricanes)

# print(max_val, max_death_hurricanes)

# This function rates hurricanes on a mortality scale according to the following ratings:

# category 0: deaths in [0, 100)
# category 1: deaths in [100, 500)
# category 2: deaths in [500, 1000)
# category 3: deaths in [1000, 10000)
# category 4: deaths in [10000, inf)

def categorize_by_mortality(hurricanes):

    hurricanes_by_mortality = {0:[], 
    1:[], 
    2:[], 
    3:[], 
    4:[], 
    5:[]}

    for key in hurricanes:
        death = hurricanes[key]['Death']

        if death < 100:
            hurricanes_by_mortality[0].append(hurricanes[key]['Name'])
        elif death > 100 and death < 500:
            hurricanes_by_mortality[1].append(hurricanes[key]['Name'])
        elif death > 500 and death < 1000:
            hurricanes_by_mortality[2].append(hurricanes[key]['Name'])
        elif death > 1000 and death < 10000:
            hurricanes_by_mortality[3].append(hurricanes[key]['Name'])
        else:
            hurricanes_by_mortality[4].append(hurricanes[key]['Name'])

    return hurricanes_by_mortality

hurricanes_mortality_scales = categorize_by_mortality(hurricanes)

# print(hurricanes_mortality_scales)

print('\nThanks for reviewing')

# Thanks for reviewing 
