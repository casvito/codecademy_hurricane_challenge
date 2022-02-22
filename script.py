# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

# test function by updating damages

def updated_damage(damage_list):
  updated_damages = []
  for damage in damage_list:
    if damage == 'Damages not recorded':
      updated_damages.append(damage)
    else:
      prefix = (conversion[damage[-1]])
      updated_damages.append((float(damage[:-1])*prefix))
  return (updated_damages)

# 2 
# Create a Table

hurricane_info = {}
hurricane_data = {}
index = 0
  
# Create and view the hurricanes dictionary

for index in range(len(names)):
  hurricane_data = {"Name": names[index],
  "Month": months[index],
  "Year": years[index],
  "Max_Sustained_Wind": max_sustained_winds[index],
  "Areas_Affected": areas_affected[index],
  "Damage": damages[index],
  "Deaths": deaths[index]}
  hurricane_info.update({names[index]: hurricane_data})
  index += 1

def make_dict(name):
    return hurricane_info[name]

'''print(hurricane_info, '\n')'''
print(hurricane_info["Cuba I"], '\n')

# 3
# Organizing by Year

# create a new dictionary of hurricanes with year and key

def organize_by_year(year):
  hurricane_by_year = {}
  list = []
  for hurricane_data in hurricane_info.values():
    if hurricane_data["Year"] == year:
      list.append(hurricane_data)
      hurricane_by_year.update({year: list})
  return hurricane_by_year

'''print(organize_by_year(1933))'''

# 4
# Counting Damaged Areas

# create dictionary of areas to store the number of hurricanes involved in
affected_areas = {}
def count_damaged_areas(hurricane):
  for data in hurricane.values():
    for area in data["Areas_Affected"]:
      if area not in affected_areas:
        affected_areas.update({area : 1})
      else:
        affected_areas.update({area : affected_areas[area]+1})
  return affected_areas

print(count_damaged_areas(hurricane_info), '\n')

# 5 
# Calculating Maximum Hurricane Count
# find most frequently affected area and the number of hurricanes involved in

def most_affected_area(areas):
  hits = []
  unlucky = {}
  for area,number_of_hits in areas.items():
    hits.append(number_of_hits)
    more_hits = max(hits)
    if affected_areas[area] == more_hits:
      unlucky.update({area : more_hits})
  return unlucky

print('The most affected area was',most_affected_area(affected_areas))


# 6
# Calculating the Deadliest Hurricane
# find highest mortality hurricane and the number of deaths


def deadliest_hurricane(hurricanes):
  most_deadly = {}
  num_of_deaths = 0
  for hurricane in hurricanes.values():
    if hurricane["Deaths"] > num_of_deaths:
      most_deadly.clear() #Empties dictionary
      num_of_deaths = hurricane["Deaths"] 
      most_deadly.update({hurricane['Name']:hurricane["Deaths"]})
  return(most_deadly)

print('The deadliest hurricane was',deadliest_hurricane(hurricane_info))

# 7
# Rating Hurricanes by Mortality
# categorize hurricanes in new dictionary with mortality severity as key

def mortality_rating(hurricane):

  mortality_ratings =  {0: [],1: [],2: [],3: [],4: []}
  for hurricane in hurricane.values():
    if hurricane['Deaths'] < 100:
      mortality_ratings[0].append(hurricane)
    elif hurricane['Deaths'] < 500:
      mortality_ratings[1].append(hurricane)
    elif hurricane['Deaths'] < 1000:
      mortality_ratings[2].append(hurricane)
    elif hurricane['Deaths'] < 10000:
      mortality_ratings[3].append(hurricane)
    else:
      mortality_ratings[4].append(hurricane)
  return(mortality_ratings)

(mortality_rating(hurricane_info))

# 8 Calculating Hurricane Maximum Damage
# find highest damage inducing hurricane and its total cost

index = 0
for hurricane in hurricane_info.values():
  hurricane['Damage'] = (updated_damage(damages)[index])
  index += 1
  
def greatest_damage(hurricanes):
  greatest_damage = {}
  damage = 0
  for hurricane in hurricanes.values():
    if hurricane["Damage"] == "Damages not recorded":
      pass
    elif hurricane["Damage"] > damage:
      greatest_damage.clear() #Empties dictionary
      damage = hurricane["Damage"] 
      greatest_damage.update({hurricane['Name']:hurricane["Damage"]})
  return(greatest_damage)

print(greatest_damage(hurricane_info))

# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  
# categorize hurricanes in new dictionary with damage severity as key

def damage_rating(hurricane):
  damage_ratings =  {0: [],1: [],2: [],3: [],4: []}
  for hurricane in hurricane.values():
    if hurricane['Damage'] == "Damages not recorded" or hurricane['Damage'] < damage_scale[1]:
      damage_ratings[0].append(hurricane)
    elif damage_scale[1] < hurricane['Damage'] < damage_scale[2]:
       damage_ratings[1].append(hurricane)
    elif damage_scale[2] < hurricane['Damage'] < damage_scale[3]:
      damage_ratings[2].append(hurricane)
    elif damage_scale[3] < hurricane['Damage'] < damage_scale[4]:
      damage_ratings[3].append(hurricane)
    else:
      damage_ratings[4].append(hurricane)
  return(damage_ratings)


#print(damage_rating(hurricane_info))



