# ecommerce-data-analysis-dashboard
### data link : "https://www.kaggle.com/datasets/ruchi798/shopping-cart-database/data"
# Project steps 
### 1) Loaded all files 
  - `customers.csv`
  - `orders.csv`
  - `products.csv`
  - `sales.csv`
### 2) Merged all data into one table:
  - `sales` with `orders` on `order_id`
  - Then with `products` on `product_id`
  - Then with `customers` on `customer_id`
### 3) Understanding Data 
  - Understand Columns
  - check dtype 
  - Describe Numerical Cols
  - Describe Categorical Cols
  - Catching any error
### 4) Data Cleaning "Handling any error" 
### 5) EXTRACT FEATURES 
### 6) Analysis questions
#### Univariate Analysis
    - 1- Which gender buys more from us .
    - 2- Which customer status buys more from us .
    - 3- what is the most seasons in the year best seller .
    - 4- The largest difference in days between the order date and the delivery date .
    - 5- Most state buy .
    - 6- Most city buy .
    - 7- Information about customers' ages .
    - 8- Best selling colours .
    - 9- Most product type of sales
    - 10- Information about each unit price
#### Bivariate Analysis
        - 1- The most common types of products are sold by seasons
        - 2- The cities that buy the most in each state
        - 3- Are order increasing over time
        - 4- Sales quantity for each product type
        - 5- What is the average delivery duration for each state 
        - 6- Total sales of each product type
        - 7- The top ten customers who bought from me
        - 8- Best selling sizes for each product type
        - 9- Does the size of the product affect the price?

### 7) Dash Board
