from password_validator import PasswordValidator


def check_pass(value):
    # Create a schema
    schema = PasswordValidator()

    # Add properties to it
    schema \
        .uppercase()\
        .lowercase()\
        .digits()\
        .symbols()

    result = schema.validate(value)

    # print(schema.validate('validPASS123'))
    # print(schema.validate('invalid12'))

    return result

# check_pass('sdsfSFSF1/')
