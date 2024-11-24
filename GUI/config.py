# config.py

import os



def get_database_path():

    GUI_path = os.path.dirname(os.path.abspath(__file__))
    main_dir = os.path.dirname(GUI_path)
    database_path = os.path.join(main_dir, 'Database')

    database_file = os.path.join(database_path, 'SUHRSystem(1).db')

    return database_file

def get_pdf_path():
    GUI_path = os.path.dirname(os.path.abspath(__file__))
    main_dir = os.path.dirname(GUI_path)
    pdf_path = os.path.join(main_dir, 'pdf')
    return pdf_path


def get_profile_path():
    GUI_path = os.path.dirname(os.path.abspath(__file__))
    profile_path = os.path.join(GUI_path,'employee_pictures')
    
    return profile_path

