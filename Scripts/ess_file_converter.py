import os
import xml.etree.ElementTree as ET
import csv

def process_tcx_file(file_path, activity_id):
    tree = ET.parse(file_path)
    root = tree.getroot()
    ns = {'default': 'http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2',
          'ns3': 'http://www.garmin.com/xmlschemas/ActivityExtension/v2'}
    
    data = []
    for trackpoint in root.findall(".//default:Trackpoint", ns):
        row = {}
        row['Activity ID'] = activity_id    # Add the activity ID to the row

        time = trackpoint.find('default:Time', ns)
        position = trackpoint.find('default:Position', ns)
        altitude = trackpoint.find('default:AltitudeMeters', ns)
        distance = trackpoint.find('default:DistanceMeters', ns)
        heartrate = trackpoint.find('default:HeartRateBpm/default:Value', ns)
        speed = trackpoint.find('.//ns3:Speed', ns)
        cadence = trackpoint.find('.//ns3:RunCadence', ns)

        row['Time'] = time.text if time is not None else ''
        row['LatitudeDegrees'] = position.find('default:LatitudeDegrees', ns).text if position is not None else ''
        row['LongitudeDegrees'] = position.find('default:LongitudeDegrees', ns).text if position is not None else ''
        row['AltitudeMeters'] = altitude.text if altitude is not None else ''
        row['DistanceMeters'] = distance.text if distance is not None else ''
        row['HeartRateBpm'] = heartrate.text if heartrate is not None else ''
        row['Speed'] = speed.text if speed is not None else ''
        row['RunCadence'] = cadence.text if cadence is not None else ''

        data.append(row)
    
    return data


folder_path = r'C:\Users\Hector G. Guerrero\Documents\Portfolio\EverySingleStreetGDL\Data\tcxs_ESS'
output_folder = r'C:\Users\Hector G. Guerrero\Documents\Portfolio\EverySingleStreetGDL\Data\csvs'
global_folder = r'C:\Users\Hector G. Guerrero\Documents\Portfolio\EverySingleStreetGDL\Data'

# Check if the output folder exists, create it if not
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

all_data = []

for file_name in os.listdir(folder_path):
    if file_name.endswith('.tcx'):
        activity_id = file_name.split('_')[1].split('.')[0]  # Extract Activity ID from the file name
        file_path = os.path.join(folder_path, file_name)
        data = process_tcx_file(file_path, activity_id)
        all_data.extend(data)

        # Write individual CSV file
        csv_file_path = os.path.join(output_folder, file_name + '.csv')
        with open(csv_file_path, 'w', newline='') as csvfile:
            fieldnames = ['Activity ID', 'Time', 'LatitudeDegrees', 'LongitudeDegrees', 'AltitudeMeters', 'DistanceMeters', 'HeartRateBpm', 'Speed', 'RunCadence']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        print('Wrote', csv_file_path)
                    
# Write combined CSV file
csv_file_path = os.path.join(global_folder, 'all_data.csv')
with open(csv_file_path, 'w', newline='') as csvfile:
    fieldnames = ['Activity ID', 'Time', 'LatitudeDegrees', 'LongitudeDegrees', 'AltitudeMeters', 'DistanceMeters', 'HeartRateBpm', 'Speed', 'RunCadence']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(all_data)
    
print('Done')