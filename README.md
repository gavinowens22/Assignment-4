# Assignment-4

# Iris Data Analysis

## Purpose
For this assignment our tasks was to use Python and Pandas to observe the differences between three types of irises. From the data we were given the petal and sepa; measurements for each of the flowers. With that data I was able to find the correlations, averages, medians, and the standard deviations. From these calculations we were able to see which of the 3 species were the most and least similar.



## Intation

First, I imported pandas and the files we used 'Petal_Data. csv' and 'Sepal_Data.csv'. Then we merged the two datasets together using the sample ID and species. Doing this made sure that the measurements for the same flower were together.
After merging the data, I removed the extra columns that were not needed. I then made a DataFrame that only included petal length, petal width, sepal length, and sepal width.


We used 5 operations
.corr() to find the correlation
.mean() to find the mean
.median() to find the median
.std() to find standard deviation

## Results

The strongest correlation was between petal length and petal width at about 0.943. This shows that as the petal length gets larger, the petal width also usually gets larger.

The averages were:

- Petal length: 3.751
- Petal width: 1.195
- Sepal length: 5.766
- Sepal width: 3.079

The medians were:

- Petal length: 4.292
- Petal width: 1.372
- Sepal length: 5.778
- Sepal width: 3.096

The standard deviations were:

- Petal length: 1.724
- Petal width: 0.744
- Sepal length: 0.735
- Sepal width: 0.465

## Species Comparison

Versicolor and Virginica were the most similar species. The sepal measurements were the closest. T. Versicolor had an average sepal length of 5.943 and T. virginica had an average of 6.355. Their average sepal widths were also close at 2.762 for Versicolor and 3.002 for Virginica.

Setosa and Virginica were the least similar. 
## Limitations


The dataset only includes 150 flowers from three species, so the results are limited to those samples and may not represent every iris of those species.

