import csv
import os
import shutil
        
id_list = []

with open(r"C:\Users\Hector G. Guerrero\Documents\Portfolio\EverySingleStreetGDL\Data\Activities.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        id_list.append(row['Activity ID'])

# Path to TCX files
source_folder = r'C:\Users\Hector G. Guerrero\Documents\Portfolio\EverySingleStreetGDL\Data\tcxs'

# Folder to copy TCX files to
destination_folder = r'C:\Users\Hector G. Guerrero\Documents\Portfolio\EverySingleStreetGDL\Data\tcxs_ESS'

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)
    
for file_name in os.listdir(source_folder):
    if file_name.startswith('activity_') and file_name.endswith('.tcx'):
        # Extract the activity ID from the file name
        activity_id = file_name.split('_')[1].split('.')[0]
        
        # Check if the activity ID is in the list
        if activity_id in id_list:
            source_path = os.path.join(source_folder, file_name)
            dest_path = os.path.join(destination_folder, file_name)
            
            # Copy the file
            shutil.copyfile(source_path, dest_path)
            print('Copied', file_name)

print('Done')