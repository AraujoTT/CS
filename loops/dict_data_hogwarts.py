students = [
    {"name": "hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Daco", "house": "Slythrtin", "patronus": None}
]

for student in students:
    print( student['name'],student['house'], student['patronus'], sep = ', ')
