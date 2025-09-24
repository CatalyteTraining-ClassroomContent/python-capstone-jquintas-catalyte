# Functions
def filter_by_date(submission_date, submissions_list):
    """
    Filters the submissions by specified date
    Parameters:
        submission_date (string) : date value in 'YYYY-MM-DD'
        submissions_list (A list of dictionary objects): A list of dictionary objects containing student data and assignments
    Returns:
        list: submission objects with a submission_date equal to the date specified
    Raises:
        ValueError: (may delete if not used)
    """

    # THIS WORKS, TEST for PRINTING ALL TEST DATA
    # for person in submissions_list:
    #     # print(f"Date of Submission: {person["submission_date"]}, ")
    #     print(person)

    # DOES NOT WORK
    # list_of_students_for_date_specified = []
    # for person in submissions_list:
    #     if submission_date == person["submission_date"]:
    #         # print(person)
    #         list_of_students_for_date_specified.append(person)
    #         return list_of_students_for_date_specified

    list_of_students_for_date_specified = []
    for person in submissions_list:
        if submission_date == person["submission_date"]:
            list_of_students_for_date_specified.append(person)
    return list_of_students_for_date_specified


def filter_by_student_id(student_id, submissions_list):
    """
    Filters the submissions by specified student ID
    Parameters:
            student_id (integer): student ID value
            submissions_list (A list of dictionary objects): A list of dictionary objects containing student data and assignments
    Returns:
            list: submission objects with a submissionId equal to the student_id specified
    Raises:
            ValueError: (may delete if not used)
    """
    list_of_students_for__student_id_specified = []
    for person in submissions_list:
        if student_id == person["student_id"]:
            # print(person)
            list_of_students_for__student_id_specified.append(person)
    return list_of_students_for__student_id_specified


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

    # list_of_students_missing_all_assignments = []
    # for person in submissions_list:
    #     if (person["student_name"] not in student_names_list) and (
    #         submission_date == person["submission_date"]
    #     ):
    #         # print(person)
    #         list_of_students_missing_all_assignments.append(person["student_name"])
    # return list_of_students_missing_all_assignments

    # This does not work because my set up is a list of dictionaries?
    # list_of_students_missing_all_assignments = []
    # submissions_values = submissions_list.values()
    # for student in student_names_list:
    #     if student not in submissions_values():
    #         # ["student_name"]:
    #         # if student not in submissions_list:
    #         # and (submission_date == submissions_list["submission_date"]):
    #         # print(person)
    #         list_of_students_missing_all_assignments.append(student)
    # return list_of_students_missing_all_assignments

    list_of_students_with_at_least_one_submission = []
    list_of_students_missing_all_assignments = []
    for person in submissions_list:
        if (person["student_name"] in student_names_list) and (
            submission_date == person["submission_date"]
        ):
            # print(person)
            list_of_students_with_at_least_one_submission.append(person["student_name"])

    set_of_students_missing_all_assignments = set(student_names_list) - set(
        list_of_students_with_at_least_one_submission
    )
    list_of_students_missing_all_assignments = list(
        set_of_students_missing_all_assignments
    )
    return list_of_students_missing_all_assignments


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
# "quiz_name": "string",
# "quiz_module": "string",
# "quiz_score": number,
# "student_id": number,
# "student_name": "string",
# "submission_date": "string"
# }

# Sample Data

submission_1 = {
    "quiz_name": "Quiz 1: Order of Operations",
    "quiz_module": "Math",
    "quiz_score": 88.7,
    "student_id": 589102,
    "student_name": "Jimmy Johns",
    "submission_date": "9/19/2025",
}

submission_2 = {
    "quiz_name": "Quiz 1: Order of Operations",
    "quiz_module": "Math",
    "quiz_score": 93.6,
    "student_id": 589702,
    "student_name": "Little BoPeep",
    "submission_date": "9/19/2025",
}

submission_3 = {
    "quiz_name": "Quiz 1: Order of Operations",
    "quiz_module": "Math",
    "quiz_score": 90.5,
    "student_id": 584752,
    "student_name": "Winter Woods",
    "submission_date": "9/19/2025",
}

submission_4 = {
    "quiz_name": "Quiz 1: Order of Operations",
    "quiz_module": "Math",
    "quiz_score": 72.3,
    "student_id": 582702,
    "student_name": "Molly Moffat",
    "submission_date": "9/19/2025",
}

submission_5 = {
    "quiz_name": "Basketball: Rules of the Game",
    "quiz_module": "Gym",
    "quiz_score": 99.0,
    "student_id": 589102,
    "student_name": "Jimmy Johns",
    "submission_date": "9/21/2025",
}

submission_6 = {
    "quiz_name": "Basketball: Rules of the Game",
    "quiz_module": "Gym",
    "quiz_score": 92.4,
    "student_id": 589702,
    "student_name": "Little BoPeep",
    "submission_date": "9/21/2025",
}

submission_7 = {
    "quiz_name": "Basketball: Rules of the Game",
    "quiz_module": "Gym",
    "quiz_score": 90.5,
    "student_id": 584752,
    "student_name": "Winter Woods",
    "submission_date": "9/21/2025",
}

submission_8 = {
    "quiz_name": "The Life of William Shakespeare",
    "quiz_module": "English",
    "quiz_score": 68.1,
    "student_id": 589102,
    "student_name": "Jimmy Johns",
    "submission_date": "9/19/2025",
}

submission_9 = {
    "quiz_name": "The Life of William Shakespeare",
    "quiz_module": "English",
    "quiz_score": 76.8,
    "student_id": 589702,
    "student_name": "Little BoPeep",
    "submission_date": "9/19/2025",
}

submission_10 = {
    "quiz_name": "The Life of William Shakespeare",
    "quiz_module": "English",
    "quiz_score": 85.4,
    "student_id": 584752,
    "student_name": "Winter Woods",
    "submission_date": "9/19/2025",
}

submission_11 = {
    "quiz_name": "The Life of William Shakespeare",
    "quiz_module": "English",
    "quiz_score": 95.7,
    "student_id": 582702,
    "student_name": "Molly Moffat",
    "submission_date": "9/19/2025",
}

submission_12 = {
    "quiz_name": "The Life of William Shakespeare",
    "quiz_module": "English",
    "quiz_score": 78.5,
    "student_id": 585702,
    "student_name": "Jenny Williams",
    "submission_date": "9/19/2025",
}

submission_13 = {
    "quiz_name": "Quiz 2: Math Vocabulary",
    "quiz_module": "Math",
    "quiz_score": 88.7,
    "student_id": 589102,
    "student_name": "Jimmy Johns",
    "submission_date": "9/23/2025",
}

submission_14 = {
    "quiz_name": "Quiz 2: Math Vocabulary",
    "quiz_module": "Math",
    "quiz_score": 93.6,
    "student_id": 589702,
    "student_name": "Little BoPeep",
    "submission_date": "9/23/2025",
}

submission_15 = {
    "quiz_name": "Quiz 2: Math Vocabulary",
    "quiz_module": "Math",
    "quiz_score": 90.5,
    "student_id": 584752,
    "student_name": "Winter Woods",
    "submission_date": "9/23/2025",
}

submission_16 = {
    "quiz_name": "Quiz 2: Math Vocabulary",
    "quiz_module": "Math",
    "quiz_score": 72.3,
    "student_id": 582702,
    "student_name": "Molly Moffat",
    "submission_date": "9/23/2025",
}

submission_17 = {
    "quiz_name": "Quiz 1: Order of Operations",
    "quiz_module": "Math",
    "quiz_score": 72.3,
    "student_id": 558062,
    "student_name": "Bruce Wayne",
    "submission_date": "9/19/2025",
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
    submission_17,
]


# Student Roster
student_roster = [
    "Jimmy Johns",
    "Little BoPeep",
    "Winter Woods",
    "Molly Moffat",
    "Jenny Williams",
    "Bruce Wayne",
]
# filter_by_date("9/19/2025", collection_of_submissions)
# Use the one below
# list_of_students_by_date = filter_by_date("9/30/2025", collection_of_submissions)
# print(list_of_students_by_date)

# list_of_students_by_student_iD = filter_by_student_id(582702, collection_of_submissions)
# print(list_of_students_by_student_iD)

# Work in Progress
list_of_students_missing_all_assignments = find_unsubmitted(
    "9/19/2025", student_roster, collection_of_submissions
)
print(list_of_students_missing_all_assignments)
