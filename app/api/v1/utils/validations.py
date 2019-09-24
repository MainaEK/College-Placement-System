"""
This contains the validators used by the schemas
"""
from marshmallow import ValidationError
import re


def Not_null_string(value):
    """Validates that string field under validation does not contain null value"""

    if isinstance(value, str):
        if not value.strip(' '):
            raise ValidationError('Sorry but this parameter cannot be null. Please fill in')
        return value
    elif value:
        return value


def password_check(password):
    """
    Validates that the password has achieved certain criteria
    """
    if len(password) < 8:
        raise ValidationError("Make sure your password is at least 8 letters")
    elif re.search('[0-9]', password) is None:
        raise ValidationError("Make sure your password has a number in it")
    elif re.search('[A-Z]', password) is None:
        raise ValidationError("Make sure your password has a capital letter in it")
    elif re.search('[a-z]', password) is None:
        raise ValidationError("Make sure your password has a small letter in it")
    else:
        return password
    