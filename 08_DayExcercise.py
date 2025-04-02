##Day 8##
dog = {}

dog = {'name':'Toto',
       'color':'Negro',
       'breed':'Chihuahua',
       'legs':4,
       'age':3}

student = {
    'first_name':'Patricia',
    'last_name':'Esparza',
    'gender':'Female',
    'age':22,
    'marital_status':'single',
    'skills':['Python','SQL','HTML','CSS','JS'],
    'country':'England',
    'city':'London',
    'addres':{
        'street':'kozani'
        'zipcode':'20298'
    }
}

print(f'The lenght of the student dictionary is {len(student)}')
print(f'The data type of student skills is {type(student["skills"])}')

student['skills'].append('PHP')
print(student['skills'])

keyList = list(student.keys())
print(keyList)

valList = list(student.values())
print(valList)

studentTuple = student.items()
print(studentTuple)

student.pop('gender')
print(student)

del dog