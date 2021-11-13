
class ParseException(Exception):
    pass


class ValidationError(Exception):
    pass


class EmptyValueError(ValidationError):
    pass