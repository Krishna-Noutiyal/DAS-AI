# Random Forest Models

This directory contains multiple models of randome forests. But due to the size limit model v2 and v3 are moved to onedrive storage. The link is provided below to download the models with its features.

 > <https://1drv.ms/u/c/d01d77966552c1dc/EdFLS-48g89PqS9qu8Wjw2oBObilidYRE9QovuKzyOZU_g?e=hfkwTQ>

## rfv1

---

This model is trained on the [categorized_v4_numeric.csv](data\categorized_v4_numeric.csv) dataset. This model is trained with native multivariate random forest algorigm without using multi output classifier provided by sklearn. The model is trained with 100 estimators. The model is trained and tested with 8:2 ration of data.

## rfv2

---

Similar to rfv2 but the dataset is standardized using StanderdScaler from sklearn. Better performance is achieved then rfv1

## rfv3

---

Similar to rfv2 but the dataset is standardized using MinMaxScaler from sklearn. Better performance is achieved compared to rfv2.
