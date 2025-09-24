# Functions
def filter_by_date(submission_date, submissions_list):
    """
    Filters the submissions by specified date
    Parameters:
        submission_date (string) : date value in 'YYYY-MM-DD'
        submissions_list (A list of dictionary objects): A list of dictionary objects containing student data and assignments
    Returns:
        list: submission objects with a submissionDate equal to the date specified
    Raises:
        ValueError: (may delete if not used)
    """

    # THIS WORKS, TEST for PRINTING ALL TEST DATA
    # for person in submissions_list:
    #     # print(f"Date of Submission: {person["submissionDate"]}, ")
    #     print(person)

    # DOES NOT WORK
    # list_of_students_for_date_specified = []
    # for person in submissions_list:
    #     if submission_date == person["submissionDate"]:
    #         # print(person)
    #         list_of_students_for_date_specified.append(person)
    #         return list_of_students_for_date_specified

    list_of_students_for_date_specified = []
    for person in submissions_list:
        if submission_date == person["submissionDate"]:
            list_of_students_for_date_specified.append(person)
    return list_of_students_for_date_specified


def filter_by_student_id(student_id, submissions_list):
    """
    Filters the submissions by specified student ID
    Parameters:
            student_id (integer): student ID value
            submissions_list (A list of dictionary objects): A list of dictionary objects containing student data and assignments
    Returns:
            list: submission objects with a submissionId equal to the studentId specified
    Raises:
            ValueError: (may delete if not used)
    """
    list_of_students_for__studentId_specified = []
    for person in submissions_list:
        if student_id == person["studentId"]:
            # print(person)
            list_of_students_for__studentId_specified.append(person)
    return list_of_students_for__studentId_specified


# NOT WORKING
def find_unsubmitted(submission_date, student_names_list, submissions_list):
    """
    Filters submissions to find missing entries
    Parameters:
        submission_date (string) : date value in 'MM/DD/YYYY'
        student_names (list): Names of the students
        submissions_list (A list of dictionary objects): A list of dictionary objects containing student data and assignments
    Returns:
        float: average of all the quiz scores
    Raises:
        ValueError: (may delete if not used)
    """
    list_of_students_missing_assignments = []
    for person in submissions_list:
        if (person not in student_names_list) and (
            submission_date == person["submissionDate"]
        ):
            # print(person)
            list_of_students_missing_assignments.append(person["studentName"])
    return list_of_students_missing_assignments


def get_average_score(submission_list):
    """
    Calculates the average score from submissions
    Parameters:
        submissions_list (A list of dictionary objects): A list of dictionary objects containing student data and assignments
    Returns:
        float: average of the quiz scores
    Raises:
        ValueError: (may delete if not used)
    """
    return


def get_average_score_by_module(submission_list):
    """

    Parameters:
        submissions_list (A list of dictionary objects): A list of dictionary objects containing student data and assignments
    Returns:
        object: module key and average
    Raises:
        ValueError: (may delete if not used)
    """
    return


# # Data Model for a Submission:
# {
# "quizName": "string",
# "quizModule": "string",
# "quizScore": number,
# "studentId": number,
# "studentName": "string",
# "submissionDate": "string"
# }

# Sample Data

submission_1 = {
    "quizName": "Quiz 1: Order of Operations",
    "quizModule": "Math",
    "quizScore": 88.7,
    "studentId": 589102,
    "studentName": "Jimmy Johns",
    "submissionDate": "9/19/2025",
}

submission_2 = {
    "quizName": "Quiz 1: Order of Operations",
    "quizModule": "Math",
    "quizScore": 93.6,
    "studentId": 589702,
    "studentName": "Little BoPeep",
    "submissionDate": "9/19/2025",
}

submission_3 = {
    "quizName": "Quiz 1: Order of Operations",
    "quizModule": "Math",
    "quizScore": 90.5,
    "studentId": 584752,
    "studentName": "Winter Woods",
    "submissionDate": "9/19/2025",
}

submission_4 = {
    "quizName": "Quiz 1: Order of Operations",
    "quizModule": "Math",
    "quizScore": 72.3,
    "studentId": 582702,
    "studentName": "Molly Moffat",
    "submissionDate": "9/19/2025",
}

submission_5 = {
    "quizName": "Basketball: Rules of the Game",
    "quizModule": "Gym",
    "quizScore": 99.0,
    "studentId": 589102,
    "studentName": "Jimmy Johns",
    "submissionDate": "9/21/2025",
}

submission_6 = {
    "quizName": "Basketball: Rules of the Game",
    "quizModule": "Gym",
    "quizScore": 92.4,
    "studentId": 589702,
    "studentName": "Little BoPeep",
    "submissionDate": "9/21/2025",
}

submission_7 = {
    "quizName": "Basketball: Rules of the Game",
    "quizModule": "Gym",
    "quizScore": 90.5,
    "studentId": 584752,
    "studentName": "Winter Woods",
    "submissionDate": "9/21/2025",
}

submission_8 = {
    "quizName": "The Life of William Shakespeare",
    "quizModule": "English",
    "quizScore": 68.1,
    "studentId": 589102,
    "studentName": "Jimmy Johns",
    "submissionDate": "9/19/2025",
}

submission_9 = {
    "quizName": "The Life of William Shakespeare",
    "quizModule": "English",
    "quizScore": 76.8,
    "studentId": 589702,
    "studentName": "Little BoPeep",
    "submissionDate": "9/19/2025",
}

submission_10 = {
    "quizName": "The Life of William Shakespeare",
    "quizModule": "English",
    "quizScore": 85.4,
    "studentId": 584752,
    "studentName": "Winter Woods",
    "submissionDate": "9/19/2025",
}

submission_11 = {
    "quizName": "The Life of William Shakespeare",
    "quizModule": "English",
    "quizScore": 95.7,
    "studentId": 582702,
    "studentName": "Molly Moffat",
    "submissionDate": "9/19/2025",
}

submission_12 = {
    "quizName": "The Life of William Shakespeare",
    "quizModule": "English",
    "quizScore": 78.5,
    "studentId": 585702,
    "studentName": "Jenny Johnson",
    "submissionDate": "9/19/2025",
}

submission_13 = {
    "quizName": "Quiz 2: Math Vocabulary",
    "quizModule": "Math",
    "quizScore": 88.7,
    "studentId": 589102,
    "studentName": "Jimmy Johns",
    "submissionDate": "9/23/2025",
}

submission_14 = {
    "quizName": "Quiz 2: Math Vocabulary",
    "quizModule": "Math",
    "quizScore": 93.6,
    "studentId": 589702,
    "studentName": "Little BoPeep",
    "submissionDate": "9/23/2025",
}

submission_15 = {
    "quizName": "Quiz 2: Math Vocabulary",
    "quizModule": "Math",
    "quizScore": 90.5,
    "studentId": 584752,
    "studentName": "Winter Woods",
    "submissionDate": "9/23/2025",
}

submission_16 = {
    "quizName": "Quiz 2: Math Vocabulary",
    "quizModule": "Math",
    "quizScore": 72.3,
    "studentId": 582702,
    "studentName": "Molly Moffat",
    "submissionDate": "9/23/2025",
}

collection_of_submissions = [
    submission_1,
    submission_2,
    submission_3,
    submission_4,
    submission_5,
    submission_6,
    submission_7,
    submission_8,
    submission_9,
    submission_10,
    submission_11,
    submission_12,
    submission_13,
    submission_14,
    submission_15,
    submission_16,
]


# Student Roster
student_roster = [
    "Jimmy Johns",
    "Little BoPeep",
    "Winter Woods",
    "Molly Moffat",
    "Jenny Johnson",
]
# filter_by_date("9/19/2025", collection_of_submissions)
# Use the one below
# list_of_students_by_date = filter_by_date("9/30/2025", collection_of_submissions)
# print(list_of_students_by_date)

# list_of_students_by_studentID = filter_by_student_id(582702, collection_of_submissions)
# print(list_of_students_by_studentID)

list_of_students_missing_all_assignments = find_unsubmitted(
    "9/23/2025", student_roster, collection_of_submissions
)
print(list_of_students_missing_all_assignments)
