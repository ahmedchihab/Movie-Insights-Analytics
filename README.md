# **Movie Data Analysis: Cleaning, Exploration & Insights**  

## **Introduction**  
This project analyzes a CSV dataset containing movie information, including ratings, budgets, revenues, and other key metrics. The goal is to clean, organize, and explore this data to extract meaningful insights about film industry trends.  

## **Methodology**  

### **1. Data Cleaning & Preparation**  
- Removed duplicates and missing values  
- Fixed column formats (dates, numeric values)  
- Standardized categories and normalized data  
- Verified data consistency  

### **2. Statistical Analysis & Outlier Detection**  
- Calculated descriptive statistics (mean, median, standard deviation)
- <img width="931" height="526" alt="image" src="https://github.com/user-attachments/assets/e68c771f-a80d-451a-aff0-0c491498b17c" />
  <img width="894" height="478" alt="image" src="https://github.com/user-attachments/assets/8d9cffb2-32b6-4d17-b58c-e36395f6cc39" />

- Identified outliers using the IQR method (1.5× interquartile range)
  <img width="1353" height="659" alt="image" src="https://github.com/user-attachments/assets/d206c17d-e6c8-4455-894c-d7001ba2edb8" />

IF( AND(movies[budget] < __upper , movies[budget] > 0) , "True" , "False") 
  

*(Space reserved for outlier visualization)*  

### **3. Correlation Analysis**  
- Calculated correlation coefficients between key variables
  <img width="868" height="520" alt="image" src="https://github.com/user-attachments/assets/c0a01c4c-5221-4611-aeb5-c5e14c2ca100" />
  
- Identified significant relationships

  <img width="774" height="535" alt="image" src="https://github.com/user-attachments/assets/af207031-1d7a-4745-aa13-b5c5ec1f84e2" />

   <img width="500" height="435" alt="image" src="https://github.com/user-attachments/assets/e4b42ee7-6396-492b-86fb-b6f2caba322b" />

- Visualized through correlation matrix
  
<img width="1026" height="560" alt="image" src="https://github.com/user-attachments/assets/8df018da-71f8-4d7a-a924-5528e9623168" />

<img width="509" height="419" alt="image" src="https://github.com/user-attachments/assets/bbe10c07-80e1-46c8-887b-2d51a1dfbf95" />

  

### **4. Key KPIs Calculation**  
- Movie profitability (ROI)  
- Performance by genre  
- Time trends of key metrics  
- Interactive visualizations of results  

<img width="904" height="516" alt="image" src="https://github.com/user-attachments/assets/0923749e-1897-4cc7-b71c-a43f4c83c664" />
  

## **Key Findings**  
The analysis revealed:  
- Factors most correlated with commercial success  
- Highest-performing movie genres  
- Budget impact on revenue  
- Notable industry trends  

## **Conclusion**  
This project highlights the importance of thorough data cleaning before analysis. The applied statistical methods provided reliable, actionable insights about the film industry. The visualizations created offer immediate understanding of cinematic trends.  

  👨‍🎓 About Me
I'm a student in Financial Engineering, currently learning Python and SQL.
This is my first public project using Excel and GitHub!

📌 Created by AHMED CHIHAB https://github.com/ahmedchihab
**Note**: All code and visualizations are reproducible with the provided dataset and scripts.
