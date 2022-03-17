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
retain = []
def dollar_damages(list_of_damages):
  retain = []
  dollar = 0
  for d in list_of_damages:
    if d == "Damages not recorded":
      retain.append(d)
    elif "M" in d:
      number = d[:-1]
      #print(number)
      dollar = float(number) * 1000000
      retain.append(dollar)
    elif "B" in d:
      number = d[:-1]
      dollar = float(number) * 1000000000
      retain.append(dollar)
  return retain


# test function by updating damages
updated_damages = (dollar_damages(damages))

# 2
# Create a Table


# Create and view the hurricanes dictionary
def hurricane_directory(name_list, month_list, years_list,  wind_list, areas_list, damage_list, death_list=0):
  directory = {}
  i = 0
  while i < len(name_list):
    for nm in name_list:
      directory[nm] = {'Name':nm}
    for nm in directory.keys():
      directory[nm].update({
        'Month':month_list[i],
        'Year':years_list[i],
        'Max Sustained Wind': wind_list[i],
        'Areas Affected': areas_list[i],
        'Damage': damage_list[i],
        'Deaths': death_list[i]})
      #if directory[nm] not in directory:
      #directory[nm].update({'Month':months_list[i])
      i += 1
  #print(directory)
  return directory

#Calling Function
hd = hurricane_directory(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)
print(hd)

# 4
# Organizing by Year
useable_years = []
for year in years:
  if year not in useable_years:
    useable_years.append(year)
#print(useable_years)

def years_directory(years_list, hurricane_directory):
  years_dictionary = {}
  for year in years_list:
    years_dictionary[year] = []
  for year in years_dictionary.keys():
    #print(year)
    for name in hurricane_directory.keys():
      #print(name)
      if year in hurricane_directory[name].values():
        #print(year)
        #print(hurricane_directory[name])
        correct_hurricane = hurricane_directory[name]
        years_dictionary[year].append(correct_hurricane)
        #print(year, " :", years_dictionary[year], "\n")

  return years_dictionary


# create a new dictionary of hurricanes with year and key

#test
new_year_dict = years_directory(years, hd)
print(new_year_dict)


# 5
# Counting Damaged Areas

# create dictionary of areas to store the number of hurricanes involved in
def area_count(areas_list):
  results = {}
  affected_areas = []
  for nest_list in areas_list:
    for location in nest_list:
      if location not in affected_areas:
        affected_areas.append(location)
  #print(affected_areas)
  all_areas = []
  for nested_list in areas_list:
    for location in nested_list:
      all_areas.append(location)
  #print(all_areas)

  for area in affected_areas:
    results[area] = all_areas.count(area)
  return results

#test
test_area = area_count(areas_affected)
print(test_area)


# 6
# Calculating Maximum Hurricane Count

# find most frequently affected area and the number of hurricanes involved in
def max_hit_location(area_count):
  #print(most_affected)
  for location, value in area_count.items():
    if value == max(area_count.values()):
      answer = location + " : " + str(value)
  return answer


#test
most_hit = max_hit_location(test_area)
print(most_hit)


# 7
# Calculating the Deadliest Hurricane

# find highest mortality hurricane and the number of deaths
def deadliest_hurricane(hurricane_directory):
  list_o_deaths = []
  for hurricane in hurricane_directory.keys():
    for data in hurricane_directory[hurricane]:
      if hurricane_directory[hurricane]['Deaths'] not in list_o_deaths:
        list_o_deaths.append(hurricane_directory[hurricane]['Deaths'])
      if hurricane_directory[hurricane]['Deaths'] == max(list_o_deaths):
        deadliest_hurricane_data = hurricane_directory[hurricane]
  deadliest_hurricane = deadliest_hurricane_data['Name'] + ". " + str(deadliest_hurricane_data['Deaths'])

  return 'The deadliest hurricane was {} people died.'.format(deadliest_hurricane)

deadly_test = deadliest_hurricane(hd)
print(deadly_test)

# 8
# Rating Hurricanes by Mortality
mortality_scale = {
  0:0,
  1:100,
  2:500,
  3:1000,
  4:10000
}

# categorize hurricanes in new dictionary with mortality severity as key
def mortality_directory(mortality_ratings, hurricane_directory):
  mort_dir = {
    0 :[],
    1 :[],
    2 :[],
    3 :[],
    4 :[],
    5: []
  }


  for scale in mortality_ratings.values():
    #print(scale)
    for hurricane in hurricane_directory.keys():
      #print(hurricane)
      for data in hurricane_directory[hurricane]:
        if (hurricane_directory[hurricane]['Deaths'] > 10000) and hurricane_directory[hurricane] not in mort_dir[5] :
            mort_dir[5].append(hurricane_directory[hurricane])
            #print(mort_dir[5])
        elif 1000 < hurricane_directory[hurricane]['Deaths'] <= 10000 and hurricane_directory[hurricane] not in mort_dir[4]:
          mort_dir[4].append(hurricane_directory[hurricane])
        elif 500 < hurricane_directory[hurricane]['Deaths'] <= 1000 and hurricane_directory[hurricane] not in mort_dir[3]:
          mort_dir[3].append(hurricane_directory[hurricane])
        elif 100 < hurricane_directory[hurricane]['Deaths'] <= 500 and hurricane_directory[hurricane] not in mort_dir[2]:
          mort_dir[2].append(hurricane_directory[hurricane])
        elif 0 < hurricane_directory[hurricane]['Deaths'] <= 100 and hurricane_directory[hurricane] not in mort_dir[1]:
          mort_dir[1].append(hurricane_directory[hurricane])
        elif hurricane_directory[hurricane]['Deaths'] <= 0 and hurricane_directory[hurricane] not in mort_dir[0]:
          mort_dir[0].append(hurricane_directory[hurricane])

  return mort_dir
#test
mortality_rating = mortality_directory(mortality_scale, hd)
print(mortality_rating)

# 9 Calculating Hurricane Maximum Damage

# find highest damage inducing hurricane and its total cost

def costliest_hurricane(hurricane_directory):
  list_o_damage = []
  for hurricane in hurricane_directory.keys():
    for data in hurricane_directory[hurricane]:
      if hurricane_directory[hurricane]['Damage'] != 'Damages not recorded':
        if hurricane_directory[hurricane]['Damage'] not in list_o_damage:
          list_o_damage.append(hurricane_directory[hurricane]['Damage'])
        if hurricane_directory[hurricane]['Damage'] == max(list_o_damage):
          costliest_hurricane_data = hurricane_directory[hurricane]
  costliest_hurricane = costliest_hurricane_data['Name'] + " with costs of " + str(costliest_hurricane_data['Damage'])

  return 'The costliest hurricane was {}.'.format(costliest_hurricane)

costly_test = costliest_hurricane(hd)
print(costly_test)

# 10
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}

# categorize hurricanes in new dictionary with damage severity as key

def damages_directory(damage_ratings, hurricane_directory):
  dmg_dir = {
    0 :[],
    1 :[],
    2 :[],
    3 :[],
    4 :[],
    5: []
  }


  for scale in damage_ratings.values():
    for hurricane in hurricane_directory.keys():
      for data in hurricane_directory[hurricane]:
        #scale 5
        if hurricane_directory[hurricane]['Damage'] != 'Damages not recorded':
          if (hurricane_directory[hurricane]['Damage']) > 50000000000 and hurricane_directory[hurricane] not in dmg_dir[5] :
            dmg_dir[5].append(hurricane_directory[hurricane])
        #scale 4
          elif 10000000000 < hurricane_directory[hurricane]['Damage'] <= 50000000000 and hurricane_directory[hurricane] not in dmg_dir[4]:
            dmg_dir[4].append(hurricane_directory[hurricane])
        #scale 3
          elif 1000000000 < hurricane_directory[hurricane]['Damage'] <= 10000000000 and hurricane_directory[hurricane] not in dmg_dir[3]:
            dmg_dir[3].append(hurricane_directory[hurricane])
        #scale 2
          elif 100000000 < hurricane_directory[hurricane]['Damage'] <= 1000000000 and hurricane_directory[hurricane] not in dmg_dir[2]:
            dmg_dir[2].append(hurricane_directory[hurricane])
        #scale 1
          elif 0 < hurricane_directory[hurricane]['Damage'] <= 100000000 and hurricane_directory[hurricane] not in dmg_dir[1]:
            dmg_dir[1].append(hurricane_directory[hurricane])
        #scale 0
          elif hurricane_directory[hurricane]['Damage'] <= 0 and hurricane_directory[hurricane] not in dmg_dir[0]:
            dmg_dir[0].append(hurricane_directory[hurricane])

  return dmg_dir

#test
damages_rating_test = damages_directory(mortality_scale, hd)
print(damages_rating_test )
