def filter_by_date(submission_date, submissions_list):
    """
    Filters the submissions by specified date
    Parameters:
        submission_date (string) : date value in 'YYYY-MM-DD'
        submissions_list (A list of dictionary objects): A list of dictionary objects containing student data and assignments
    Returns:
        list: submission objects with a submission_date equal to the date specified
    """

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
            list: submission objects with a submission_id equal to the student_id specified
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
    """

    list_of_students_with_at_least_one_submission = []
    list_of_students_missing_all_assignments = []
    for person in submissions_list:
        if (person["student_name"] in student_names_list) and (
            submission_date == person["submission_date"]
        ):
            list_of_students_with_at_least_one_submission.append(person["student_name"])

    set_of_students_missing_all_assignments = set(student_names_list) - set(
        list_of_students_with_at_least_one_submission
    )
    list_of_students_missing_all_assignments = list(
        set_of_students_missing_all_assignments
    )
    return list_of_students_missing_all_assignments


def get_average_score(submissions_list):
    """
    Calculates the average score from submissions
    Parameters:
        submissions_list (A list of dictionary objects): A list of dictionary objects containing student data and assignments
    Returns:
        float: average of the quiz scores
    """

    quiz_score_list = []
    for score in submissions_list:
        quiz_score_list.append(score["quiz_score"])

    average = sum(quiz_score_list) / len(quiz_score_list)
    return round(average, 1)


def get_average_score_by_module(submissions_list):
    """
    Calculates the average score of each quiz module
    Parameters:
        submissions_list (A list of dictionary objects): A list of dictionary objects containing student data and assignments
    Returns:
        object: module key and average
    """

    dict_totals_by_module = {}
    for quiz in submissions_list:
        module_name = quiz["quiz_module"]
        module_score = quiz["quiz_score"]

        if module_name in dict_totals_by_module:
            dict_totals_by_module[module_name]["total_score"] += module_score
            dict_totals_by_module[module_name]["count"] += 1
        else:
            dict_totals_by_module[module_name] = {
                "total_score": module_score,
                "count": 1,
            }

    dict_average_by_module = {}
    for module_name, value in dict_totals_by_module.items():
        average = value["total_score"] / value["count"]
        dict_average_by_module[module_name] = round(average, 1)
    return dict_average_by_module


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


student_roster = [
    "Jimmy Johns",
    "Little BoPeep",
    "Winter Woods",
    "Molly Moffat",
    "Jenny Williams",
    "Bruce Wayne",
]

list_of_students_by_date = filter_by_date("9/23/2025", collection_of_submissions)
print("Students Filtered by Date: ", list_of_students_by_date, "\n")

list_of_students_by_date = filter_by_date("9/30/2025", collection_of_submissions)
print("Students Filtered by Date: ", list_of_students_by_date, "\n")


list_of_students_by_student_id = filter_by_student_id(582702, collection_of_submissions)
print("Students Filtered by ID: ", list_of_students_by_student_id, "\n")

list_of_students_by_student_id = filter_by_student_id(500000, collection_of_submissions)
print("Students Filtered by ID: ", list_of_students_by_student_id, "\n")


list_of_students_missing_all_assignments = find_unsubmitted(
    "9/23/2025", student_roster, collection_of_submissions
)
print(
    "Students Missing All Assignments for Date Specified: ",
    list_of_students_missing_all_assignments,
    "\n",
)

list_of_students_missing_all_assignments = find_unsubmitted(
    "9/30/2025", student_roster, collection_of_submissions
)
print(
    "Students Missing All Assignments for Date Specified: ",
    list_of_students_missing_all_assignments,
    "\n",
)


average_quiz_score = get_average_score(collection_of_submissions)
print("Average Score of All Quizzes: ", average_quiz_score, "\n")


module_averages = get_average_score_by_module(collection_of_submissions)
print("Average Quizzes by Module: ", module_averages, "\n")
