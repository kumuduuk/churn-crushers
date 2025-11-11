# BankChurners - Hackathon project

Project bookmarks:

-   [README](https://github.com/kumuduuk/churn-crushers/blob/main/README.md)
-   [Project board](https://github.com/users/kumuduuk/projects/3)
-   [Raw Data](https://github.com/kumuduuk/churn-crushers/blob/main/data/raw_data/BankChurners.csv) | [Clean data](https://github.com/kumuduuk/churn-crushers/blob/main/data/cleaned_data/bankchurners.csv)
-   [Streamlit](https://churn-crusher-dashboard.streamlit.app/)
-   [Conclusion](#conclusion)

## Team Members:

| Name            |      Role       |                   Responsibility                   |
| :-------------- | :-------------: | :------------------------------------------------: |
| Kumudu Liyanage | Project Manager | Oversee the project and create streamlit dashboard |
| Ali Khurshid    | Data Architecht |                 Visualise the data                 |
| Steven Naylor   |  Data Analyst   |            Clean and tranform the data             |

## Contents:

-   [Project Overview](#project-overview)
-   [Dataset Content](#dataset-content)
-   [Business Requirements](#business-requirements)
-   [Hypothesis Testing and Validation](#hypothesis-testing-and-validation)
-   [Analysis Techniques Used](#analysis-techniques-used)
-   [Development Roadmap](#development-roadmap)
-   [Libraries & External Software Used](#libraries--external-software-used)
-   [Conclusion](#conclusion)
-   [Credits](#credits)
-   [Acknowledgements](#acknowledgements)

## Project overview

The project uses a dataset looking at existing and attrited customers from a bank. It contains over 10,000 records of customers who have used the banks services in the past or still do, using this we can identify trends and patterns within the dataset and will also look to make a predicitive model that the bank can use on future applicants to see whether they are likely to churn (leave) or not.

![project_header](images/readme_header.png)

## Dataset content

| Field                    | Description                                                |
| ------------------------ | ---------------------------------------------------------- |
| clientnum                | Unique customer identifier                                 |
| customer_status          | 'Existing' or 'Attrited'                                   |
| age                      | Age of the customer in years                               |
| gender                   | Customer’s gender                                          |
| dependencies             | Number of dependents                                       |
| education_level          | Highest education achieved                                 |
| marital_status           | Marital status                                             |
| income_category          | Annual income sorted into brackets                         |
| card_category            | Type of credit card                                        |
| months_on_book           | Total relationship length (in months)                      |
| total_relationship_count | Total number of products                                   |
| months_inactive_12_mon   | Inactive months in the last 12 months                      |
| contacts_count_12_mon    | Number of contacts with the bank in the last 12 months     |
| credit_limit             | Credit card limit                                          |
| total_revolving_bal      | Money owed going into the next month                       |
| avg_open_to_buy          | Credit available to spend                                  |
| total_trans_amt          | Total transaction amount (12 months)                       |
| total_trans_ct           | Total transaction count (12 months)                        |
| avg_utilization_ratio    | Average card utilization                                   |
| age_bracket              | age brackets to convert age into a categorical             |
| utilization_cat          | Credit score like rating (1.00 being high risk - 0.01 low) |

## Business requirements

The bank manager is perplexed as to why an increasing number of customers are leaving their credit card services. They are looking for someone to present the historical data in a way that can help them find out if there are any patterns in who is churning and why so they can proactively approach those customers who may leave and provide them with a better service in a bid to persuade them to stay.
We will also put together a predictive model that will allow the bank to vet new applicants and deem them to be likely to churn based on our findings throughout the project.

## Hypothesis testing and validation

## Project Board

![project_board](images/project_board.png)

As this was a group project all tasks within the project were assigned to users, some tasks were for the individual to complete and others allowed for a collaborative approach to be taken so were applied to multiple or all members of the group. We were assigned different roles in the group and took a lead area:
Data Analyst - Run the data through the ETL process
Data Architect - Visualise the data
Project Manager/Dashboard builder - Manage the project and build the dashboard to house the project findings.

The project baord allowed us to clearly plan out the three days with measurable targets to keep track of our progress.

### Day 1 — Data Understanding & Preparation

Import and Inspect the Dataset
Data Cleaning and Pre-processing
Exploratory Data Analysis (EDA)
Feature Engineering
Begin basic visualisation
Create wireframe of streamlit dashboard

### Day 2 — Analysis, Visualisation & Insights

Testing our dataset against a set of hypothesis and validation rules.
Data Visualisation (Matplotlib, Seaborn)
Descriptive Statistics & Correlation Analysis
Advanced plots to be done on Power BI
Discuss key insights, trends and patterns in the data
Build streamlit webpage and function test, ready for integrating of project components

### Day 3

Integrate all necessary components of project onto streamlit webpage.
Document all steps done throughout the project on the project board
Cross reference this with the README to ensure accuracy of project notes
Proof read documents
Check over project intended outcomes, have we achieved them

## Analysis techniques used

The ETL stage of this project allowed us to deploy a number of data analysis techniques to take our raw data set and turn it into a useable clean version ready to visualise and deploy on our streamlit dashboard.

-   Data cleaning: To maintain data integrity we identified all problem values within our dataset, these include missing values, duplicates, and some incorrect data entries such as a string value being found in the age category.
-   Data categorisation: By categorising data and grouping it we were able to spot whether there were any trends or issues within our data set, one notable example being when we sorted by gender and looked at value counts of income bracket we found that women earning over $60k were not represented in this dateset. Grouping the data also allowed us to see the distribution amongst categories prior to plotting them on a histogram.
-   Outlier detection: We looked into the statistical analysis of the dataset early on, using .describe() to check the values of our numerical columns, one key area were the values between 0% and the first quartile (25%) and the third quartile (75%) and 100%. This was an early indicator of whether we had outliers in our data. Double checked with the plotting of boxplots to highlight outliers within the dataset. We then made the decision as a group which values to keep and whihc to drop.
-   Column management - To create consistency across the board we put all of our column names into lowercase letters as there was a mix of upper and lower case characters within the same column set which made writing code frustrating.

## Ethical

All data has been included anonymously, nobody in this dataset can be identified from the values in this table. The only unique identifier is the bank client number but the name of the bank has not been given anywhere.

## Development Roadmap

This project was the first project we have worked on as a group which also involved us using a joint github repository for the first time. This involved working to group deadlines and not to your own individual timings. It also meant there had to be compromise within the group about which features of the project to include/exclude and how to present our findings.

_"The feedback I received from my first solo project was that I needed to be more concise with my markdown and code comments, markdown to explain the why each bit of code has been included and the code comment to describe what each bit of code is doing. That is something I have made a conscious effort to include in this project. Working collaboratively lends itself to having people to bounce ideas off but can also require a bit of compromise when deciding on the best course of action as a group. Overall it's been a beneficial experience, on a steep learning curve"_ - Steven Naylor

## Main Data Analysis Libraries

This has been a python based project, the libraries and additional software used on this project were:

-   Pandas
-   Numpy
-   Matplotlib
-   Seaborn
-   Scikit-learn
-   SciPy
-   Streamlit
-   PowerBI

# Conclusion

## Credits

Code Institute LMS
Masterclass and data coach session notes
Code Institute project template
Kaggle - source for the dataset

## Content

All images throughout the project that were not produced by this group are free to use.

## Acknowledgements

-   Code institute tutors, masterclass coach Spencer Barriball and data coach Mark Briscoe
-   Peers in September cohort for support
