# Every Single Street Guadalajara

## Overview
This repository documents the journey of running Every Single Street in Guadalajara, Jalisco, Mexico. The data for this project was sourced from running activities tracked and exported from Garmin devices.

## Project Structure

### 1. Data Extraction
- **Data Source**: Garmin Connect
- **File Formats**: TCX and GPX, which capture detailed information about each running activity.
  
### 2. Data Transformation
- A custom Python script was used to:
  - Convert TCX and GPX files into CSV format for ease of analysis.
  - Extract details such as time, latitude, longitude, altitude, distance, heart rate, speed, and cadence for each track point.
  - Process multiple TCX files to generate individual and combined CSVs.

### 3. Data Cleaning & Manipulation
- Used Google Sheets for preliminary data cleaning:
  - Deletion of empty rows.
  - Filtering activities with specific criteria.

### 4. Data Organization
- Developed scripts to:
  - Copy TCX files based on a given list of activity IDs to a designated folder.
  - Introduce an 'Activity ID' column in CSV files for easy reference and linking.

### 5. External Tools
- Utilized `garmin-connect-export` for bulk downloading of TCX files from Garmin Connect.

## Background & Context
This project was inspired by the challenge of running every single street in Guadalajara, Jalisco, Mexico. The data represents the culmination of numerous runs, capturing the essence of the city one street at a time.

## Future Directions
With a rich dataset in hand, potential next steps include in-depth data analysis, visualization, and creating a narrative around the running journey. This will provide insights into running patterns, performance metrics, and the overall experience of this unique challenge.
