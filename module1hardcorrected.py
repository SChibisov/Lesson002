journal = {}
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

avarage_grade = []
for i in range(len(grades)):
    avarage_grade.append(sum(grades[i])/len(grades[i]))

# valu_1st = sum(grades[0])/len(grades[0])
# valu_2st = sum(grades[1])/len(grades[1])
# valu_3st = sum(grades[2])/len(grades[2])
# valu_4st = sum(grades[3])/len(grades[3])
# valu_5st = sum(grades[4])/len(grades[4])
# grades[0] = valu_1st
# grades[1] = valu_2st
# grades[2] = valu_3st
# grades[3] = valu_4st
# grades[4] = valu_5st
students = list(students)
students.sort()
# journal = dict(zip(students, grades))

journal = dict(zip(students, avarage_grade))
print(journal)
print(journal['Bilbo'])