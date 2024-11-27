import random
import pandas as pd
import os
import re

grades = ["AA", "AB", "BB", "BC", "CC", "CD", "DD", "FF"]

def generate_valid_grades():
    return "".join(random.choice(grades) for _ in range(20))

def generate_negative_csv_data(file_name, case_type, num_students=20):
    students_data = []
    
    for i in range(num_students):
        student_id = f"S{i+1}"
        if case_type == "invalid_grade_code":
            grades_data = generate_valid_grades()[:-2] + "ZZ"
        elif case_type == "empty":
            grades_data = ""
        elif case_type == "special_characters":
            grades_data = "AA" + "".join(random.choice(grades) for _ in range(18)) + "%"
        elif case_type == "numbers_present":
            grades_data = "AA" + "".join(random.choice(grades) for _ in range(18)) + "1"
        elif case_type == "same_grade":
            grades_data = "AA" * 20
        else:
            grades_data = generate_valid_grades()
        
        students_data.append({"Student ID": student_id, "Grades": grades_data})
    
    df = pd.DataFrame(students_data)
    
    directory = "/Users/mihirkatakdhond/Downloads/DAA LAB 6/LCS"
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    file_path = os.path.join(directory, file_name)
    df.to_csv(file_path, index=False)

negative_cases = ["invalid_grade_code", "empty", "special_characters", "numbers_present", "same_grade"]

for case_type in negative_cases:
    generate_negative_csv_data(f"negative_test_case_{case_type}.csv", case_type=case_type)

def lcs(str1, str2):
    dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]
    
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    lcs_sequence = []
    i, j = len(str1), len(str2)
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            lcs_sequence.append(str1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return ''.join(reversed(lcs_sequence))

def validate_grades(grades):
    if not isinstance(grades, str):
        raise ValueError(f"Invalid grade sequence: {grades}. Grade data should be a valid string.")
    
    if any(char.isdigit() for char in grades):
        raise ValueError(f"Invalid grade sequence: {grades}. Numbers found in the sequence.")
    
    if any(not char.isalpha() or char not in 'ABCDEF' for char in grades):
        raise ValueError(f"Invalid grade sequence: {grades}. Special characters or invalid characters found.")
    
    if len(grades) != 40:
        raise ValueError(f"Invalid grade sequence length: {grades}. The grade sequence must be exactly 40 characters.")
    
    if not all(re.match(r"[A-F]{2}", grades[i:i+2]) for i in range(0, len(grades), 2)):
        raise ValueError(f"Invalid grade sequence: {grades}. Invalid grade format detected.")

print("Negative Test Cases:")
directory = "/Users/mihirkatakdhond/Downloads/DAA LAB 6/LCS"
for case_number, case_type in enumerate(negative_cases, start=1):
    file_path = os.path.join(directory, f"negative_test_case_{case_type}.csv")
    try:
        df = pd.read_csv(file_path)

        grades_list = df["Grades"].tolist()

        grades_data = grades_list[0]
        
        if pd.isna(grades_data) or not isinstance(grades_data, str):
            print(f"Test Case {case_number}: Student {df.iloc[0]['Student ID']} - Missing or invalid grade data.")
        
        try:
            validate_grades(grades_data)
            print(f"Test Case {case_number}: Student {df.iloc[0]['Student ID']} - Grades are valid")
        except ValueError as e:
            print(f"Test Case {case_number}: Error for student {df.iloc[0]['Student ID']}: {e}")

    except FileNotFoundError:
        print(f"File {file_path} not found. Please check the file path.")

def handle_same_grade_case(test_case_number, df):
    grades_list = df["Grades"].tolist()
    if all(grade == grades_list[0] for grade in grades_list):
        print(f"Test Case {test_case_number}: All students have the same grade: {grades_list[0]}")
    else:
        print(f"Test Case {test_case_number}: Grades are not all the same.")

file_path = os.path.join(directory, f"negative_test_case_same_grade.csv")
try:
    df = pd.read_csv(file_path)
    handle_same_grade_case(5, df)
except FileNotFoundError:
    print(f"File {file_path} not found. Please check the file path.")
