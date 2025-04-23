# Random Forest Models

This directory contains multiple ML models of random forest regression algorithms trained on different datasets. But due to the size limit, all of the models are moved to OneDrive storage. The link is provided below to download the models with its features.

 > <https://1drv.ms/u/c/d01d77966552c1dc/EQ4w9U80kj5NnP6VyGyNT30BZG9kiFKK1-PGHRLDSC9bDA?e=vQM1HR>

## rfv1

---

This model is trained on the [categorized_v4_numeric.csv](data\categorized_v4_numeric.csv) dataset. This model is trained with native multivariate random forest algorigm without using multi output classifier provided by sklearn. The model is trained with 100 estimators. The model is trained and tested with 8:2 ration of data.

## rfv2

---

Similar to rfv2, but the dataset is standardised using StandardScaler from sklearn. Better performance is achieved than rfv1

## rfv3

---

Similar to rfv2, but the dataset is standardised using MinMaxScaler from sklearn. Better performance is achieved compared to rfv2.
