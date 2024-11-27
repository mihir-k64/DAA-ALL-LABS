import random
import pandas as pd
import os

# List of valid grades (2 characters each)
grades = ["AA", "AB", "BB", "BC", "CC", "CD", "DD", "FF"]

# Function to generate valid grade sequences of 40 characters (20 subjects)
def generate_valid_grades():
    return "".join(random.choice(grades) for _ in range(20))  # 40 characters for 20 subjects

# Function to generate CSV data
def generate_csv_data(file_name, valid=True, num_students=20):
    students_data = []
    
    # Generate grade data for each student
    for i in range(num_students):
        student_id = f"S{i+1}"
        if valid:
            grades_data = generate_valid_grades()  # Valid grades
        else:
            grades_data = generate_valid_grades()  # Invalid data logic can be added later
        
        students_data.append({"Student ID": student_id, "Grades": grades_data})
    
    # Create a DataFrame
    df = pd.DataFrame(students_data)
    
    # Ensure directory exists
    directory = "/Users/mihirkatakdhond/Downloads/DAA LAB 6/LCS"  # Corrected directory path
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Created directory: {directory}")
    else:
        print(f"Directory already exists: {directory}")
    
    # Save DataFrame to CSV in the specified directory
    file_path = os.path.join(directory, file_name)
    df.to_csv(file_path, index=False)
    
    # Debug: Print confirmation message
    print(f"File saved at: {file_path}")  # Confirm file saving

# Generate 5 positive CSV files with valid grades (40 characters long)
for i in range(1, 6):
    generate_csv_data(f"positive_test_case_{i}.csv", valid=True)
