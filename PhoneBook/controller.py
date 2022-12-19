import modul
import txt
import csv
import view

def choice_action (value):
    if   value == 1:
        modul.great_contact()
        view.head()
        choice_action(view.get_value())
    elif value == 2:
        modul.search()
        view.head()
        choice_action(view.get_value())
    elif value == 3:
        modul.change_data()
        view.head()
        choice_action(view.get_value())
    elif value == 4:
        modul.delet()
        view.head()
        choice_action(view.get_value())
    elif value == 5:
        txt.export()
        view.head()
        choice_action(view.get_value())
    elif value == 6:
        csv.export()
        view.head()
        choice_action(view.get_value())
    elif value == 7:
        txt.import_txt()
        view.head()
        choice_action(view.get_value())
    elif value == 8:
        csv.import_csv()
        view.head()
        choice_action(view.get_value())
    elif value == 0:
        exit()



