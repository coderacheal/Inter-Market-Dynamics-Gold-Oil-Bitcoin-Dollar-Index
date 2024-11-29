import streamlit as st

feature_descriptions = """

1. **Age**: Age of employee
2. **Attrition**: Employee attrition status
3. **Department**: Department of work
4. **DistanceFromHome**: what is their distance from hime
5. **Education**: 1-Below College; 2- College; 3-Bachelor; 4-Master; 5-Doctor;
6. **EducationField**: The field they studies in in the University
7. **EnvironmentSatisfaction**: 1-Low; 2-Medium; 3-High; 4-Very High;
8. **JobSatisfaction**: 1-Low; 2-Medium; 3-High; 4-Very High;
9. **MaritalStatus**: Whether they are married, single or divorced
10. **MonthlyIncome**: How much an employee makes a month
11. **NumCompaniesWorked**: Number of companies worked prior to IBM
12. **WorkLifeBalance**: 1-Bad; 2-Good; 3-Better; 4-Best;
13. **YearsAtCompany**: Current years of service in IBM

"""

about = """
### About
This project investigates the inter-market dynamics between gold, crude oil, and Bitcoin, examining their collective influence on the U.S. Dollar Index (DXY). Using daily price data spanning the past decade (2014–2024), the study seeks to uncover critical patterns and dependencies among these assets and to construct a predictive model for the dollar index. 

### Key Features
- **Predict movement in the in the dollar price index**
- **Calculate the weight of every commodity in a portfolio**
- **Save portfolio Information**

### User Benefits
- **Data-driven Decisions:** Make informed decisions backed by data analytics.
- **Easy Machine Learning:** Utilize powerful machine learning algorithms effortlessly.

"""

column_2 = """
### Machine Learning Integration
- **Model Selection:** Choose between two advanced models for accurate predictions.
- **Seamless Integration:** Integrate predictions into your workflow with a user-friendly interface.
- **Probability Estimates:** Gain insights into the likelihood of predicted outcomes.

### Need Help?
For collaborations contact me at [hello@rachealappiahkubi.com](mailto:hello@rachealappiahkubi.com).
"""


#Build command
# mkdir .streamlit; cp /etc/secrets/secrets.toml ./.streamlit/; pip install --upgrade pip && pip install -r requirements.txt