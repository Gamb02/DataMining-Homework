# DataMining-Homework
This project is focused on the extraction of **association rules** from a dataset of transactions using two **Market Basket Analysis algorithms**: **Apriori** and **FP-Growth**.

## Technologies used
-  **Pandas**: data manipulation
-  **Mlxtend**: Apriori, FP-Growht and association rules function
-  **Matplotlib**: data visualization

I developed three Python modules to make more easy the implementation:
- "dataCleaning"
- "preAnalisys"
- "data_rappresentation".


## Data Preprocessing
To have good results, the dataset needs to was cleaned by:
-  Nan values
-  Unuseless values
-  Product with low support
-  Transaction with only one product

After filtering, the dataset was trasformed into binary transaction matrix
-   1 means the product is present in the transaction
-   0 means it

To do that, I have developed the *dataCleaning* and *preAnalisys* libraries that includes all these operations 

## Data visualization
To make more easy and speedy the data visualization I have developed *data_rappresentation*. That was created using *Matplotlib*

## Marlet Basket Analisys
After all the preprocessing operations I can finally apply
-  Apriori
-  FP-Growht
  After generating frequent itemsets, the association rules can be extracted

