def convert_to_numeric(score):
    """
    Converts score of any type into a score
    of type int or float.
    """
    return float(score)

def sum_of_middle_three(score1, score2, score3, score4, score5):
    """
    Finds the sum of the middle three scores.
    """
    return sum_middle_three

def score_to_rating_string():
    """
    Maps a numeric score to a text rating.
    """
    return rating

def scores_to_rating(score1, score2, score3, score4, score5):
    """
    Turns five scores into a rating by averaging the
    middle three scores and then mapping the average
    to a text rating.
    """

    #Convert scores to numbers
    score1 = convert_to_numeric(score1)
    score2 = convert_to_numeric(score2)
    score3 = convert_to_numeric(score3)
    score4 = convert_to_numeric(score4)
    score5 = convert_to_numeric(score5)

    #Find the average of the middle 3 scores
    average_score = sum_of_middle_three(score1,score2,score3,score4,score5)/3

    #Map the average to a text rating
    rating = score_to_rating_string(average_score)

    return rating
