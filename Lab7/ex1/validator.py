import pandas as pd
from .csv_rules import *


def run_validation(file_path, rules):
    data = pd.read_csv(file_path)
    errors = []

    missing_values_error = missing.check_missing_values(data)
    if missing_values_error:
        errors.append(missing_values_error)

    data_types_errors = data_types.validate_data_types(data, rules)
    errors.extend(data_types_errors)

    return errors
