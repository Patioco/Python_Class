'''
1. Print “Python Assignment 2”
2. Create a python dictionary storing a list of members in the following teams (Alpha Team, Beta Team, Brainy Team, Harvard Team, Stars Team)
3. Print “All the members of the Harvard and the Beta teams”
4. Using list or dictionary(choose the best option to use), create an item storing 10 previous Nigerian presidents with their year of attaining power
5. Print the last 5 presidents stored in no 4 
6. Create a list of your bet 10 Nigerian foods
7. Print the last 5 foods stored in no6
8. Print the 3 middle foods stored in no6
9. Print the 1st to 7th foods stored in no6
10. Please use comments before writing the code for each line
'''

#SOLUTION
print('Python Assignment 2')
#creating given key-value pairs
python_dictionary = {"Alpha_Team":"alpha", "Beta_Team":"beta", "Brainy_Team":"brainy", "Harvard_Team":"harvard", "Stars_Team":"stars"}
#printing required key-value pairs
print(python_dictionary["Harvard_Team"], python_dictionary["Beta_Team"])
#creating list of Nigeria Presidents assumption of office years
past_presidents = {'tinubu':'2023', 'buhari':'2015', 'yaradua':'2007', 'obasanjo':'1999', 'abdulsalam':'1998', 'abacha':'1992', 'babangida':'1985', 'idiagbon':'1984', 'shagari':'1979', 'murtala':'1975'}
#printing required presidents assumption of office years
print(past_presidents['abacha'], past_presidents['babangida'], past_presidents['idiagbon'], past_presidents['shagari'], past_presidents['murtala'])
#my best nigerian foods
best_Nigerian_foods = ['beans', 'abacha', 'akamu', 'corn', 'bread', 'rice', 'egusi', 'eba', 'semo', 'akpu']
#printing required slices from best_Nigerian_foods
print(best_Nigerian_foods[5:])
print(best_Nigerian_foods[4:6])
print(best_Nigerian_foods[0:7])