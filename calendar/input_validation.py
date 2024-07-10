# input_validation.py

def validate_year(year):
    """
    Function to validate if the input year is a valid integer.
    """
    try:
        year = int(year)
        return True, year
    except ValueError:
        return False, None

def validate_month(month):
    """
    Function to validate if the input month is a valid integer between 1 and 12.
    """
    try:
        month = int(month)
        if 1 <= month <= 12:
            return True, month
        else:
            return False, None
    except ValueError:
        return False, None
