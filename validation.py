import re

class Validators:

    @classmethod
    def is_email(cls, value):
        return bool(re.match(r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+", value))

    @classmethod
    def is_phone(cls, value):
        return bool(re.match(r'(\+7|8)[- ]?\d{3}[- ]?\d{3}[- ]?\d{2}[- ]?\d{2}', value))

    @classmethod
    def is_date(cls, value):
        return bool(re.match(r'^(0[1-9]|1[0-2])[/\.-](0[1-9]|[12][0-9]|3[01])[/\.-](19\d\d|20\d\d|21\d\d)$', value) or re.match(r'^(19\d\d|20\d\d|21\d\d)[/\.-](0[1-9]|1[0-2])[/\.-](0[1-9]|[12][0-9]|3[01])$', value))

class Validation:

    DEFAULT_TYPE = 'TEXT'

    types_validators = {
        'DATE': Validators.is_date,
        'PHONE': Validators.is_phone,
        'EMAIL': Validators.is_email,
    }

    @classmethod
    def get_type(cls, value):
        for type, validator in cls.types_validators.items():
            if validator(value):
                return type
        return cls.DEFAULT_TYPE

print(Validators.is_date('12-12-2042'))
