
# coding: utf-8

# # Project Introduction to Big Data
# 
# Xuandong ZHAO 20170588
# 
# Duo XU 20170598
# ## Part 1
# ### Loading CSV FILES

# In[87]:


import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import urllib.request
get_ipython().magic('matplotlib inline')
url ='https://data.enedis.fr/explore/dataset/consommation-electrique-par-secteur-dactivite-commune/download/?format=csv&timezone=Europe/Berlin&use_labels_for_header=true'
response = urllib.request.urlopen(url)

df = pd.read_csv( response, delimiter = ";" )
print(df.shape)
df.head(20)


# ### Showing colums

# In[6]:


df.columns


# ### Electric consomations' infos, department level  

# In[7]:


annee_depart_conso = DataFrame(df,columns=['Année','Nom département', 'Code département', 'Nombre d\'habitants',
                                              'Nb sites Résidentiel', 'Conso totale Résidentiel (MWh)',
       'Conso moyenne Résidentiel (MWh)', 'Nb sites Professionnel',
       'Conso totale Professionnel (MWh)', 'Conso moyenne Professionnel (MWh)',
       'Nb sites Agriculture', 'Conso totale Agriculture (MWh)',
       'Nb sites Industrie', 'Conso totale Industrie (MWh)',
       'Nb sites Tertiaire', 'Conso totale Tertiaire (MWh)',
       'Nb sites Secteur non affecté',
       'Conso totale Secteur non affecté (MWh)'])
annee_depart_conso.head(10)


# #### Departments with the less industrail consomation  
# From 2011-2016, the average number of departments with less industrial electric consomation

# In[13]:


df001 = annee_depart_conso.groupby(['Année','Nom département']).sum()[['Conso totale Industrie (MWh)']]
df002 = df001.groupby('Nom département').mean().sort_values('Conso totale Industrie (MWh)').head(20)
df002


# In[36]:


plt.figure(figsize=(35, 20))  

plt.xlabel('Dept') # 给 x 轴添加标签
plt.ylabel('ConsoTotal') # 给 y 轴添加标签
plt.bar(df002.index.get_values(),df002['Conso totale Industrie (MWh)'])
plt.show()


# #### Departments with the less Résidentiel consomation  
# From 2011-2016, the average number of departments with less Résidentiel electric consomation

# In[16]:


df003 = annee_depart_conso.groupby(['Année','Nom département']).sum()[['Conso totale Résidentiel (MWh)']]
df004 = df003.groupby('Nom département').mean().sort_values('Conso totale Résidentiel (MWh)').head(20)
df004


# In[41]:


plt.figure(figsize=(35, 20))  

plt.xlabel('Dept') # 给 x 轴添加标签
plt.ylabel('ConsoTotal') # 给 y 轴添加标签
plt.bar(df004.index.get_values(),df004['Conso totale Résidentiel (MWh)'])
plt.show()


# #### Departments with the less Professionnel consomation  
# From 2011-2016, the average number of departments with less Professionnel electric consomation

# In[18]:


df005 = annee_depart_conso.groupby(['Année','Nom département']).sum()[['Conso totale Professionnel (MWh)']]
df006 = df005.groupby('Nom département').mean().sort_values('Conso totale Professionnel (MWh)').head(20)
df006


# In[42]:


plt.figure(figsize=(35, 20))  

plt.xlabel('Dept') # 给 x 轴添加标签
plt.ylabel('ConsoTotal') # 给 y 轴添加标签
plt.bar(df006.index.get_values(),df006['Conso totale Professionnel (MWh)'])
plt.show()


# #### Departments with the less Agriculture consomation  
# From 2011-2016, the average number of departments with less Agriculture electric consomation

# In[20]:


df007 = annee_depart_conso.groupby(['Année','Nom département']).sum()[['Conso totale Agriculture (MWh)']]
df008 = df007.groupby('Nom département').mean().sort_values('Conso totale Agriculture (MWh)').head(20)
df008


# In[43]:


plt.figure(figsize=(35, 20))  

plt.xlabel('Dept') # 给 x 轴添加标签
plt.ylabel('ConsoTotal') # 给 y 轴添加标签
plt.bar(df008.index.get_values(),df008['Conso totale Agriculture (MWh)'])
plt.show()


# #### Departments with the less Tertiaire consomation  
# From 2011-2016, the average number of departments with less Tertiaire electric consomation

# In[60]:


df009 = annee_depart_conso.groupby(['Année','Nom département']).sum()[['Conso totale Tertiaire (MWh)']]
df010 = df009.groupby('Nom département').mean().sort_values('Conso totale Tertiaire (MWh)').head(20)
df010


# In[47]:


plt.figure(figsize=(35, 20))  

plt.xlabel('Dept') # 给 x 轴添加标签
plt.ylabel('ConsoTotal') # 给 y 轴添加标签
plt.bar(df010.index.get_values(),df010['Conso totale Tertiaire (MWh)'])
plt.show()


# #### Departments with the less Secteur non affecté consomation  
# From 2011-2016, the average number of departments with less Secteur non affecté electric consomation

# In[61]:


df011 = annee_depart_conso.groupby(['Année','Nom département']).sum()[['Conso totale Secteur non affecté (MWh)']]
df012 = df011.groupby('Nom département').mean().sort_values('Conso totale Secteur non affecté (MWh)').head(20)
df012


# In[65]:


plt.figure(figsize=(35, 20))  

plt.xlabel('Dept') # 给 x 轴添加标签
plt.ylabel('ConsoTotal') # 给 y 轴添加标签
plt.bar(df012.index.get_values(),df012['Conso totale Secteur non affecté (MWh)'])
plt.show()


# #### 2011 Electricity analysis

# In[38]:


SecteurTotal_2011=df[df['Année']==2011]['Conso totale Secteur non affecté (MWh)'].sum()
ProfessionnelTotal_2011=df[df['Année']==2011]['Conso totale Professionnel (MWh)'].sum()
TertiaireTotal_2011=df[df['Année']==2011]['Conso totale Tertiaire (MWh)'].sum()
AgricultureTotal_2011=df[df['Année']==2011]['Conso totale Agriculture (MWh)'].sum()
IndustrieTotal_2011=df[df['Année']==2011]['Conso totale Industrie (MWh)'].sum()
RésidentielTotal_2011=df[df['Année']==2011]['Conso totale Résidentiel (MWh)'].sum()
Total_2011=SecteurTotal_2011+TertiaireTotal_2011+AgricultureTotal_2011+IndustrieTotal_2011+ProfessionnelTotal_2011+RésidentielTotal_2011
Total_2011


# In[66]:


labels = 'Conso totale Tertiaire (MWh)', 'Conso totale Agriculture (MWh)', 'Conso totale Professionnel (MWh)', 'Conso totale Résidentiel (MWh)' ,'Conso totale Industrie (MWh)','Conso totale Secteur non affecté (MWh)' # 定义标签  
sizes = [TertiaireTotal_2011/Total_2011, AgricultureTotal_2011/Total_2011, ProfessionnelTotal_2011/Total_2011,RésidentielTotal_2011/Total_2011,IndustrieTotal_2011/Total_2011,SecteurTotal_2011/Total_2011]  # 每一块的比例  
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral','red','blue']  # 每一块的颜色  
explode = (0, 0.1, 0, 0,0,0) #突出显示  
#labeldistance，文本的位置离远点有多远，1.1指1.1倍半径的位置  
#autopct，圆里面的文本格式，%3.1f%%表示小数有三位，整数有一位的浮点数  
#shadow，饼是否有阴影  
#startangle，起始角度，0，表示从0开始逆时针转，为第一块。一般选择从90度开始比较好看  
#pctdistance，百分比的text离圆心的距离  
#patches, l_texts, p_texts，为了得到饼图的返回值，p_texts饼图内部文本的，l_texts饼图外label的文本  
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
plt.title('2011 Electricity analysis')
plt.axis('equal')  
plt.savefig("bingtu.png")  
plt.show() 


# #### 2012 Electricity analysis

# In[39]:


SecteurTotal_2012=df[df['Année']==2012]['Conso totale Secteur non affecté (MWh)'].sum()
ProfessionnelTotal_2012=df[df['Année']==2012]['Conso totale Professionnel (MWh)'].sum()
TertiaireTotal_2012=df[df['Année']==2012]['Conso totale Tertiaire (MWh)'].sum()
AgricultureTotal_2012=df[df['Année']==2012]['Conso totale Agriculture (MWh)'].sum()
IndustrieTotal_2012=df[df['Année']==2012]['Conso totale Industrie (MWh)'].sum()
RésidentielTotal_2012=df[df['Année']==2012]['Conso totale Résidentiel (MWh)'].sum()
Total_2012=SecteurTotal_2012+TertiaireTotal_2012+AgricultureTotal_2012+IndustrieTotal_2012+ProfessionnelTotal_2012+RésidentielTotal_2012
Total_2012


# In[53]:


labels = 'Conso totale Tertiaire (MWh)', 'Conso totale Agriculture (MWh)', 'Conso totale Professionnel (MWh)', 'Conso totale Résidentiel (MWh)' ,'Conso totale Industrie (MWh)','Conso totale Secteur non affecté (MWh)' # 定义标签  
sizes = [TertiaireTotal_2012/Total_2012, AgricultureTotal_2012/Total_2012, ProfessionnelTotal_2012/Total_2012,RésidentielTotal_2012/Total_2012,IndustrieTotal_2012/Total_2012,SecteurTotal_2012/Total_2012]  # 每一块的比例  
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral','red','blue']  # 每一块的颜色  
explode = (0, 0.1, 0, 0,0,0) #突出显示  
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
plt.title('2012 Electricity analysis')
plt.axis('equal')  
plt.savefig("bingtu.png")  
plt.show() 


# #### 2013 Electricity analysis

# In[41]:


SecteurTotal_2013=df[df['Année']==2013]['Conso totale Secteur non affecté (MWh)'].sum()
ProfessionnelTotal_2013=df[df['Année']==2013]['Conso totale Professionnel (MWh)'].sum()
TertiaireTotal_2013=df[df['Année']==2013]['Conso totale Tertiaire (MWh)'].sum()
AgricultureTotal_2013=df[df['Année']==2013]['Conso totale Agriculture (MWh)'].sum()
IndustrieTotal_2013=df[df['Année']==2013]['Conso totale Industrie (MWh)'].sum()
RésidentielTotal_2013=df[df['Année']==2013]['Conso totale Résidentiel (MWh)'].sum()
Total_2013=SecteurTotal_2013+TertiaireTotal_2013+AgricultureTotal_2013+IndustrieTotal_2013+ProfessionnelTotal_2013+RésidentielTotal_2013
Total_2013


# In[52]:


labels = 'Conso totale Tertiaire (MWh)', 'Conso totale Agriculture (MWh)', 'Conso totale Professionnel (MWh)', 'Conso totale Résidentiel (MWh)' ,'Conso totale Industrie (MWh)','Conso totale Secteur non affecté (MWh)' # 定义标签  
sizes = [TertiaireTotal_2013/Total_2013, AgricultureTotal_2013/Total_2013, ProfessionnelTotal_2013/Total_2013,RésidentielTotal_2013/Total_2013,IndustrieTotal_2013/Total_2013,SecteurTotal_2013/Total_2013]  # 每一块的比例  
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral','red','blue']  # 每一块的颜色  
explode = (0, 0.1, 0, 0,0,0) #突出显示  
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
plt.title('2013 Electricity analysis')
plt.axis('equal')  
plt.savefig("bingtu.png")  
plt.show() 


# #### 2014 Electricity analysis

# In[45]:


SecteurTotal_2014=df[df['Année']==2014]['Conso totale Secteur non affecté (MWh)'].sum()
ProfessionnelTotal_2014=df[df['Année']==2014]['Conso totale Professionnel (MWh)'].sum()
TertiaireTotal_2014=df[df['Année']==2014]['Conso totale Tertiaire (MWh)'].sum()
AgricultureTotal_2014=df[df['Année']==2014]['Conso totale Agriculture (MWh)'].sum()
IndustrieTotal_2014=df[df['Année']==2014]['Conso totale Industrie (MWh)'].sum()
RésidentielTotal_2014=df[df['Année']==2014]['Conso totale Résidentiel (MWh)'].sum()
Total_2014=SecteurTotal_2014+TertiaireTotal_2014+AgricultureTotal_2014+IndustrieTotal_2014+ProfessionnelTotal_2014+RésidentielTotal_2014
Total_2014


# In[46]:


labels = 'Conso totale Tertiaire (MWh)', 'Conso totale Agriculture (MWh)', 'Conso totale Professionnel (MWh)', 'Conso totale Résidentiel (MWh)' ,'Conso totale Industrie (MWh)','Conso totale Secteur non affecté (MWh)' # 定义标签  
sizes = [TertiaireTotal_2014/Total_2014, AgricultureTotal_2014/Total_2014, ProfessionnelTotal_2014/Total_2014,RésidentielTotal_2014/Total_2014,IndustrieTotal_2014/Total_2014,SecteurTotal_2014/Total_2014]  # 每一块的比例  
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral','red','blue']  # 每一块的颜色  
explode = (0, 0.1, 0, 0,0,0) #突出显示  
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
plt.title('2014 Electricity analysis')
plt.axis('equal')  
plt.savefig("bingtu.png")  
plt.show()


# #### 2015 Electricity analysis

# In[47]:


SecteurTotal_2015=df[df['Année']==2015]['Conso totale Secteur non affecté (MWh)'].sum()
ProfessionnelTotal_2015=df[df['Année']==2015]['Conso totale Professionnel (MWh)'].sum()
TertiaireTotal_2015=df[df['Année']==2015]['Conso totale Tertiaire (MWh)'].sum()
AgricultureTotal_2015=df[df['Année']==2015]['Conso totale Agriculture (MWh)'].sum()
IndustrieTotal_2015=df[df['Année']==2015]['Conso totale Industrie (MWh)'].sum()
RésidentielTotal_2015=df[df['Année']==2015]['Conso totale Résidentiel (MWh)'].sum()
Total_2015=SecteurTotal_2015+TertiaireTotal_2015+AgricultureTotal_2015+IndustrieTotal_2015+ProfessionnelTotal_2015+RésidentielTotal_2015
Total_2015


# In[51]:


labels = 'Conso totale Tertiaire (MWh)', 'Conso totale Agriculture (MWh)', 'Conso totale Professionnel (MWh)', 'Conso totale Résidentiel (MWh)' ,'Conso totale Industrie (MWh)','Conso totale Secteur non affecté (MWh)' # 定义标签  
sizes = [TertiaireTotal_2015/Total_2015, AgricultureTotal_2015/Total_2015, ProfessionnelTotal_2015/Total_2015,RésidentielTotal_2015/Total_2015,IndustrieTotal_2015/Total_2015,SecteurTotal_2015/Total_2015]  # 每一块的比例  
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral','red','blue']  # 每一块的颜色  
explode = (0, 0.1, 0, 0,0,0) #突出显示  
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
plt.title('2015 Electricity analysis')
plt.axis('equal')  
plt.savefig("bingtu.png")  
plt.show()


# #### 2016 Electricity analysis

# In[49]:


SecteurTotal_2016=df[df['Année']==2016]['Conso totale Secteur non affecté (MWh)'].sum()
ProfessionnelTotal_2016=df[df['Année']==2016]['Conso totale Professionnel (MWh)'].sum()
TertiaireTotal_2016=df[df['Année']==2016]['Conso totale Tertiaire (MWh)'].sum()
AgricultureTotal_2016=df[df['Année']==2016]['Conso totale Agriculture (MWh)'].sum()
IndustrieTotal_2016=df[df['Année']==2016]['Conso totale Industrie (MWh)'].sum()
RésidentielTotal_2016=df[df['Année']==2016]['Conso totale Résidentiel (MWh)'].sum()
Total_2016=SecteurTotal_2016+TertiaireTotal_2016+AgricultureTotal_2016+IndustrieTotal_2016+ProfessionnelTotal_2016+RésidentielTotal_2016
Total_2016


# In[50]:


labels = 'Conso totale Tertiaire (MWh)', 'Conso totale Agriculture (MWh)', 'Conso totale Professionnel (MWh)', 'Conso totale Résidentiel (MWh)' ,'Conso totale Industrie (MWh)','Conso totale Secteur non affecté (MWh)' # 定义标签  
sizes = [TertiaireTotal_2016/Total_2016, AgricultureTotal_2016/Total_2016, ProfessionnelTotal_2016/Total_2016,RésidentielTotal_2016/Total_2016,IndustrieTotal_2016/Total_2016,SecteurTotal_2016/Total_2016]  # 每一块的比例  
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral','red','blue']  # 每一块的颜色  
explode = (0, 0.1, 0, 0,0,0) #突出显示  
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
plt.title('2016 Electricity analysis')
plt.axis('equal')  
plt.savefig("bingtu.png")  
plt.show()


# ## Part 2
# ### Analysis of living Numbers

# In[90]:


annee_Nb = DataFrame(df,columns=['Année','Nom région','Nb sites Résidentiel',
                                            'Nb sites Professionnel','Nb sites Agriculture','Nb sites Industrie',
                                            'Nb sites Tertiaire','Nb sites Secteur non affecté'])
annee_Nb.head(10)


# In[95]:


Nb1 = annee_Nb[annee_Nb['Nom région'].isin(['Auvergne-Rhône-Alpes'])]
Nb1 = Nb1.groupby(Nb1['Année']).sum()
Nb1.plot(marker='*')
for x,y in zip(Nb1.index, Nb1['Nb sites Résidentiel']):
    plt.text(x, y+10, '%.0f' % y, ha = 'center', va = 'bottom')
plt.grid()
plt.title('Number of sites in Auvergne-Rhône-Alpes from 2011 to 2016')  
plt.xlabel('year')  
plt.ylabel('number')
plt.show()


# In[97]:


Nb2 = annee_Nb[annee_Nb['Nom région'].isin(['Centre-Val de Loire'])]
Nb2 = Nb2.groupby(Nb2['Année']).sum()
Nb2.plot(marker='o')
for x,y in zip(Nb2.index, Nb2['Nb sites Résidentiel']):
    plt.text(x, y+10, '%.0f' % y, ha = 'center', va = 'bottom')
plt.grid()
plt.title('Number of sites in Centre-Val de Loire from 2011 to 2016')
plt.xlabel('year')  
plt.ylabel('number')
plt.show()


# In[98]:


Nb3 = annee_Nb[annee_Nb['Nom région'].isin(['Bourgogne-Franche-Comté'])]
Nb3 = Nb3.groupby(Nb3['Année']).sum()
Nb3.plot(marker='o')
for x,y in zip(Nb3.index, Nb3['Nb sites Résidentiel']):
    plt.text(x, y+10, '%.0f' % y, ha = 'center', va = 'bottom')
plt.grid()
plt.title('Number of sites in Bourgogne-Franche-Comté from 2011 to 2016')
plt.xlabel('year')  
plt.ylabel('number')
plt.show()


# In[99]:


Nb4 = annee_Nb[annee_Nb['Nom région'].isin(['Pays de la Loire'])]
Nb4 = Nb4.groupby(Nb4['Année']).sum()
Nb4.plot(marker='o')
for x,y in zip(Nb4.index, Nb4['Nb sites Résidentiel']):
    plt.text(x, y+10, '%.0f' % y, ha = 'center', va = 'bottom')
plt.grid()
plt.title('Number of sites in Pays de la Loire from 2011 to 2016')
plt.xlabel('year')  
plt.ylabel('number')
plt.show()


# In[105]:


Nb5 = annee_Nb[annee_Nb['Nom région'].isin(['Île-de-France'])]
Nb5  = Nb5 .groupby(Nb5 ['Année']).sum()
Nb5 .plot(marker='*')
for x,y in zip(Nb5 .index, Nb5 ['Nb sites Résidentiel']):
    plt.text(x, y+10, '%.0f' % y, ha = 'center', va = 'bottom')
plt.grid()
plt.style.use('bmh')
plt.title('Number of sites in Île-de-France from 2011 to 2016')
plt.xlabel('year')  
plt.ylabel('number')
plt.show()


# ## Part 3
# ### Analysis of living Numbers

# In[8]:


annee_habitants = DataFrame(df,columns=['Année','Nom département', 'Code département', 'Nombre d\'habitants',
       'Taux de logements collectifs', 'Taux de résidences principales','Superficie des logements < 30 m2',
       'Superficie des logements 30 à 40 m2',
       'Superficie des logements 40 à 60 m2',
       'Superficie des logements 60 à 80 m2',
       'Superficie des logements 80 à 100 m2',
       'Superficie des logements > 100 m2',
       'Résidences principales avant 1919',
       'Résidences principales de 1919 à 1945',
       'Résidences principales de 1946 à 1970',
       'Résidences principales de 1971 à 1990',
       'Résidences principales de 1991 à 2005',
       'Résidences principales de 2006 à 2010',
       'Résidences principales après 2011', 'Taux de chauffage électrique'])
annee_habitants.head(10)


# #### Departments with the less Taux de résidences principales
# From 2011-2016, the average number of departments with less Taux de résidences principales

# In[32]:


df015 = annee_habitants.groupby(['Année','Nom département']).sum()[['Taux de résidences principales']]
df016 = df015.groupby('Nom département').mean().sort_values('Taux de résidences principales').head(20)
df016


# In[40]:


plt.figure(figsize=(35, 20))  

plt.xlabel('Dept') # 给 x 轴添加标签
plt.ylabel('Nom département') # 给 y 轴添加标签
plt.bar(df016.index.get_values(),df016['Taux de résidences principales'])
plt.show()


# #### Departments with the less Taux de logements collectifs
# From 2011-2016, the average number of departments with less Taux de logements collectifs

# In[106]:


df017 = annee_habitants.groupby(['Année','Nom département']).sum()[['Taux de logements collectifs']]
df018 = df017.groupby('Nom département').mean().sort_values('Taux de logements collectifs').head(20)
df018


# In[109]:


plt.figure(figsize=(35, 20))  

plt.xlabel('Dept') # 给 x 轴添加标签
plt.ylabel('Nom département') # 给 y 轴添加标签
plt.bar(df018.index.get_values(),df018['Taux de logements collectifs'])
plt.show()

