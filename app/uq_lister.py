import os
import sys
import web_parser
import course_lister

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)


"""
Main function of the program.
"""
def main():
    ''''Run parsers and cleanup functions'
    struct = web_parser.obtain_page_details(
        web_parser.year_to_lookup())
    info = web_parser.cleanup_course_info(
        web_parser.get_raw_courses_info(struct))
    courses = web_parser.cleanup_course_list(
        web_parser.get_raw_course_code(struct))
    units = web_parser.cleanup_units_from_courses(
        web_parser.get_raw_courses_info(struct))

    prog_codes = web_parser.get_raw_program_code(
        web_parser.obtain_program_details_from_page())
    prog_names = web_parser.get_raw_program_name(
        web_parser.obtain_program_details_from_page())
    
    'Check for any errors while parsing data'
    web_parser.check_for_invalid_outliers(info, courses, units)

    'Prints available courses'
    course_lister.print_course_table(courses, units, info)

    'Prints available programs'
    course_lister.print_program_table(prog_codes, prog_names)'''
    web_parser.program_to_lookup()
    

if __name__ == "__main__":
    main()
