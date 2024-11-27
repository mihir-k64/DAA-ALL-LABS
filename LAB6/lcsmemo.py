import random
import pandas as pd
import os
import re

grades = ["AA", "AB", "BB", "BC", "CC", "CD", "DD", "FF"]

def generate_valid_grades():
    return "".join(random.choice(grades) for _ in range(20))

def generate_csv_data(file_name, valid=True, num_students=20):
    students_data = []
    
    for i in range(num_students):
        student_id = f"S{i+1}"
        if valid:
            grades_data = generate_valid_grades()
        else:
            grades_data = generate_valid_grades()
        
        students_data.append({"Student ID": student_id, "Grades": grades_data})
    
    df = pd.DataFrame(students_data)
    
    directory = "/Users/mihirkatakdhond/Downloads/DAA LAB 6/LCS"
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    file_path = os.path.join(directory, file_name)
    df.to_csv(file_path, index=False)

# Generate positive test cases
for i in range(1, 6):
    generate_csv_data(f"positive_test_case_{i}.csv", valid=True)

# Memoization-based LCS implementation
def lcs_memo(str1, str2):
    memo = {}

    def helper(i, j):
        # Base case: if either string is empty
        if i == 0 or j == 0:
            return ""
        
        # Check if result is already computed
        if (i, j) in memo:
            return memo[(i, j)]
        
        # Characters match
        if str1[i - 1] == str2[j - 1]:
            memo[(i, j)] = helper(i - 1, j - 1) + str1[i - 1]
        else:
            # Take the longer of excluding one character from either string
            lcs1 = helper(i - 1, j)
            lcs2 = helper(i, j - 1)
            memo[(i, j)] = lcs1 if len(lcs1) > len(lcs2) else lcs2
        
        return memo[(i, j)]

    return helper(len(str1), len(str2))

# Validation function
def validate_grades(grades):
    if len(grades) != 40:
        raise ValueError(f"Invalid grade sequence length: {grades}. Expected length is 40 characters.")
    
    if any(char.isdigit() for char in grades):
        raise ValueError(f"Invalid grade sequence: {grades}. Numbers found in the sequence.")
    
    if not all(re.match(r"[A-F]{2}", grades[i:i+2]) for i in range(0, len(grades), 2)):
        raise ValueError(f"Invalid grade sequence: {grades}. Special characters or invalid grade format detected.")

# Processing the positive test cases
print("Positive Test Cases:")
directory = "/Users/mihirkatakdhond/Downloads/DAA LAB 6/LCS"

for test_case_num in range(1, 6):
    file_path = os.path.join(directory, f"positive_test_case_{test_case_num}.csv")
    try:
        df = pd.read_csv(file_path)

        grades_list = df["Grades"].tolist()

        overall_lcs = grades_list[0]
        for student_index in range(1, len(grades_list)):
            try:
                validate_grades(grades_list[student_index])
                overall_lcs = lcs_memo(overall_lcs, grades_list[student_index])
            except ValueError as e:
                print(f"Error for student {df.iloc[student_index]['Student ID']}: {e}")

        print(f"Longest Common Subsequence of Grades for All Students in Test Case {test_case_num}:", overall_lcs)
    except FileNotFoundError:
        print(f"File {file_path} not found. Please check the file path.")
