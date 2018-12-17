"""
Prints out all of the available courses for that specific program and year in a neat, table form.
"""
def print_course_table(courses, units, names):
    total = 0
    
    print("""


        Here is a list of the courses you could do:
        
        |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
        ||||  Course    ||||| Units |||||||||||||||||||||||||||||  Name  ||||||||||||||||||||||||||||||||||||||||||||||||||||||
        |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
        """, end = "")

    while total < len(courses):
        if total == 0:
            print("||||  ", end="")
            print(courses[total], end="  |||||   ")
            print(units[total], end="   |||||  ")
            print(names[total], end="\n")
        elif total == len(courses)-1:
            print("        ||||  ", end="")
            print(courses[total], end="  |||||   ")
            print(units[total], end="   |||||  ")
            print(names[total], end="")
        else:
            print("        ||||  ", end="")
            print(courses[total], end="  |||||   ")
            print(units[total], end="   |||||  ")
            print(names[total], end="\n")
        total += 1
    print("""
        |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
        """)




def print_program_table(code, name):
    total = 0
    previous = None

    print("""


        Here is a list of all the undergraduate programs provided by The University of Queensland as of today:
        
        |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
        ||||    Program Code    |||||||||||||||||||||||||||||||||||||||||  Program Name  ||||||||||||||||||||||||||||||||||||||
        |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
        """, end = "")

    while total < len(code):
        if name[total] == previous:
            continue
        elif total == 0:
            print("||||    ", end="")
            print(code[total], end="  |||||   ")
            print(name[total], end="\n")
        elif total == len(code)-1:
            print("        ||||  ", end="")
            print(code[total], end="  |||||   ")
            print(name[total], end="\n")
        else:
            print("        ||||  ", end="")
            print(code[total], end="  |||||   ")
            print(name[total], end="\n")
        total += 1
        previous = name[total]
    print("""
        |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
        """)
