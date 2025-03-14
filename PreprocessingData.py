import pandas as pd


def find_missing_values_columns(file_path):
    # Load the dataset
    df = pd.read_csv(file_path)

    # Iterate through columns and count missing values ('?')
    for col in df.columns:
        missing_count = (df[col] == '?').sum()
        if (missing_count == 0):
            continue
        print(f"{col}: {missing_count} missing values")


def remove_missing_values(file_path):
    df = pd.read_csv(file_path)

    # Remove rows where any of diag_1, diag_2, or diag_3 contain '?' or where 'race' or 'max_glu_serum' are null
    # df_cleaned = df[
    #     (df["diag_1"] != '?') &
    #     (df["diag_2"] != '?') &
    #     (df["diag_3"] != '?') &
    #     (df["race"].notna()) &
    #     (df["max_glu_serum"].notna())
    # ]
    df_cleaned = df[
        (df["diag_1"] != '?') &
        (df["diag_2"] != '?') &
        (df["diag_3"] != '?') &
        (df["race"]!= '?')
    ]

    # Save the cleaned dataset
    cleaned_file_path = "data/diabetic_data_cleaned.csv"
    df_cleaned.to_csv(cleaned_file_path, index=False)

    # Print the number of rows in the cleaned dataset
    print(f"Number of rows in the cleaned dataset: {len(df_cleaned)}")
    print(f"Cleaned dataset saved to: {cleaned_file_path}")


# remove weights, payer_code, medical_specialty
def remove_unneeded_columns(file_path):
    df = pd.read_csv(file_path)

    # Drop specified columns
    columns_to_drop = ["weight", "payer_code", "medical_specialty", "max_glu_serum", "A1Cresult"]
    df_cleaned = df.drop(columns = columns_to_drop, errors = 'ignore')

    # Save the cleaned dataset
    cleaned_file_path = "data/diabetic_data_cleaned.csv"
    df_cleaned.to_csv(cleaned_file_path, index = False)

    print(f"Cleaned dataset saved to: {cleaned_file_path}")

def race_count(file_path):
    df = pd.read_csv(file_path)

    # Remove rows where any of diag_1, diag_2, or diag_3 contain '?'
    df_cleaned = df[(df["A1Cresult"] != '?')]

    # Save the cleaned dataset
    cleaned_file_path = "data/diabetic_data_cleaned.csv"
    df_cleaned.to_csv(cleaned_file_path, index = False)

    print(f"Cleaned dataset saved to: {cleaned_file_path}")

    # Filter rows where 'weight' is not NaN
    count = df['A1Cresult'].notna().sum()

    print(f"Number of rows with a weight value: {count}")

def droping_again(file_path):
    # Read the CSV into a DataFrame
    df = pd.read_csv(file_path)

    # Drop the 'A1Cresult' column
    df = df.drop(columns = ['A1Cresult'])

    # Remove rows where 'max_glu_serum' is missing
    df = df.dropna(subset = ['max_glu_serum'])

    # Save the cleaned DataFrame to a new CSV
    df.to_csv("data/KNN_cleaned_data.csv", index = False)


if __name__ == '__main__':
    # file_path = "data/diabetic_data.csv"
    # file_path = "data/KNN_cleaned_data.csv"
    # remove_missing_values("data/diabetic_data.csv")
    # remove_unneeded_columns("data/KNN_cleaned_data.csv")
    find_missing_values_columns("data/diabetic_data_cleaned.csv")