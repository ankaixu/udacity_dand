#One way to define the function
def which_prize(points):
    """
    Returns the prize one wins given the number of points earned.
    """
    if 0 <= points <= 50:
        return "Congratulations! You have won a wooden rabbit!"
    elif 151 <= points <= 180:
        return "Congratulations! You have won a wafer-thin mint!"
    elif 181 <= points <= 200:
        return "Congratulations! You have won a penguin!"
    else:
        return "Oh dear, no prize this time."


#A second way to define the function
def which_prize2(points):
    """
    Returns the prize one wins given the number of points earned.
    """
    prize = None
    if 0 <= points <= 50:
        prize = "a wooden rabbit"
    elif 151 <= points <= 180:
        prize = "a wafer-thin mint"
    elif 181 <= points <= 200:
        prize = "a penguin"

    if prize:
        return "Congratulations! You have won " + prize + "!"
    else:
        return "Oh dear, no prize this time."
