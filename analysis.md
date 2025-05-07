### Analysis Approach
The analysis grouped patients based on their BMI categories ("Underweight," "Normal," "Overweight," and "Obese") and calculated their average glucose levels, average age, and patient count for each group. The dataset was filtered to include only patients with BMI between 10 and 60. Lazy evaluation and the Parquet format were used to optimize memory and processing speed for large datasets.


### Patterns and Insights
The analysis revealed that obese patients had the highest average glucose levels, while underweight patients had the lowest. The overweight category had the largest number of patients, followed by the obese group. The obese group also had the highest average age.


### Efficiency Using Polars
Polars' lazy evaluation and columnar format (Parquet) allowed for efficient processing of large datasets by reducing memory usage. By deferring computations with scan_parquet() and using Parquet for faster data input and output, the analysis was both scalable and quick. Polars' powerful groupby and aggregation functions enabled efficient summarization of data, making it ideal for this cohort analysis.


### Result output: 
| bmi_range   | avg_glucose | patient_count | avg_age   |
|-------------|-------------|----------------|-----------|
| Underweight | 95.195115   | 26041          | 23.980646 |
| Overweight  | 116.373363  | 1165360        | 32.880893 |
| Normal      | 108.004737  | 664064         | 31.888848 |
| Obese       | 126.032016  | 3066409        | 33.82713  |

