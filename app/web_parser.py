from lxml import html
import requests
import sys

print("""
==============================================================================
Program planner for UQ's Bachelor of Engineering / Software (H) Single Major
                                 >>SOFTWX2342<<
                                    
Created by Fouad Khalaf, 2018.

Important note: this program is not affiliated with UQ. Use at your own risk.
==============================================================================
""")



def program_to_lookup():
    program = input("""
What program / degree would you like to inquire about? Please enter it in the following format e.g. (SOFTWY2342).
For a list of program codes, type 'help'. 
""")
    if program == "help":
        print("Add course code list here...")
    else:
        print("zzzz")


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
            break


"""
Obtains all the data from the webpage.

Returns: data from the webpage in the form of a tree structure.
"""
def obtain_page_details(year):
    'Obtain page details'
    page = requests.get(
        'https://my.uq.edu.au/programs-courses/plan_display.html?acad_plan=SOFTWX2342&year='+str(year))
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
    'Run parsers and cleanup functions'
    struct = obtain_page_details(year_to_lookup())
    info = cleanup_course_info(get_raw_courses_info(struct))
    courses = cleanup_course_list(get_raw_course_code(struct))
    units = cleanup_units_from_courses(get_raw_courses_info(struct))
    
    'Check for any errors while parsing data'
    check_for_invalid_outliers(info, courses, units)

    'A list containing all available undergraduate programs (Program Codes)'
    available_undergrad_programs_codes = get_raw_program_code(obtain_program_details_from_page())

    'A list containing all available undergraduate programs (Program Names)'
    avaialble_undergrad_program_names = get_raw_program_name(obtain_program_details_from_page())
    

if __name__ == "__main__":
    main()
