'''use parameter_ui to make your own query!'''
#this is NOT my code.

# Import the libraries to connect to the database and present the information in tables
import sqlite3
from tabulate import tabulate

# This is the filename of the database to be used
DB_NAME = 'part_stats.db'

def print_query(view_name:str):
    ''' Prints the specified view from the database in a table '''
    # Set up the connection to the database
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    # Get the results from the view
    sql = "SELECT * FROM '" + view_name + "'"
    cursor.execute(sql)
    results = cursor.fetchall()
    # Get the field names to use as headings
    field_names = "SELECT name from pragma_table_info('" + view_name + "') AS tblInfo"
    cursor.execute(field_names)
    headings = list(sum(cursor.fetchall(),()))
    # Print the results in a table with the headings
    print(tabulate(results,headings))
    db.close()

#you may want to zoom out using ctrl +/- to see the full database.
menu_choice = ''
while menu_choice != 'Z':
    menu_choice = input('This is a database of parts\n\n'
                        'Type the letter for the information you want:\n'
                        'A: all data\n'
                        'B: parts usable by creatures\n'
                        'C: parts usable by plants\n'
                        'D: block parts (6 connections)\n'
                        'E: non-block parts (< 6 connections)\n'
                        'F: parts with high part defense\n'
                        'G: parts that dont cost DNA to place\n'
                        'H: parts that can be eaten by herbivores\n'
                        'I: parts that produce energy passivley under certain conditions\n'
                        'J: parts that let more than no light through them\n'
                        'K: parts that can deal damage to organisms\n'
                        'L: parts that have a higher buoyancy than weight, and therefore float on water\n'
                        'M: parts with damage type inflictions and/or resistances\n'
                        'Z: Exit\n\nType option here: ')
    menu_choice = menu_choice.upper()
    if menu_choice == 'A':
        print_query('all_data')
    elif menu_choice == 'B':
        print_query('creature_parts')
    elif menu_choice == 'C':
        print_query('plant_parts')
    elif menu_choice == 'D':
        print_query('block_parts')
    elif menu_choice == 'E':
        print_query('non-block_parts')
    elif menu_choice == 'F':
        print_query('defensive_parts')
    elif menu_choice == 'G':
        print_query('free_parts')
    elif menu_choice == 'H':
        print_query('edible_parts')
    elif menu_choice == 'I':
        print_query('producer_parts')
    elif menu_choice == 'J':
        print_query('transparent_parts')
    elif menu_choice == 'K':
        print_query('damaging_parts')
    elif menu_choice == 'L':
        print_query('buoyant_parts')
    elif menu_choice == 'M':
        print_query('type_parts')