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

# write your update damages function here:
conversion = {"M": 1000000,
              "B": 1000000000}
updated_damages = []

def update_damages():
#convert damages list string elements into floats or keep as strings if "Damages not recorded" and insert into new list
    for num in range(len(damages)):
        if damages[num] == "Damages not recorded":
            updated_damages.append("Damages not recorded")
        elif damages[num][-1] == "M":
            x = float(damages[num][:-1])
            y = conversion["M"]
            z = updated_damages.append(x*y)
        elif damages[num][-1] == "B":
            a = float(damages[num][:-1])
            b = conversion["B"]
            c = updated_damages.append(a*b)
    return updated_damages
# test function by updating damages
updated_damages = update_damages()


# write your construct hurricane dictionary function here:
hurricanes = {}
def hurricane_table():
  for name in names:
    idx = names.index(name)
    hurricanes.update({name:{"Name":names[idx],
                        "Months":months[idx],
                        "Years":years[idx],
                        "Max Sustained Wind":max_sustained_winds[idx],
                        "Areas Affected":areas_affected[idx],
                        "Damage":updated_damages[idx],
                        "Deaths":deaths[idx]}})
  return hurricanes
hurricanes = hurricane_table()

# write your construct hurricane by year dictionary function here:

years_dict = {}
for key, value in hurricanes.items():
    years_dict.update({value['Years']:[value]})

# Organizing by Year

print(f"\n", years_dict, f"\n")

# write your count affected areas function here:

def count_affected_areas():
    flatten = sum(areas_affected, [])
    uniq_flatten = sorted(list(set(flatten)))
    area_count = [flatten.count(a) for a in uniq_flatten]
    area_hit_count = dict(zip(uniq_flatten, area_count))
    return area_hit_count

area_counter = count_affected_areas()


# write your find most affected area function here:

def max_hurricane_count(dictionary):
    for name, hit in dictionary.items():
        if hit == max(dictionary.values()):
            max_hit = name, int(hit)
    return f"\nThe area most affected by hurricanes is {max_hit[0]} with a maximum hurricane count of {max_hit[1]}."


print(max_hurricane_count(area_counter))

# write your greatest number of deaths function here:

def deadliest_hurricane(dictionary):
    lst = []
    for key, val in dictionary.items():
        a = val['Deaths']
        lst.append(a)
        fatalities = int(max(lst))
        max_fatalities = key, fatalities
    return f"\nThe most deadly hurricane is hurricane {max_fatalities[0]} with a death count of {max_fatalities[1]:,}. "

# find highest mortality hurricane and the number of deaths
print(deadliest_hurricane(hurricanes))


# write your catgeorize by mortality function here:

scale = {0: 0,
         1: 100,
         2: 500,
         3: 1000,
         4: 10000}

def mortality_scale(dictionary):

    scaled_hurricanes = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
    for k,v in dictionary.items():
        if v["Deaths"] == scale[0]:
            scaled_hurricanes[0].append(v['Name'])
        elif v['Deaths'] <=scale[1] and v['Deaths'] > 0:
            scaled_hurricanes[1].append(v['Name'])
        elif v['Deaths'] <=scale[2] and v['Deaths'] > scale[1]:
            scaled_hurricanes[2].append(v['Name'])
        elif v['Deaths'] <=scale[3] and v['Deaths'] > scale[2]:
            scaled_hurricanes[3].append(v['Name'])
        elif v['Deaths'] <= scale[4] and v['Deaths'] > scale[3] :
             scaled_hurricanes[4].append(v['Name'])
        else:
            scaled_hurricanes[5].append(v['Name'])
    return scaled_hurricanes

# categorize hurricanes in new dictionary with mortality severity as key

scaled_hurricanes = mortality_scale(hurricanes)

# print(f"\n", scaled_hurricanes)
print(f"\nScale 5 hurricanes: ", scaled_hurricanes[5])

# write your greatest damage function here:

def hurricane_maximum(dictionary):
    dam_lst = [thing for thing in updated_damages if not thing=='Damages not recorded']
    maxum = max(dam_lst)
    for key,value in dictionary.items():
        if value['Damage'] == maxum:
        a =  value['Name'], maxum
    return a

# find highest damage inducing hurricane and its total cost

greatest_damage = hurricane_maximum(hurricanes)

print(f"\nThe hurricane that did the most damage is hurricane {greatest_damage[0]} costing a total of ${greatest_damage[1]:,.2f}.")


# write your catgeorize by damage function here:

dam_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}

def damage_scale(dictionary):

    scaled_damages = {0:[], 1:[], 2:[], 3:[], 4:[]}

    for k,v in dictionary.items():
        if v['Damage'] == 'Damages not recorded':
            scaled_damages[0].append(v['Name'])
        elif v['Damage'] <=dam_scale[1] and v['Damage'] > dam_scale[0]:
            scaled_damages[1].append(v['Name'])
        elif v['Damage'] <=dam_scale[2] and v['Damage'] > dam_scale[1] :
            scaled_damages[2].append(v['Name'])
        elif v['Damage'] <=dam_scale[3] and v['Damage'] > dam_scale[2]:
            scaled_damages[3].append(v['Name'])
        elif v['Damage'] <= dam_scale[4] and v['Damage'] > dam_scale[3]:
            scaled_damages[4].append(v['Name'])
    return scaled_damages

scaled_damages = damage_scale(hurricanes)

# categorize hurricanes in new dictionary with damage severity as key

print(f"\n", scaled_damages)
