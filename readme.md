![logo_ironhack_blue 7](https://user-images.githubusercontent.com/23629340/40541063-a07a0a8a-601a-11e8-91b5-2f13e4e6b441.png)

# Lab | Customer Analysis Round 4

In today's lesson we talked about continuous distributions (mainly normal distribution), linear regression and how multicollinearity can impact the model. In this lab, we will test your knowledge on those things using the 'marketing_customer_analysis.csv' file. You have been using the same data in the previous labs (Rounds 2 and 3). You can continue using the same Jupyter file. The file can be found in the 'files_for_lab' folder.

### Get the data 

Use the Jupyter file from the last lab (Customer Analysis Round 3)

### Complete the following tasks 

- Check the data types of the columns. 
- Place the the numeric data into a dataframe called 'numerical' and the categorical columns in a dataframe called categorical'.
TIP: You can use ```python np.number  ``` and ```python np.object  ``` to select the numerical data types and categorical data types respectively. 
- Now we will try to check the normality of the numerical variables visually
  - Use the seaborn library to construct distribution plots for the numerical variables
  - Use Matplotlib to construct histograms
  - Standardize the distributions for different numerical variables to look like normal distributions 
- For the numerical variables, check the multicollinearity between the features. Please note that we will use the column 'total_claim_amount' later as the target variable. 
- Drop one of the two features that show a high correlation between them (greater than 0.9). Write code for both the correlation matrix and for seaborn heatmap. If there is no pair of features that have a high correlation, then do not drop any features
