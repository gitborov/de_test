from password_validator import PasswordValidator


def main():
    # Create a schema
    schema = PasswordValidator()

    # Add properties to it
    schema \
        .min(8) \
        .max(100) \
        .has().uppercase() \
        .has().lowercase() \
        .has().digits() \
        .has().no().spaces()

    # Validate against a password string
    print(schema.validate('validPASS123'))
    print(schema.validate('invalidPASS'))


if __name__ == '__main__':
    main()
