import random
import json
volunteerlist = {}

def addVolunteer(name, position, team):
    volunteerlist[str(name+position+team)] = {'name': name, 'position': position, 'team': team}

addVolunteer('John', 'Judge', '1')
addVolunteer('Jane', 'Referee', '2')
addVolunteer('Jack', 'Scorekeeper', '3')
addVolunteer('Jill', 'Inspector', '4')
addVolunteer('Joe', 'Scorekeeper', '5')
addVolunteer('Joaquin', 'Judge', '6')
addVolunteer('Jasmine', 'Referee', '7')
addVolunteer('Javier', 'Inspector', '8')
addVolunteer('Jenny', 'Judge', '9')
addVolunteer('Jesse', 'Referee', '10')
addVolunteer('Jin', 'Scorekeeper', '11')
addVolunteer('Jocelyn', 'Inspector', '12')
addVolunteer('Joel', 'Judge', '13')
addVolunteer('Jolene', 'Referee', '14')

def returnVolunteerList():
    return json.dumps(volunteerlist)