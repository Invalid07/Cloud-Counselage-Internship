#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns 


# In[2]:


df=pd.read_excel(r"C:\Users\Vikas\jupyter book\ex_files\Data analyst Data.xlsx")
df


# # 1. find how many uinque student r in data 

# # c: droping duplicated value by email id

# In[3]:


df=df[~(df["Email ID"].duplicated())]
df


# In[4]:


print("total unique values in the dataset is",2157)


# In[5]:


df.nunique()


# In[ ]:





# In[6]:


df.shape


# In[7]:


df.describe()


# In[8]:


df.dtypes


# # 2. what is avg gpa of the student

# In[10]:


df.rename(columns={"CGPA":"GPA"},inplace=True)


# In[11]:


df.GPA.mean()


# # 3 what is the distribution of student across different gradution year

# In[12]:


plt.figure(figsize=(15,5))
sns.histplot(df,x= "Year of Graduation" ,kde =True) #,kde =True)


# In[13]:


sns.kdeplot(df["Year of Graduation"]) #,kde =True)


# # 4. what is the distribution of student experience with python programming ?

# In[14]:


plt.figure(figsize=(15,5))
sns.kdeplot(df,x= "Experience with python (Months)" ,shade=True, color="red",alpha=0.6) #,kde =True)


# In[ ]:





# In[ ]:





# # 5.What is the average family income of the student?

# In[15]:


df["Family Income"]


# In[16]:


df["Family Income"].value_counts()


# In[17]:


df["Family Income"]=df["Family Income"].replace("7 Lakh+","8" )


# In[18]:


df["Family Income"]=df["Family Income"].replace("5-7 Lakh","7" )


# In[19]:


df["Family Income"]=df["Family Income"].replace("2-5 Lakh","5" )


# In[20]:


df["Family Income"]=df["Family Income"].replace("0-2 Lakh","2")


# In[21]:


df["Family Income"]=pd.to_numeric(df["Family Income"])


# In[22]:


q=df["Family Income"].mean()


# In[23]:


print (f"the  Avg income of the family in given dataset is {q}")


# In[ ]:





# # 6. How does the GPA vary among different colleges? (Show top 5 results only)

# In[28]:


t=df.groupby(["College Name"]).agg({"GPA":"mean"})
t.sort_values(by="GPA",ascending=False).head(5).plot(kind="bar",grid=True)


# In[25]:


df.groupby(["College Name"]).agg({"GPA":"mean"}).plot(kind="bar",figsize=(19,10),grid=True)


# # 7.Are there any outliers in the quantity (number of courses completed) attribute?

# In[124]:


plt.figure(figsize=(3,3))

plt.boxplot(df["Quantity"])
# sns.histplot(df["Quantity"])
plt.show()


# In[125]:


print("there is no outlier")


# # 8.what is the avergae GPAfor student from each city

# In[34]:


t=df.groupby("City").agg({"GPA":"mean"}).plot(kind="bar",figsize=(20,10),color="orange",alpha=1,grid=True)


# In[ ]:


print("  delhi and raipur some of higest GPA in the city  ")


# # 9. can u identify any relation between family income ang GPA

# In[35]:


from sklearn.preprocessing import LabelEncoder

df['Family Income'].unique()


# In[36]:


# Import label encoder
from sklearn import preprocessing
label_encoder = preprocessing.LabelEncoder()
df['Family Income']= label_encoder.fit_transform(df['Family Income'])
  
df['Family Income'].unique()


# In[37]:


sns.heatmap(df.corr() ,annot=True)


# In[38]:


#relation between monthly and total
sns.lmplot(x='Family Income',y='GPA',data = df)


# In[39]:


print("there is no relation in between gpa and family income")


# 

# # 10.How many students from various cities? (Solve using data visualisation tool).

# In[43]:


# no of of student from each city


# In[31]:


df.groupby(["City"]).agg({"City":"count"}).plot(kind="bar",figsize=(27,10),color="red",alpha=1,grid=True)


# In[45]:


# no of of student from each city in sorted according to count


# In[41]:


df["City"].value_counts().plot(kind="bar", figsize=(27,12))


# In[46]:


print("top 5 city are \n 1.Amreli \n2.jalor \n.jodhpur \n4.amer  \n5.mumbai")


# In[41]:


df.head(0)


# # how does the expected salary vary baseed on the factor  like "GPA","Family Income","Expericence with pythin (month)"
# 

# In[42]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



# Explore the relationship between GPA and Expected Salary using a scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x='GPA', y='Expected salary (Lac)', data=df)
plt.xlabel('GPA')
plt.ylabel('Expected Salary (Lac)')
plt.title('Relationship between GPA and Expected Salary')
plt.show()

# Explore the distribution of Expected Salary based on Family Income using a box plot
plt.figure(figsize=(10, 6))
sns.boxplot(x='Family Income', y='Expected salary (Lac)', data=df)
plt.xlabel('Family Income')
plt.ylabel('Expected Salary (Lac)')
plt.title('Distribution of Expected Salary based on Family Income')
plt.xticks(rotation=45)
plt.show()

# Calculate correlation between Experience with Python and Expected Salary
correlation = df['Experience with python (Months)'].corr(df['Expected salary (Lac)'])
print(f"Correlation between Experience with Python and Expected Salary: {correlation:.2f}")


# In[43]:


correlation = df['Experience with python (Months)'].corr(df['Expected salary (Lac)'])
print(f"Correlation between Experience with Python and Expected Salary: {correlation:.2f}")

# Create a scatter plot to visualize the relationship
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Experience with python (Months)', y='Expected salary (Lac)', data=df)
plt.xlabel('Experience with Python (Months)')
plt.ylabel('Expected Salary (Lac)')
plt.title('Relationship between Experience with Python and Expected Salary')
plt.show()








# # 12 Which event tend to attract more students from specific fields of study

# In[44]:


df.groupby("Events").count()


# In[126]:


print("Internship Program(IP) Success Conclave =\n657")


# # 13.Do students in leadership positions during their college years tend to have higher GPAs or better expected salary?

# In[46]:


import pandas as pd


# Define a filter for students with leadership experience
leadership_filter = df['Leadership- skills'] == 'Yes'

# Separate the data into students with and without leadership experience
students_with_leadership = df[leadership_filter]
students_without_leadership = df[leadership_filter]

# Calculate average GPAs for students with and without leadership experience
avg_gpa_with_leadership = students_with_leadership['GPA'].mean()
avg_gpa_without_leadership = students_without_leadership['GPA'].mean()

# Calculate average expected salaries for students with and without leadership experience
avg_salary_with_leadership = students_with_leadership['Expected salary (Lac)'].mean()
avg_salary_without_leadership = students_without_leadership['Expected salary (Lac)'].mean()

print(f"Average GPA for students with leadership experience: {avg_gpa_with_leadership:.2f}")
print(f"Average GPA for students without leadership experience: {avg_gpa_without_leadership:.2f}")

print(f"Average Expected Salary for students with leadership experience: {avg_salary_with_leadership:.2f}")
print(f"Average Expected Salary for students without leadership experience: {avg_salary_without_leadership:.2f}")


# # 14.How many students are graduating by the end of 2024?

# In[47]:


df.groupby("Year of Graduation").agg({"Year of Graduation":"count"})


# # 15 .Which promotion channel brings in more student participations for the event?

# In[48]:


df["How did you come to know about this event?"].value_counts()


# In[54]:


df["How did you come to know about this event?"].str.contains("Whatsapp").value_counts()


# In[55]:


df["How did you come to know about this event?"].str.contains("Email").value_counts()


# In[1]:


print("promotion channel brings in more student? \n Whatsapp = 517/1075")


# In[46]:


df


# In[1]:


# 


# # 16.Find the total number of students who attended the events related to Data Science? (From all Data

# In[127]:


t=df.groupby(df["Events"]=="IS DATA SCIENCE FOR YOU?").value_counts().sum()
t


# In[128]:


f=df["Events"]=="IS DATA SCIENCE FOR YOU?"


# In[129]:


f=f.value_counts()


# In[130]:


print(f"total number of students who attended the events related to Data Science? \n {t}" )


# # 18. how many student know about the event from their college? top 5 college ?

# In[55]:


d=df["how did you come to know about this event"].agg({"College Name":"count",})


# In[56]:


print(f"total {d} whoes student known the event from there college ")


# In[34]:


df['how did you come to know about this event'].str.contains("College").count()


# In[11]:


df.groupby(df["how did you come to know about this event"]=="college name").value_counts().head(5)


# In[58]:


print(89,"know about this event from college\n")
print('''top  collleges are =\n\n1.society's college of bca, rls institute, belagavi  =haijipur
       \n 2. ernment polytechnic gandhinagar    =rajkot
       \n 3.  son college  =ajmer
       \n 4.  son college  =hyderbad
       \n 5   Xavier's College  =aurangabad''')


# In[ ]:









