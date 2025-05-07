#!/usr/bin/env python3
"""
Patient Data Cleaner

This script standardizes and filters patient records according to specific rules:

Data Cleaning Rules:
1. Names: Capitalize each word (e.g., "john smith" -> "John Smith")
2. Ages: Convert to integers, set invalid ages to 0
3. Filter: Remove patients under 18 years old
4. Remove any duplicate records

Input JSON format:
    [
        {
            "name": "john smith",
            "age": "32",
            "gender": "male",
            "diagnosis": "hypertension"
        },
        ...
    ]

Output:
- Cleaned list of patient dictionaries
- Each patient should have:
  * Properly capitalized name
  * Integer age (≥ 18)
  * Original gender and diagnosis preserved
- No duplicate records
- Prints cleaned records to console

Example:
    Input: {"name": "john smith", "age": "32", "gender": "male", "diagnosis": "flu"}
    Output: {"name": "John Smith", "age": 32, "gender": "male", "diagnosis": "flu"}

Usage:
    python patient_data_cleaner.py
"""

import json
import os

def load_patient_data(filepath):
    """
    Load patient data from a JSON file.
    
    Args:
        filepath (str): Path to the JSON file
        
    Returns:
        list: List of patient dictionaries
    """
    # BUG: No error handling for file not found
    # with open(filepath, 'r') as file:
        # return json.load(file)
    
    # FIX: Added try-except block to catch FileNotFoundError and return empty list
    try:
        with open(filepath, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return []

def clean_patient_data(patients):
    """
    Clean patient data by:
    - Capitalizing names
    - Converting ages to integers
    - Filtering out patients under 18
    - Removing duplicates
    
    Args:
        patients (list): List of patient dictionaries
        
    Returns:
        list: Cleaned list of patient dictionaries
    """
    cleaned_patients = []
    seen = set() # To track duplicates

    for patient in patients:
        try: 
            # BUG: Typo in key 'nage' instead of 'name'
            # FIX: Corrected key to 'name'
            patient['name'] = patient['name'].title()
            
            # BUG: Wrong method name (fill_na vs fillna)
            # FIX: No fillna needed
            patient['age'] = int(patient.get('age', 0))
            
            # BUG: Wrong method name (drop_duplcates vs drop_duplicates)
            # FIX: can't use drop_duplicates() since 'patient' is a dictionary; included set() of unique identifiers in the beginning of loop.
            # patient = patient.drop_duplcates()
            
            # BUG: Wrong comparison operator (= vs ==)
            # FIX: Changed '=' to '>=', and fixed logic to exclude patients under 18
            if patient['age'] >= 18:
                # BUG: Logic error - keeps patients under 18 instead of filtering them out
                # cleaned_patients.append(patient)
                identifier = (patient['name'], patient['age'], patient['diagnosis'])
                if identifier not in seen:
                        cleaned_patients.append(patient)
                        seen.add(identifier)
        except (KeyError, ValueError, TypeError):
            # Skip invalid patient entries
            continue
    
    # BUG: Missing return statement for empty list
    # FIX: return a list, even if it's empty
    return cleaned_patients
   
def main():
    """Main function to run the script."""
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Construct the path to the data file
    data_path = os.path.join(script_dir, 'data', 'raw', 'patients.json')
    
    # BUG: No error handling for load_patient_data failure
    # FIX: Handled inside load_patient_data using try-except
    patients = load_patient_data(data_path)
    
    # Clean the patient data
    cleaned_patients = clean_patient_data(patients)
    
    # BUG: No check if cleaned_patients is None
    # FIX: Now always returns a list, but we still check for emptiness
    if not cleaned_patients:
        print("No valid patient records found.")
        return []
    
    # Print the cleaned patient data
    print("Cleaned Patient Data:")
    for patient in cleaned_patients:
        # BUG: Using 'name' key but we changed it to 'nage'
        # FIX: We already changed it to 'name', so this works
        print(f"Name: {patient['name']}, Age: {patient['age']}, Diagnosis: {patient['diagnosis']}")
    
    # Return the cleaned data (useful for testing)
    return cleaned_patients

if __name__ == "__main__":
    main()
    