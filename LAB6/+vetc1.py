# Function to calculate the Longest Common Subsequence (LCS) with memoization
def lcs(s1, s2, m, n, memo):
    # Base condition: If either string is empty, LCS length is 0
    if m == 0 or n == 0:
        return 0

    # Check if the result is already in the memoization table
    if memo[m][n] != -1:
        return memo[m][n]

    # If characters match, add 1 to the result and move diagonally in the matrix
    if s1[m - 1] == s2[n - 1]:
        memo[m][n] = 1 + lcs(s1, s2, m - 1, n - 1, memo)
    else:
        # If characters do not match, take the maximum result from two possible moves
        memo[m][n] = max(lcs(s1, s2, m, n - 1, memo), lcs(s1, s2, m - 1, n, memo))
    
    return memo[m][n]

# Function to reconstruct the LCS sequence from the memoization table
def get_lcs_sequence(s1, s2, m, n, memo):
    sequence = []
    while m > 0 and n > 0:
        # If characters match, add to the sequence and move diagonally up-left
        if s1[m - 1] == s2[n - 1]:
            sequence.append(s1[m - 1])
            m -= 1
            n -= 1
        # Move in the direction of the larger value in the memo table
        elif memo[m - 1][n] >= memo[m][n - 1]:
            m -= 1
        else:
            n -= 1
    
    # Since we built the sequence backwards, reverse it before returning
    return ''.join(reversed(sequence))

# Function to find LCS of grades
def find_lcs_of_grades(student_grades):
    lcs_length = 0
    longest_sequence = ""
    student_pair = ()

    # Compare each student's grades list with every other student
    for i in range(len(student_grades)):
        for j in range(i + 1, len(student_grades)):
            # Get two grade lists to compare
            s1 = student_grades[i]
            s2 = student_grades[j]
            m = len(s1)
            n = len(s2)
            
            # Initialize memoization table with -1
            memo = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]
            
            # Calculate LCS length for these two students
            current_lcs_length = lcs(s1, s2, m, n, memo)
            
            # Update longest LCS sequence if a longer one is found
            if current_lcs_length > lcs_length:
                lcs_length = current_lcs_length
                longest_sequence = get_lcs_sequence(s1, s2, m, n, memo)
                student_pair = (i + 1, j + 1)

    return lcs_length, longest_sequence, student_pair

# Example student grades data (20 students with grades like 'AA', 'AB', 'BB', ...)
student_grades = [
    "AABBBBCBCCBBCCFFACDCDAC", "BBCCABABAFBBAAACCFFBBCCD", "CCABACDDBFBBABCBFFBCBBC", 
    "BBCCFFABBCABABCCACDBBBA", "BACCABBCDCABFFABABACBCA", "FFBCABBCDAAFCCDDCBABABF", 
    "AABBBCCACBBCCFFBDDAACAB", "CCFAABCCCDABBCBBFAFFABF", "DDCCABFBBABBCACAAFFBBAC", 
    "BBCCDDABABACBBAABFFCCAC", "ACBBCAFFDDCCBBAABABBCAC", "ABABABCCFDCABBBBCFDDCBA", 
    "BBACCCFADFBBABCCDDCAACC", "CCCDABABFBFFCAABAAACBBF", "ABBCDAFFACCBBACBFFABCCA", 
    "FBACABBBCCBBFFCAACBBDDA", "CCABBCFAAACDDBBAABABCCB", "FBBCCDAACCDACBBFBABAFCA", 
    "AAABBBCCDBFBBACACCCFFAC", "BCAAFFBCCABACCDDDABACCB"
]


# Find LCS among grades of students
lcs_length, longest_sequence, student_pair = find_lcs_of_grades(student_grades)

# Output the results
print(f"Longest Common Sequence Length: {lcs_length}")
print(f"Longest Common Sequence: {longest_sequence}")
print(f"Found between Student {student_pair[0]} and Student {student_pair[1]}")
