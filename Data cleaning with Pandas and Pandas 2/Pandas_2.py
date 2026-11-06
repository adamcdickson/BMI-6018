import pandas as pd
import numpy as np

#Question 1
p = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
q = pd.Series([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

q_1 = (((p - q) ** 2).sum()) ** 0.5

print(q_1)

#Question 2
df = pd.DataFrame(
    np.arange(20).reshape(-1, 5),
    columns=list("abcde")
)

q_2 = df[["c", "b", "a", "d", "e"]]

print(q_2)

#Question 3- I swapped column a and b since it didn't specify for the q_3 output but it should work for any.
df = pd.DataFrame(
    np.arange(20).reshape(-1, 5),
    columns=list("abcde")
)

def swap_columns(dataframe, first_column, second_column):
    columns = dataframe.columns.tolist()
    first_position = columns.index(first_column)
    second_position = columns.index(second_column)
    columns[first_position], columns[second_position] = (
        columns[second_position],
        columns[first_position]
    )
    return dataframe[columns]

q_3 = swap_columns(df, "a", "b")

print(q_3)

#Question 4
df = pd.DataFrame(
    np.random.random(4) ** 10,
    columns=["random"]
)

pd.set_option("display.float_format", "{:.4f}".format)

q_4 = df

print(q_4)

pd.reset_option("display.float_format")
#unsure if this would mess up the next 2 questions so I added the reset command

#Question 5
df = pd.DataFrame(
    np.random.randint(1, 100, 40).reshape(10, -1),
    columns=list("pqrs"),
    index=list("abcdefghij")
)

values = df.to_numpy()

distances = np.sqrt(
    ((values[:, np.newaxis] - values[np.newaxis, :]) ** 2).sum(axis=2)
)

np.fill_diagonal(distances, np.inf)

nearest_positions = distances.argmin(axis=1)

df["nearest_row"] = df.index[nearest_positions]

df["dist"] = np.round(
    distances[np.arange(len(df)), nearest_positions]
)

q_5 = df

print(q_5)

#Question 6
data = {
    "A": [45, 37, 0, 42, 50],
    "B": [38, 31, 1, 26, 90],
    "C": [10, 15, -10, 17, 100],
    "D": [60, 99, 15, 23, 56],
    "E": [76, 98, -0.03, 78, 90]
}

df = pd.DataFrame(data)

q_6 = df.corr()

print(q_6)

