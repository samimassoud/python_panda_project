import pandas as pd
 # Load the dataset
 file_path = 'chicago.csv'  # Make sure the dataset is in the same 
directory as this script
 df = pd.read_csv(file_path)
 # Basic Data Types
 # Integers and Floats
 total_trip_duration = 
average_trip_duration =
 # Strings
 first_start_station = 
# Booleans
 has_female_users =
 # Compound Data Types
 # Lists
 start_stations_list = 
# Tuples
 summary_stats = 
# Dictionaries
 user_type_counts = df['User Type'].value_counts().to_dict()
# Sets
 unique_stations = set(df['Start Station'])
 # Operators
 # Arithmetic Operators
 total_duration =  # Total trip duration
 average_duration =  # Average trip duration
 # Comparison Operators
 long_trips =  # Filtering trips longer than 1000 seconds
 # Logical Operators
 male_trips = # Trips by males born after 1990
 # Assignment Operators
 df['Adjusted Duration'] =  # Creating a new column
 df['Adjusted Duration'] = # Adding 60 seconds to each trip duration
 # Output results
 print("Total Trip Duration:", total_trip_duration)
 print("Average Trip Duration:", average_trip_duration)
 print("First Start Station:", first_start_station)
 print("Has Female Users:", has_female_users)
 print("Start Stations List:", start_stations_list[:5])  # Print first 5 to avoid clutter
 print("Summary Stats:", summary_stats)
 print("User Type Counts:", user_type_counts)
 print("Unique Start Stations:", list(unique_stations)[:5])  # Print first 5 to avoid clutter
 print("Total Duration:", total_duration)
 print("Average Duration:", average_duration)
 print("Number of Long Trips:", len(long_trips))
 print("Number of Male Trips by Users Born After 1990:", 
 len(male_trips))
 print("Sample Adjusted Durations:", df['Adjusted Duration'].head())
 # Save results to a new CSV file
 df.to_csv('chicago_analysis_results.csv', index=False)