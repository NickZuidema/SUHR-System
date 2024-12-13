
#playing around with file directories, so we wont have to always specify and change filepaths
import os


# Get the directory of the current file, which is in GUI
current_file_dir = os.path.dirname(os.path.abspath(__file__))
print(current_file_dir)

# Navigate back to the 'main' folder, for us to see the database, GUI, logs,pdf and etc... folders
#main_dir = os.path.dirname(current_file_dir)
#print(main_dir)

# Access the 'main/database' folder
#database_dir = os.path.join(main_dir, 'Database')

# Change the working directory to 'images'
#os.chdir(database_dir)
# Print the current working directory to verify
#print("Current directory:", os.getcwd())

#os.chdir(current_file_dir)
#print("Going Back to Filepath:",os.getcwd())

GUI_path = os.path.dirname(os.path.abspath(__file__))
#main_dir = os.path.dirname(GUI_path)
database_path = os.path.join(GUI_path, 'Database')

database_file = os.path.join(database_path, 'SUHRSystem(1).db')

print(database_file)

GUI_path = os.path.dirname(os.path.abspath(__file__))
#main_dir = os.path.dirname(GUI_path)
pdf_path = os.path.join(GUI_path, 'pdf')

print(pdf_path)


GUI_path = os.path.dirname(os.path.abspath(__file__))
profile_path = os.path.join(GUI_path,'employee_pictures')

print(profile_path)