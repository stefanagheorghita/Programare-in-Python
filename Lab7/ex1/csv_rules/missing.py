def check_missing_values(data):
    missing_values = data.isnull().sum().sum()
    if missing_values > 0:
        return f"There are {missing_values} missing values in the dataset"
    return None
