def validate_data_types(data, rules):
    errors = []
    for column, expected_type in rules.items():
        if column not in data.columns:
            errors.append(f"Column {column} not found.")
            continue

        column_data = data[column]
        try:
            data[column] = [expected_type(value) for value in column_data]
        except ValueError:
            errors.append(f"Expected type {expected_type} for column '{column}'. Got {column_data.dtype} instead.")
    return errors
