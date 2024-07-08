# Customers Age and District Impact on the Mortgage Amount in Lithuania

### Project overview:

The main results of the project:
* Analysed and visualised customer's age group and district impact on the maximum amount of mortgage.

Data set obtained from [Registrų centras](https://www.registrucentras.lt/p/1561) with Creative Commons Attribution 4.0 
([CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.lt)) license. 

Data cleaning, missing data management, detecting and removing outliers were performed. 

Technologies used:
* Python
* Pandas
* Seaborn
* Matplotlib 

### Distribution of mortgages by age
In all districts, the majority of contractual mortgages for clients aged 18-55 years ranged from €50,000 (€100,000) 
to €500,000, 25% of such mortgages amounting to €1 million. The mortgages of clients aged over 55 were smaller -
the majority between €50,000 to €100,000, and only a small number of clients had larger mortgages.
Compulsory mortgage amounts are much lower - the majority up to €50,000.  A quarter of clients aged 
between 25 and 85 and only a few younger clients have a compulsory mortgage up to €100,000. 

![img.png](Images%2Fimg.png)

### Distribution of mortgages in different districts
In Vilnius, Klaipėda, Kaunas and Šiauliai districts, which include the municipalities of the 4 largest cities, 
contractual mortgages ranged from €50,000 (€100,000) to €500,000, and a quarter of mortgages reach €1 million. 
The situation is different in smaller districts (even in Panevėžys, which includes the 5th larger city) - majority 
of contractual mortgages ranged from  €50,000 to €100,000.
Compulsory mortgage amounts are much lower - the majority up to €50,000.  A quarter of compulsory mortgage reaches 
€100,000. 

![img_1.png](Images%2Fimg_1.png)

### Distribution of mortgages by age in different districts
In Vilnius district, there is no correlation between clients' age and mortgage amount  - no matter what age group
the client belongs to, mortgage amount is the same - the majority ranges from 50-100 K€ to 500 K€ and a quarter 
reaches €1 million.
Data from Klaipėda, Kaunas and Šiauliai districts shows diversified situation - based on age group, the mortgage 
amount can differ. The larger mortgage loans (the majority amounted to 500 K€) were granted to clients:
* aged between 18 and 55 in Kaunas district;  
* aged between 25 and 45 in Klaipėda district;
* aged between 25 and 45, also between 65-85 in Šiauliai district.
In general, 50-100 K€ mortgages were provided for the majority of clients from smaller districts, with just a few 
outliers for the oldest group of clients in Panevėžys (an increase to 500 K€), Utena and Telšiai districts 
(a decrease to 50 K€). In Alytus district, there is also a spike in the amount of mortgages for clients aged 35-45 
(up to 500 K€).

![img_2.png](Images%2Fimg_2.png)

### Mortgages trend
The number of mortgage granted is dynamic. However, it is not significant, especially for the last quarter - 2023Q3. 
![img_3.png](Images%2Fimg_3.png)
![img_4.png](Images%2Fimg_4.png)

### Conclusions
1. There is a correlation between client's age and max amount of mortgage, except 3 districts (Vilnius, Marijampolė and 
Tauragė).
2. Districts have an impact on the mortgages as well - the largest contractual mortgages were granted in 4 largest 
districts (Vilnius, Klaipėda, Kaunas and Šiauliai).
