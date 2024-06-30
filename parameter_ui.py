#this is NOT my code.

# Import the libraries to connect to the database and present the information in tables
import sqlite3
from tabulate import tabulate

# This is the filename of the database to be used
DB_NAME = 'part_stats.db'
# This is the SQL to connect to all the tables in the database
TABLES = (" Part_Stats_Main "
           "LEFT JOIN Eats ON Part_Stats_Main.Eats_id = Eats.Eats_id "
           "LEFT JOIN Usable_By ON Part_Stats_Main.Usable_By_id = Usable_By.Usable_By_id ")

def print_parameter_query(fields:str, where:str, parameter):
    ''' Prints the results for a parameter query in tabular form. '''
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    sql = ("SELECT " + fields + " FROM " + TABLES + " WHERE " + where)
    cursor.execute(sql,(parameter,))
    results = cursor.fetchall()
    print(tabulate(results,fields.split(",")))
    db.close()

connections = input("How many connections do you want to search for (1-6): ")
print_parameter_query("*", "connections = ? ORDER BY Part_id DESC",connections)