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

def print_parameter_query(fields:str, where:str):
    ''' Prints the results for a parameter query in tabular form. '''
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    sql = ("SELECT " + fields + " FROM " + TABLES + " WHERE " + where)
    print(sql)
    cursor.execute(sql)
    results = cursor.fetchall()
    print(tabulate(results,fields.split(",")))
    db.close()

print("")
print("list of columns: [Part_id, Usable_by_id, Eats_id, Name, Connections, Energy, Appetite, Health, Health_Regeneration, Defense, Part_Defense, Damage_Taken_Modifiers, Speed, Weight, Buoyancy, Light_Transparency, Power, Damage, Damage_Cooldown, Can_Damage, Inflicted_Damage_Types, Passive_Energy, Cost]")
print("")
print("only write what is in brackets -> (). notes are written in -> [].")
print("")
chosen_columns = input("which columns would you like? [* for all columns] [remember to put a , and a space inbetween them - also use capitals as shown in the list above!] [recommended to put Name or Part_id in at some point]: ")
while not chosen_columns:
    print("")
    chosen_columns = input("which columns would you like? [* for all columns] [remember to put a , and a space inbetween them - also use capitals as shown in the list above!] [recommended to put Name or Part_id in at some point]: ")
print("")
chosen_where = input("only show parts where (column (= [or] > [or] <) number) [leave blank for no restrictions]: ")
print("")
chosen_order = input("order by (column (ASC [or] DESC)) [leave blank for Part_id ASC order [ASC is ascending] [DESC is descending]]: ")
print("")

if chosen_where:
    if chosen_order:
        print_parameter_query(chosen_columns, chosen_where + " ORDER BY " + chosen_order)
    else:
        print_parameter_query(chosen_columns, chosen_where)
elif chosen_order:
    print_parameter_query(chosen_columns, "Part_id < 99999999 ORDER BY " + chosen_order)
else:
    print_parameter_query(chosen_columns, "Part_id < 99999999")