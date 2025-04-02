import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
df =pd.read_csv("C:\\Users\\Aishwarya\\Downloads\\WA_Fn-UseC_-Telco-Customer-Churn.csv")
print(df)

#Plotting pie chart to check the churn values yes or no
gb=df.groupby('Churn').agg({'Churn':'count'})
print(gb)
plt.pie(gb['Churn'],labels=gb.index,autopct="%1.2f%%")
plt.title("Percentage Of Churned Customers",fontsize=10)
plt.show()

#Checking for specific number of top values
print(df.head(20))

#checking for null value
print("Total number of null values:",df.isnull().sum().sum())

#replacing null values in the column Total charges with '0' and changing datatypes of Total Charges from object to float
df['TotalCharges']=df['TotalCharges'].replace(" ","0")
df['TotalCharges']=df['TotalCharges'].astype("float")
df.info()

#Describing some mathematical calculations of data
print(df.describe())

#Checking for duplicated value
print("Total number of duplicated value:",df.duplicated().sum())

#Checking for duplicated value in the CustomerID column which has unique values
print("Total number of duplicated value ij CustomerID column:",df["customerID"].duplicated().sum())

#Converting value 1=Yes and 0=No in the seniorcitizen column
def conv(value):
    if value==1:
        return "Yes"
    else:
        return "No"
df["SeniorCitizen"]=df["SeniorCitizen"].apply(conv)
print(df)

#Checking for specific number of top values
print(df.head(40))

#Plotting bar graph to check number of peoples who has churned and not churned
ax=sns.countplot(x=df['Churn'])
ax.bar_label(ax.containers[0])
plt.title("Count Of Customers By Churned Values",fontsize=10)
plt.show()

#Plotting bar graph to check customer data on the basis of gender
ax=sns.countplot(x='gender',data=df,hue='Churn')
ax.bar_label(ax.containers[0])
plt.title("Count Of Churned Customers By gender",fontsize=10)
pl.figure(figsize=(5,5))
plt.show()

#Plotting bar graph to check customer data vs Senior Citizen counts
ax=sns.countplot(x='SeniorCitizen',data=df,hue='Churn')
ax.bar_label(ax.containers[0])
plt.title("Count Of Churned Customers vs SeniorCitizen count",fontsize=10)
pl.figure(figsize=(5,5))
plt.show()

#Plotting bar graph to check customer count of Senior Citizen
ax=sns.countplot(x='SeniorCitizen',data=df,)
ax.bar_label(ax.containers[0])
plt.title("Churned Customers count of SeniorCitizen",fontsize=10)
pl.figure(figsize=(5,5))
plt.show()


#Stack bar chart for the Churned Costomers vs Senior citizen % data
data_counts = df.groupby(['SeniorCitizen', 'Churn']).size().unstack()
data_percent = data_counts.div(data_counts.sum(axis=1), axis=0) * 100

fig, ax = plt.subplots(figsize=(5, 5))
data_percent.plot(kind='bar', stacked=True, ax=ax, colormap='viridis')

# Add percentage labels
for i, bars in enumerate(ax.containers):
    for bar in bars:
        height = bar.get_height()
        if height > 0:
            ax.text(bar.get_x() + bar.get_width() / 2, bar.get_y() + height / 2,
                    f'{height:.1f}%', ha='center', va='center', fontsize=10, color='white', fontweight='bold')

# Titles and labels
plt.title("Stacked Bar Chart of Churn Customers vs SeniorCitizen", fontsize=12)
plt.xlabel("Senior Citizen")
plt.ylabel("Percentage (%)")
plt.xticks(rotation=0)
plt.show()
#Comparitively larger number of Senior Citizens are Churned out


#Plotting histogram of churned vs tenure
plt.figure(figsize=(7,3))
sns.histplot(x="tenure",data=df,bins=72, hue="Churn")
plt.show()
#People of long tenure are not churned and people with tenure 1-2 months have churned most

#Bar graph of Count of customers vs Contract period
ax=sns.countplot(x='Contract',data=df,hue="Churn")
ax.bar_label(ax.containers[0])
plt.title("Churned Customers count vs Contract period",fontsize=10)
pl.figure(figsize=(5,5))
plt.show()
#People with month to month contract are likely to churn most as compaired to people with longer duration contract

print(df.columns.values)

columns = ['PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity',
           'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV',
           'StreamingMovies']

# Set up the subplots
fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(15,12))
axes = axes.flatten()
# Create count plots for each column
for i, col in enumerate(columns):
    sns.countplot(data=df, x=col, ax=axes[i], palette='viridis',hue="Churn")
    axes[i].set_title(f'Count Plot of {col}')
    axes[i].set_xlabel(col)
    axes[i].set_ylabel('Count')
    axes[i].tick_params(axis='x', rotation=30)

plt.tight_layout()
plt.show()
#The count plots visualize the distribution of various telecom services among customers, categorized by
# churn status (Yes/No). Services like PhoneService, InternetService, OnlineSecurity, and Streaming TV show
# clear differences in churn behavior. Customers with Fiber Optic Internet and no security services seem more likely to churn.
# The data highlights that support-related services (TechSupport, OnlineBackup, and DeviceProtection) also impact customer retention.


#Count plot of Churned customers by Payment Method
ax=sns.countplot(x='PaymentMethod',data=df,hue="Churn")
ax.bar_label(ax.containers[0])
plt.title("Churned Customers count vs PaymentMethod",fontsize=10)
plt.figure(figsize=(5,5))
plt.show()
#There is high possibility that customer will churn if he is using Electronic Payment method








