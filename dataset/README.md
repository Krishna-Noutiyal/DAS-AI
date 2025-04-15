# Datasets

---
The datasets in this directories come from [DASS Dataset Filteration](https://github.com/Krishna-Noutiyal/DASS-Dataset-Filteration.git) repository. Each dataset has some unique characteristics and is intended for specific use cases.

## Dataset Descriptions

---

### categorized_datav4_scored.csv

- **Description**: This dataset contains categorized data with 4 new columns, depression_score, anxiety_score, stress_score and das_score assigned to each entry. It is useful for tasks that require classification and scoring of data points.

- **depression_score** : Score of depression for entry. Range is 0-56.
- **anxiety_score** : Score of anxiety for entry. Range is 0-56.
- **stress_score** : Score of stress for entry. Range is 0-56.
- **das_score** : Score of depression, anxiety and stress for entry. Range is 0-100. ( Its percentage of summation of depression_score, anxiety_score and stress_score ). Formula : upper(((depression_score + anxiety_score + stress_score) / 168) * 100)
