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
    return


def filter_by_student_id(student_id, submission_list):
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
    return


def find_unsubmitted(date, submission_list):
    """
    Filters submissions to find missing entries
    Parameters:
        submission_date (string) : date value in 'YYYY-MM-DD'
        submissions_list (A list of dictionary objects): A list of dictionary objects containing student data and assignments
    Returns:
        float: average of all the quiz scores
    Raises:
        ValueError: (may delete if not used)
    """
    return


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
