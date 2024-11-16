
#playing around with file directories, so we wont have to always specify and change filepaths
#this a tutorial code section and therefore should not have any impact on the rest of the modules
import os


# Get the directory of the current file, which is in GUI
current_file_dir = os.path.dirname(os.path.abspath(__file__))
print(current_file_dir)

# Navigate back to the 'main' folder, for us to see the database, GUI, logs,pdf and etc... folders
main_dir = os.path.dirname(current_file_dir)
print(main_dir)

# Access the 'main/database' folder
database_dir = os.path.join(main_dir, 'Database')

# Change the working directory to 'images'
os.chdir(database_dir)
# Print the current working directory to verify
print("Current directory:", os.getcwd())

os.chdir(current_file_dir)
print("Going Back to Filepath:",os.getcwd())