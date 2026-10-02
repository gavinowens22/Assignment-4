import pandas as pd

# 1
petal_data = pd.read_csv("Petal_Data.csv")
sepal_data = pd.read_csv("Sepal_Data.csv")

iris_data = pd.merge(
    petal_data,
    sepal_data,
    on=["sample_id", "species"]
)

iris_data = iris_data.drop(
    columns=["Unnamed: 0_x", "Unnamed: 0_y"]
)

print(iris_data)


# 2
measurements = iris_data[
    ["petal_length", "petal_width", "sepal_length", "sepal_width"]
]

correlations = measurements.corr()

print("Correlations:")
print(correlations)


# 3
averages = measurements.mean()

print("Averages:")
print(averages)


# 4
medians = measurements.median()

print("Medians:")
print(medians)


# 5
standard_deviation = measurements.std()

print("Standard Deviations:")
print(standard_deviation)


# 6
species_averages = iris_data.groupby("species")[
    ["petal_length", "petal_width", "sepal_length", "sepal_width"]
].mean()

print("Species Averages:")
print(species_averages)
