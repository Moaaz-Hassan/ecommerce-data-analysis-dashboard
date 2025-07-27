# to write a new file .py for the dash borad


# Import necessary libraries for data handling and visualization
import pandas as pd 
import numpy as np 
import plotly.express as px 
import streamlit as st 
import plotly.figure_factory as ff


# Set up the page layout and title for the dashboard
st.set_page_config(page_title = 'Simple DashBoard')


# page titell
st.title("Dashboard data analysis project")

# read the data fram 
df = pd.read_csv('New_version_data.csv')
df_products = pd.read_csv("Shopping Cart Database/products.csv")


# this slider for chooeing the number of rowes
n_rowes = st.slider("chooes number of rowes " , min_value = 5 , max_value = len(df) , step=1)
st.write(df[:n_rowes]) # print the data fram with the number of row 

st.write("\n") # new line 


# this selectbox for chooeing the type of analysis
analysis_type = st.selectbox("chooes the type of analysis " ,["Univariate","Bivariate"]) 
# button return true if clekd on 
botom=st.button("Go...!") 

if botom : # if button some one clekd on 
    if analysis_type == "Univariate" : #  the type of analysis
        st.write("# Univariate Analysis Questions are 10 ")
        cal_1,cal_2 = st.columns(2)
        with cal_1 :
            st.write("#### 1- Which gender buys more")
            st.write("#### 2- Which customer status buys more")
            st.write("#### 3- what is the seasons best seller")
            st.write("#### 4- Duration difference between order date and delivery date")
            st.write("#### 5- Most state buy")

        with cal_2 :
            st.write("#### 6- Most city buy")
            st.write("#### 7- Information about customers' ages")
            st.write("#### 8- Best selling colours")
            st.write("#### 9- Most product type of sales")
            st.write("#### 10- Information about each unit price")

        st.write("\n")
        st.write("\n")
        st.write("### Questions 1")
        gender= df["gender"].value_counts().to_frame().reset_index()
        gender.columns = ["gender" , "number"]
        Univariate_Questions_1 = px.bar(data_frame=gender , x="gender" , y="number" , title="gender buys from us" , color="gender" , color_discrete_sequence=px.colors.qualitative.G10 , text_auto=True)
        st.plotly_chart(Univariate_Questions_1)
 

        st.write("\n")
        st.write("\n")
        st.write("### Questions 2")
        Status = df["Customer_Status"].value_counts().reset_index()
        Status.columns = ["Customer_Status" , "number"]
        Univariate_Questions_2 = px.pie(data_frame=Status , values="number" , names="Customer_Status" ,title="customer status" , color_discrete_sequence=px.colors.qualitative.Antique)
        st.plotly_chart(Univariate_Questions_2)
        


        st.write("\n")
        st.write("\n")
        st.write("### Questions 3")
        seasons = df["order_seasons"].value_counts().reset_index()
        seasons.columns = ["order_seasons" , "number"]
        Univariate_Questions_3 = px.bar(data_frame=seasons , x="order_seasons" , y="number" , title="seasons in the year best seller" , color="order_seasons" , color_discrete_sequence=px.colors.qualitative.G10 , text_auto=True)
        st.plotly_chart(Univariate_Questions_3)



        st.write("\n")
        st.write("\n")
        st.write("### Questions 4")
        Univariate_Questions_4 = px.histogram(data_frame=df , x="delivery_duration" , title="difference in days between the order date and the delivery date" , text_auto=True, nbins=50)
        st.plotly_chart(Univariate_Questions_4)



        st.write("\n")
        st.write("\n")
        st.write("### Questions 5")
        state = df["state"].value_counts().reset_index()
        state.columns = ["state" , "number"]
        Univariate_Questions_5 = px.bar(data_frame=state , x="state" , y="number" , title="Most state buy" , color="state" , color_discrete_sequence=px.colors.qualitative.Light24_r , text_auto=True )
        st.plotly_chart(Univariate_Questions_5)


        st.write("\n")
        st.write("\n")
        st.write("### Questions 6")
        city = df["city"].value_counts().reset_index()
        city.columns = ["city" , "number"]
        Univariate_Questions_6 = px.scatter(data_frame=city , x="city" , y="number" , title="Most city buy" , color="city" , color_discrete_sequence=px.colors.qualitative.Light24_r)
        st.plotly_chart(Univariate_Questions_6)



        st.write("\n")
        st.write("\n")
        st.write("### Questions 7")
        Univariate_Questions_7 = ff.create_distplot([df.age.to_list()] , group_labels=["ages"] , show_hist=False ,  bin_size=.1, show_rug=False  )
        Univariate_Questions_7.update_layout(title_text="age distributions")
        st.plotly_chart(Univariate_Questions_7)


        st.write("\n")
        st.write("\n")
        st.write("### Questions 8")
        colour= df["colour"].value_counts().to_frame().reset_index()
        colour.columns = ["colour" , "number"]
        Univariate_Questions_8 = px.bar(data_frame=colour , x="colour" , y="number" , title="Best selling colours" , color="colour" ,color_discrete_sequence=df["colour"].value_counts().index.to_list() , text_auto=True)
        st.plotly_chart(Univariate_Questions_8)



        st.write("\n")
        st.write("\n")
        st.write("### Questions 9")
        product_type = df["product_type"].value_counts().reset_index()
        product_type.columns = ["product_type" , "number"]
        Univariate_Questions_9 = px.pie(data_frame=product_type ,values="number" , names="product_type" ,title="Most product type of sales" , color_discrete_sequence=px.colors.qualitative.Dark2)
        st.plotly_chart(Univariate_Questions_9)



        st.write("\n")
        st.write("\n")
        st.write("### Questions 10")
        Univariate_Questions_10 = ff.create_distplot([df_products.quantity.to_list()] , group_labels=["price"] , show_hist=False ,  bin_size=.10, show_rug=False  )
        Univariate_Questions_10.update_layout(title_text="unit price distributions")
        st.plotly_chart(Univariate_Questions_10)

        st.write("\n")
        st.write("\n")
        st.write("# Done, thanks for your attention")
    
    elif analysis_type == "Bivariate" :

        st.write("# Bivariate Analysis Questions are 9 ")
        cal_1,cal_2 = st.columns(2)
        
        with cal_1 :
            st.write("#### 1- common types of products sold by seasons")
            st.write("#### 2- cities that buy the most in each state")
            st.write("#### 3- dose order increasing over time")
            st.write("#### 4- Sales quantity for each product type")
            st.write("#### 5- What is the average delivery duration for each state ")

        with cal_2 :
            st.write("#### 6- Total sales of each product type")
            st.write("#### 7- top ten customers who bought from me")
            st.write("#### 8- Best selling sizes for each product type")
            st.write("#### 9- Does the size of the product affect the price?")



        st.write("\n")
        st.write("\n")
        st.write("### Questions 1")
        Bivariate_Questions_1 = px.histogram(data_frame=df , x="order_seasons" ,y="quantity", color="product_type" ,  color_discrete_sequence=px.colors.qualitative.Bold , text_auto=True , title="The most common types of products are sold by seasons")
        st.plotly_chart(Bivariate_Questions_1)



        st.write("\n")
        st.write("\n")
        st.write("### Questions 2")
        Bivariate_Questions_2_1 =  px.strip(data_frame=df , x="state" ,y="order_id" , color="city" ,color_discrete_sequence=px.colors.qualitative.Bold , title="The cities that buy the most in each state"  )
        st.plotly_chart(Bivariate_Questions_2_1)
        Bivariate_Questions_2_2 = px.bar(data_frame=df , x="state" , color="city" ,color_discrete_sequence=px.colors.qualitative.Bold , title="The cities that buy the most in each state"  )
        st.plotly_chart(Bivariate_Questions_2_2)




        st.write("\n")
        st.write("\n")
        st.write("### Questions 3")
        Bivariate_Questions_3 = px.scatter(data_frame= df, x="order_date" ,color="month_name" , color_discrete_sequence=px.colors.qualitative.Bold , title=" Are order increasing over "  )
        st.plotly_chart(Bivariate_Questions_3)


        st.write("\n")
        st.write("\n")
        st.write("### Questions 4")
        Sales_quantity = df.groupby("product_type")["quantity"].sum().reset_index()
        Bivariate_Questions_4 = px.bar(data_frame=Sales_quantity , x="product_type" , y="quantity" , text_auto=True , title=" Sales quantity for each product type" , color="product_type" ,color_discrete_sequence=px.colors.qualitative.Safe )
        st.plotly_chart(Bivariate_Questions_4)


        st.write("\n")
        st.write("\n")
        st.write("### Questions 5")
        average_delivery_duration =df.groupby("state")["delivery_duration"].mean().reset_index()
        average_delivery_duration["delivery_duration"] = average_delivery_duration["delivery_duration"].astype("int")
        Bivariate_Questions_5 = px.bar(data_frame=average_delivery_duration , x="state" , y="delivery_duration" , text_auto=True , title="average delivery duration for each state " , color="state" ,color_discrete_sequence=px.colors.qualitative.T10 )
        st.plotly_chart(Bivariate_Questions_5)



        st.write("\n")
        st.write("\n")
        st.write("### Questions 6")
        sales_of_each_product_type = df.groupby("product_type")["total_price"].sum().reset_index()
        Bivariate_Questions_6 = px.bar(data_frame=sales_of_each_product_type , x="product_type" , y="total_price" , text_auto=True , title="Total sales of each product type" , color="product_type" ,color_discrete_sequence=px.colors.qualitative.T10)
        st.plotly_chart(Bivariate_Questions_6)


        st.write("\n")
        st.write("\n")
        st.write("### Questions 7")
        top_ten_customers=df.groupby(["customer_id" ,"customer_name"])["order_id"].count().to_frame().reset_index().sort_values(by="order_id" , ascending=False)
        top_ten_customers.columns = ["customer_id","customer_name" , "number"]
        top_ten_customers = top_ten_customers.iloc[:10]
        Bivariate_Questions_7 = px.bar(data_frame=top_ten_customers,x="customer_name" , y="number" , text_auto=True , title="The top ten customers who bought from me" , color="customer_name" ,color_discrete_sequence=px.colors.qualitative.Light24)
        st.plotly_chart(Bivariate_Questions_7)



        st.write("\n")
        st.write("\n")
        st.write("### Questions 8")
        Best_selling_sizes = df.groupby(["product_type","size"])["quantity"].sum().to_frame().reset_index()
        Bivariate_Questions_8 = px.bar(data_frame=Best_selling_sizes , x="product_type" , y= "quantity" ,color="size"  , text_auto=True , title="Best selling sizes for each product type" , color_discrete_sequence=px.colors.qualitative.Dark2)
        st.plotly_chart(Bivariate_Questions_8)




        st.write("\n")
        st.write("\n")
        st.write("### Questions 9")
        OrdinalEncoder_for_size= {'XS':1, 'S':2, 'M':3, 'L':4, 'XL':5}
        dict_size = {"size" : df["size"].map(OrdinalEncoder_for_size) ,"price_per_unit" : df["price_per_unit"]}
        dict_size = pd.DataFrame(dict_size)

        Bivariate_Questions_9 = px.imshow(dict_size.corr().round(2), text_auto=True)
        st.plotly_chart(Bivariate_Questions_9)

        st.write("\n")
        st.write("\n")
        st.write("# Done, thanks for your attention")












        




