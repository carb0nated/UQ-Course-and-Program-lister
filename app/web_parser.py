from lxml import html
import requests
import sys
import course_lister
import web_parser

print("""
==============================================================================
                UQ Course and Program Lister v0.9.0 
                            >> UQCPL <<
                                    
                    Created by Fouad Khalaf, 2018.

Important note: this program is NOT affiliated with UQ. Use at your own risk.
==============================================================================
""")



def program_to_lookup():
    done = False
    while (done == False):
        program = input("""
Would you like to inquire about a course or a program?
For a list of program codes, type 'help'. 
    """)
        if program == "help":
            prog_codes = web_parser.get_raw_program_code(
                web_parser.obtain_program_details_from_page())
            prog_names = web_parser.get_raw_program_name(
                web_parser.obtain_program_details_from_page())
            course_lister.print_program_table(prog_codes, prog_names)
        elif program.lower() == "course":
            done = True
            inquire_about_course()
        elif program.lower() == "program":
            done = True
            inquire_about_program()
        else:
            print("Sorry, that was an invalid option.")
            


"""
Communicates with the user if they ask about course information.
"""
def inquire_about_course():
    while True:
        program = input("What program would you like to inquire about? ").upper()
        if len(program) != 10:
            print("That was an invalid program code. It must be in a 10-character format. e.g. SOFTWX2342: ")
            continue
        else:
            'Run parsers and cleanup functions'
            struct = obtain_page_details(program, year_to_lookup())
            info = cleanup_course_info(get_raw_courses_info(struct))
            courses = cleanup_course_list(get_raw_course_code(struct))
            units = cleanup_units_from_courses(get_raw_courses_info(struct))

            'Check for any errors while parsing data'
            check_for_invalid_outliers(info, courses, units)
            
            while True:
                choice = input("What would you like to get the data in the form of? A LIST or a TABLE? ").upper()
                if choice == "LIST":
                    print("Course codes: " + str(courses), end='\n\n')
                    print("Units: " + str(units), end='\n\n')
                    print("Course name: " + str(info), end='\n\n')
                    break
                elif choice == "TABLE":
                    course_lister.print_course_table(courses, units, info)
                    break
                else:
                    print("That was an invalid choice. Please enter either LIST or TABLE. ")
                    continue
            break
    prompt_go_back()



"""
Communicates with the user if they ask about undergraduate programs information.
"""
def inquire_about_program():
    while True:
        choice = input("Would you like the programs to be in the form of a LIST or a TABLE? ").upper()
        if choice == "LIST":
            while True:
                name_or_code = input("Would you like the data to be retured in a 10-char program code or name in plain english? Type CODE or NAME: ").upper()
                if name_or_code != "NAME" and name_or_code != "CODE":
                    print("Invalid choice. Please type either NAME or CODE... ")
                else:
                    break
            if name_or_code == "NAME":
                print(get_raw_program_name(obtain_program_details_from_page()))
            elif name_or_code == "CODE":
                print(get_raw_program_code(obtain_program_details_from_page()))
            break
        elif choice == "TABLE":
            print("WARNING: Feature is still under development...")
            prog_codes = get_raw_program_code(obtain_program_details_from_page())
            prog_names = get_raw_program_name(obtain_program_details_from_page())
            course_lister.print_program_table(prog_codes, prog_names)
            break
        else:
            print("That was an invalid choice. Please enter either LIST or TABLE. ")
    prompt_go_back()



"""
Prompts the user back to the beginning of the program.
Exits the program if 'y' was not entered.
"""
def prompt_go_back():
    choice = input("Would you like to go back? [y/n]")
    if choice == 'y':
        program_to_lookup()
    else:
        sys.exit()



"""
Asks the user to input the year they want to enquire about. It checks for the range
which the user enters, and checks whether it is an integer or not.

Returns: the year which was entered.
"""
def year_to_lookup():
    'What year to obtain for the program'
    while True:
        try:
            year = int(input("What year would you like to retrieve the course lists from? "))
        except ValueError:
            print("Please enter an integer between 2010 and 2020...")
            continue
        if year < 2010 or year > 2020:
            print("Please enter an integer between 2010 and 2020...")
            continue
        else:
            return(year)


"""
Obtains all the data from the webpage.

Returns: data from the webpage in the form of a tree structure.
"""
def obtain_page_details(program, year):
    'Obtain page details'
    page = requests.get(
        'https://my.uq.edu.au/programs-courses/plan_display.html?acad_plan='+str(program)+'&year='+str(year))
    struct = html.fromstring(page.content)
    return(struct)


"""
Returns all data from the webpage with the tag <td>.
"""
def get_raw_courses_info(struct):
    return(struct.xpath('//td/text()'))


"""
Returns all the data from the webpage with the tag <a> within <td>
"""
def get_raw_course_code(struct):
    return(struct.xpath('//td//a/text()'))


"""
Obtains raw data from the undergrad programs web page.
"""
def obtain_program_details_from_page():
    page = requests.get('https://my.uq.edu.au/programs-courses/browse.html?level=ugpg')
    struct = html.fromstring(page.content)
    return(struct)


"""
Returns a list of all available undergrad programs at UQ in the form of a 10-char program code.
"""
def get_raw_program_code(struct):
    program_codes= []
    for x in struct.xpath('//tr//td[@class="plan"]//a'):
        z = x.attrib['href']
        if len(z) == 48:
            program_codes.append(z[38:])
    return(program_codes)


"""
Returns a list of all available undergrad programs at UQ (titles/names).
"""
def get_raw_program_name(struct):
    return(struct.xpath('//tr//td[@class="plan"]//a/text()'))



"""
Cleans up the course list.

Returns: a list containing readable 8 character course codes.
"""
def cleanup_course_list(courses_raw):
    courses=[]
    'Clears up the course list'
    for course in courses_raw:
        if len(course) == 11:
            courses.append(course[3:])
    return(courses)



"""
Cleans up the course info list and removes all unnecessary data.

Returns: a cleaned up list containing only course name.
"""
def cleanup_course_info(courses_info):
    'Clears up the course info list'
    course = 0
    info = []
    for x in courses_info:
        if x == 'Course Code' or x == 'Units' or x == 'Course Title' or len(x) < 4 or x == '[\xa0or':
            continue
        elif type(x) == int:
            continue
        else:
            info.append(x)
    return(info)


"""
Cleans up the tree structure given and filters out everythng but the units each course has.

Returns: an integer representing the number of units the course provides.
"""
def cleanup_units_from_courses(courses_info):
    units = []
    for x in courses_info:
        if len(x) == 1 and x != '\t':
            units.append(x)
    return(units)



"""
Prints out an error message when the length of any of the three lists above do not match.
It then exits the program.
"""
def print_error():
    print("""
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    !!!!! An error has occured. Please contact me on fouad@fouadkhalaf.com and state !!!!!
    !!!!! the program/degree and the year you are enquiring about. Your input is highly !!
    !!!!! appreciated :) !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    ........................... The program will now terminate ...........................

    """)
    sys.exit()



"""
Checks the lists when the length of any of the three lists above do not match and
prints out an error message. It then exits the program.
"""
def check_for_invalid_outliers(info, courses, units):
    if len(info) != len(courses):
        print_error()
    elif len(info) != len(units):
        print_error()
    elif len(courses) != len(units):
        print_error()


"""
Returns a list of all available electives
"""
def get_electives_only(struct):
    None
        


"""
Main function of the program.
"""
def main():
    program_to_lookup()
    

if __name__ == "__main__":
    main()
