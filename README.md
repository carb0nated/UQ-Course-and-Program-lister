# UQ-Course-and-Program-lister
***NOTE: THIS PROGRAM IS NOT AFFILIATED WITH UQ IN ANY WAY. USE AT YOUR OWN RISK.***
A simple program which lists all the undergraduate programs (degrees) provided by The University of Queensland, and all of the courses possible for a program.

## Purpose


## How to use:
### Installation
#### Install libraries
This progam uses the `lxml` and `requests` libraries which do not come pre-installed on some devices.

* To install `lxml`, please follow the steps listed [here](https://lxml.de/installation.html)

* To install `requests`, please follow the steps listed [here](https://stackoverflow.com/a/30362669)

#### Option 1: Add it to your program
You may add this program to yours by importing it. To do that:
1. Place `UQ-Course-and-Program-lister`'s source files in your program's main directory.
2. Add `import uq_course_program_lister` to your program.
3. Use any of the four functions listed below:

| Function | Parameters | Returns |
|:--------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------:|
| uq_lister.available_courses(program, choice) | program: 10-character program code (in caps)  choice: `code` to return course codes, `name` to return course names | Returns a list of all the available courses for a specific program. |
| uq_lister.available_programs(choice) | choice: `code` for 10-character program codes, `name` for program names | Returns a list containing either 10-character program codes or program names. |
| uq_lister.available_courses_table(program, choice) | program: 10-character program code (in caps)   choice: `code` to return course codes, `name` to return course names | Prints a user-friendly table containing all the available courses for that program. |
| uq_lister.available_programs_table(choice) | choice: `code` for 10-character program codes, `name` for program names | Prints a user-friendly table containing all the available programs currently being provided by UQ. |


#### Option 2: Use it by itself
1. `cd` to the directory containing this program using Terminal or CMD
2. Type `python uq_lister.py`
3. Follow the user prompts.

**OR**

1. Right click on `uq_lister.py` and select *Edit WITH IDLE*
2. Run the program and follow the user prompts.

## Usage
You are allowed to use this program for free, and even integrate it with your open source projects as long as it's purely used for non-commercial purposes. Contributions and improvements are welcome and highly appreciated!
