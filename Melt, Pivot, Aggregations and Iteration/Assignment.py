import pandas as pd
from pathlib import Path

# Locate the dataset in this folder
folder_path = Path(__file__).resolve().parent

# Create a path to the dataset
data_file = folder_path / "breast-cancer.data"

# Read the breast-cancer data file into a DataFrame
df = pd.read_csv(data_file, header=None)

# Give the columns names so it's easier to work with
df.columns = [
    "recurrence_class",
    "age",
    "menopause",
    "tumor_size",
    "inv_nodes",
    "node_caps",
    "deg_malig",
    "breast",
    "breast_quad",
    "irradiat"
]

# Show the first five rows of the dataset
print(df.head())

#--MELT--

# Add a unique record number so each can be identified
df["record_id"] = range(1, len(df) + 1)

# Store the columns that identify each original record
columns_to_melt = ["record_id", "recurrence_class"]

# Reshape columns from wide format to long format
df_melted = df.melt(
    id_vars=columns_to_melt,
    value_vars=["age", "menopause", "tumor_size"],
    var_name="Measurement",
    value_name="Value"
)

# Display first five rows of the melt DF
print("\nMelt result:")
print(df_melted.head())

# --PIVOT--

# Reshape the melt DF back to wide format
df_pivoted = df_melted.pivot(
    index=columns_to_melt,
    columns="Measurement",
    values="Value"
)

# Move back from the index into regular columns.
df_pivoted = df_pivoted.reset_index()
df_pivoted.columns.name = None

# Display the first five rows of the pivoted DataFrame.
print("\nPivot result:")
print(df_pivoted.head())

# --AGGREGATION--

# Summarize data for degree of malignancy
deg_malig_summary = df["deg_malig"].aggregate(
    ["mean", "min", "max", "count"]
)

# Display the aggregation result
print("\nAggregation result:")
print(deg_malig_summary)

# --ITERATION--

# Loop through the first five records giving numbered rows and associated values
print("\nIteration result:")

for index, row in df.head(5).iterrows():
    print(
        "Record ID:", row["record_id"],
        "| Recurrence class:", row["recurrence_class"],
        "| Tumor size:", row["tumor_size"]
    )

# --GROUPBY--

# Group records by age group and calculate mean degree of malignancy and record count.
age_group_summary = df.groupby("age")["deg_malig"].agg(["mean", "count"])

# Show Groupby result in a new DF "age_group_summary"
print("\nGroupby result:")
print(age_group_summary)


