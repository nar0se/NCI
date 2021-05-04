import os 
from os import system
from colorama import Fore 

system('cls')

computers = ['Toshiba', 'Dell', 'MacBook Pro', 'iMac', 'HP', 'Microsoft']
print(computers)

for computer in computers:
    print(computer)

# 5 lists [5 teams]
# team1 = ['Pushpa', 'Aicha', 'Omer', 'Andres', 'Andrew', 'Olivia']
# team2 = ['Daniel', 'Byron', 'Brian', 'Robert', 'Joven', 'Christelle']
# team3 = ['Mtagui', 'Essie', 'James', 'Jane', 'Li_Jin', 'Jeff']
# team4 = ['Yordanos', 'Joe', 'John', 'Kylan', 'Laan', 'Rachid']
# team5 = ['Rufina', 'TB', 'Yasemin', 'Terrel', 'Yasin']

# myList = [
#     [1, 2, 3],
#     ['Dunieski', 'Carlos'],
#     [2.4, 5.6, 7.8],
#     [{'name': 'Dunieski'},{'age': 45}],
#     [(4, 5, 6, 7), (6, 7, 4, 7)]
# ]


teamCounter = 1
# list of lists
teams = [
    ['Pushpa', 'Aicha', 'Omer', 'Andres', 'Andrew', 'Olivia'],
    ['Daniel', 'Byron', 'Brian', 'Robert', 'Joven', 'Christelle'],
    ['Mtagui', 'Essie', 'James', 'Jane', 'Li_Jin', 'Jeff'],
    ['Yordanos', 'Joe', 'John', 'Kylan', 'Laan', 'Rachid'],
    ['Rufina', 'TB', 'Yasemin', 'Terrel', 'Yasin']
]
# this will print each team
def printTeam(team):
    for member in team:
        print(Fore.RED, f'{member}')

# this will pass each team to the function in line 39
for team in teams:
    print(Fore.BLUE, f'Team # {teamCounter}')
    printTeam(team)
    teamCounter += 1


    # member <- team <- list of teams