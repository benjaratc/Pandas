#!/usr/bin/env python
# coding: utf-8

# In[223]:


import numpy as np
import pandas as pd


# 1.โหลด csv เข้าไปใน Python Pandas

# In[292]:


df = pd.read_csv('../Desktop/DataCamp/train.csv')


# In[293]:


df


# 2. เขียนโค้ดแสดง หัว10แถว ท้าย10แถว และสุ่ม10แถว

# In[294]:


df.head(10)


# In[295]:


df.tail(10)


# In[296]:


df.sample(10)


# 3. ลบ row ที่มี Embarked ว่าง

# In[297]:


df.dropna(axis=0,subset = ['Embarked'])


# 4. เติม age ด้วยค่าเฉลี่ย

# In[298]:


age = df['Age'].mean()
age


# In[299]:


df1 = pd.read_csv('../Desktop/DataCamp/train.csv')
df1['Age'].fillna(value = age, inplace = True)
df1


# 5. เติม age ด้วย 0

# In[260]:


df2 = pd.read_csv('../Desktop/DataCamp/train.csv')
df2['Age'].fillna(value = 0, inplace = True)
df2


# 6. ลบ row ที่ age เป็นค่าว่าง

# In[265]:


df.dropna(axis=0, subset=['Age'])


# 7. หาจำนวนผู้หญิงต่อผู้ชายที่อยู่บนเรือ

# In[100]:


women = (df['Sex'] == 'male').sum()
women 


# In[101]:


men = (df['Sex'] == 'female').sum()
men


# 8. หาจำนวนผู้หญิงและผู้ชายที่รอดชีวิต

# In[127]:


survival_women = ((df['Survived'] == 1) & (df['Sex'] == 'female')).sum()
survival_women


# In[129]:


survival_men = ((df['Survived'] == 1) & (df['Sex'] == 'male')).sum()
survival_men


# 9. หา % การรอดชีวิตของผู้หญิงและผู้ชาย

# In[134]:


survival_all = (df['Survived'] == 1).sum()
survival_all


# In[135]:


survival_women_percent = survival_women/survival_all*100
survival_women_percent


# In[136]:


survival_men_percent = survival_men/survival_all*100
survival_men_percent


# 10. แปลงคอลัมน์ female = 0 และ male = 1 

# In[276]:


df['Sex'].replace('female',0) & df['Sex'].replace('male',1)
df


# 11. หาคนที่อายุมากที่สุดพร้อมบอกชื่อ อายุ และลงท่าที่ไหน

# In[475]:


df3 = pd.read_csv('../Desktop/DataCamp/train.csv')
df3['Age'].fillna(value = 0, inplace = True)
oldest = df3['Age'].max()
print(oldest)
print(df[['Name','Age','Embarked']][df['Age']== oldest])


# 12. หาคนที่อายุน้อยที่สุดพร้อมบอกชื่อ อายุ และลงท่าที่ไหน

# In[476]:


df5 = pd.read_csv('../Desktop/DataCamp/train.csv')
youngest = df5['Age'].min()
print(youngest)
print(df[['Name','Age','Embarked']][df['Age']== youngest])


# 13. หาคนที่จ่ายค่าโดยสารแพงที่สุดพร้อมบอกชื่อ อายุ และรอดชีวิตไหม

# In[477]:


df7 = pd.read_csv('../Desktop/DataCamp/train.csv')
max_fare = df7['Fare'].max()
print(max_fare)
print(df7[['Name','Age','Survived']][df['Fare']== max_fare])


# 14. หาคนที่จ่ายค่าโดยสารถูกที่สุดพร้อมบอกชื่อ อายุ และรอดชีวิตไหม

# In[478]:


df8 = pd.read_csv('../Desktop/DataCamp/train.csv')
min_fare = df8['Fare'].min()
print(min_fare)
print(df8[['Name','Age','Survived']][df8['Fare']== min_fare])


# 15. สรุปว่ามีคนนั่งตั๋ว 1 2 3 กี่คน

# In[163]:


(df['Pclass'] == 1).sum()


# In[164]:


(df['Pclass'] == 2).sum()


# In[165]:


(df['Pclass'] == 3).sum()


# 16. หาค่าเฉลี่ยของตั๋วโดยสารแบบที่นั่งชั้น 1 2 3

# In[343]:


df['Fare'][df['Pclass'] == 1].mean()


# In[344]:


df['Fare'][df['Pclass'] == 2].mean()


# In[345]:


df['Fare'][df['Pclass'] == 3].mean()


# 17. มีผู้โดยสารกี่คนที่อายุเกิน 50 แล้วรอดชีวิต

# In[176]:


survival_men_age50above = ((df['Survived'] == 1) & (df['Age'] > 50)).sum()
survival_men_age50above


# 18. แสดงผลข้อมูลทั้งหมดของที่นั่งชั้น 1 2 3 (describe)

# In[184]:


(df['Pclass'] == 1).describe()


# In[185]:


(df['Pclass'] == 2).describe()


# In[186]:


(df['Pclass'] == 3).describe()


# In[188]:


df['Pclass'].describe()


# 19. แสดงผลตั๋วที่แพงที่สุดของที่นั่งแต่ละชั้น

# In[380]:


df['Fare'][df['Pclass'] == 1].max()


# 20. แสดงเป็นกลุ่มช่วงอายุ 0-10, 20-30 …. (เพิ่มทีละ10) และหาว่าแต่ละกลุ่มมีอัตราการรอดชีวิตเท่าไหร่ 

# In[450]:


df['Survived'][df['Age'].between(0, 10, inclusive = True)].mean()


# In[451]:


df['Survived'][df['Age'].between(11, 20, inclusive = True)].mean()


# In[452]:


df['Survived'][df['Age'].between(21, 30, inclusive = True)].mean()


# In[453]:


df['Survived'][df['Age'].between(31, 40, inclusive = True)].mean()


# In[454]:


df['Survived'][df['Age'].between(41, 50, inclusive = True)].mean()


# In[455]:


df['Survived'][df['Age'].between(51, 60, inclusive = True)].mean()


# In[456]:


df['Survived'][df['Age'].between(61, 70, inclusive = True)].mean()


# In[457]:


df['Survived'][df['Age'].between(71, 80, inclusive = True)].mean()


# In[458]:


df['Survived'][df['Age'].between(81, 90, inclusive = True)].mean()


# 21. เรียงลำดับตามราคามากไปน้อย และน้อยไปมาก

# In[384]:


df10 = pd.read_csv('../Desktop/DataCamp/train.csv')
df11 = df10.sort_values('Fare')[::-1]
df11.head()


# 22. (Optional) หานามสกุลที่ซ้ำกัน และแต่ละนามสกุลที่ซ้ำกันซ้ำกันกี่คน  (not sure)

# In[416]:


df14 = pd.read_csv('../Desktop/DataCamp/train.csv')
df14[['Last','First']] = df14.Name.str.split(",",expand=True)
df14.head(5)


# In[540]:


df15 = df14[df14['Last'].duplicated()]
df15.head()


# In[541]:


dups = df15.pivot_table(index=['Last'],aggfunc='size')
print(dups)


# 23. (Optional) แสดงผลนามสกุลที่ไม่มีการซ้ำกันเลย และนับว่ามีกี่นามสกุล

# In[522]:


df16 = df14[df14['Last'].duplicated() == False]
df16.head()


# In[542]:


dups = df16.pivot_table(index=['Last'],aggfunc='size')
print(dups)

