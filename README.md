# Interactive Budget Tracker

## Group Members
- Laksh Trivedi (KU2407U420)
- Mehul Labana (KU2407U419)
- Namra Patel (KU2407U428)
- Pratham Solanki (KU2407U660)

## Object of the Interactive Budget Tracker Project
The objective of this project is to analyze and visualize budget data, specifically focusing on income, loans, and miscellaneous expenses over a specified year. The project aims to provide insights into financial trends and help users understand their budget distribution on a monthly basis.

## Tools and Libraries

- **Python:** The primary programming language used for developing the project.

- **Pandas:** A powerful data manipulation and analysis library for Python. It provides data structures like DataFrames, which are ideal for handling structured data, making it easy to read, write, and manipulate datasets.

- **Matplotlib:** A plotting library for Python that provides a flexible way to create static, animated, and interactive visualizations in Python. It is used in this project to visualize income and expenses.

- **CSV:** A module in Python's standard library used for reading and writing CSV (Comma-Separated Values) files. It is used in this project to store and retrieve budget data.

- **Git:** A version control system used to track changes in the project files. It allows for collaboration among team members and maintains a history of changes.

- **GitHub:** A web-based platform for version control and collaboration. It hosts the project repository, allowing team members to share code and track issues.

## Data Source(s)
The primary data source for this project is a CSV file named budget_data.csv. This file contains structured financial data that includes the following columns:

### Date: The date of the transaction, formatted as YYYY-MM-DD. This column is crucial for time-based analysis and allows for the extraction of year and month information.

### Type: A categorical variable that indicates the nature of the transaction. Possible values include:
- **Income:** Money received, such as salary, bonuses, or other earnings.
- **Expenses:** Money spent on various categories, such as bills, groceries, and entertainment.
- **Loans:** Any loans taken, which may include personal loans, student loans, or mortgages.
- **Miscellaneous:** Any other financial transactions that do not fit into the above categories.
- **Amount:** A numerical value representing the monetary amount associated with the transaction. This value can be positive (for income and loans) or negative (for expenses).

### Sample Data
Here is a sample of what the budget_data.csv file might look like:\
Date,Type,Amount\
2020-01-01,Income,4\
2020-01-15,Income,5\
2020-01-31,Expenses,1\
2020-01-31,Loans,1\
2020-01-31,Miscellaneous,1\
2020-02-01,Income,5\
2020-02-15,Income,6\
2020-02-28,Expenses,2\
2020-02-28,Loans,1\
2020-02-28,Miscellaneous,1\
2020-03-01,Income,5

## Execution Steps
To successfully run the budget data visualization project, follow these steps:

**Step 1:** Prerequisites\
Ensure you have Python installed on your machine. You can download it from the official Python website. It is recommended to use Python 3.6 or higher.

**Step 2:** Install Required Libraries\
You will need to install the necessary Python libraries to run the project. Open your terminal or command prompt and execute the following command:\
**pip install pandas plotly**

**Step 3:** Download or Create the Dataset
You need a CSV file named budget_data.csv containing your financial data. If you do not have this file, you can create one with the following sample structure:\

Date,Type,Amount\
2020-01-01,Income,4\
2020-01-15,Income,5\
2020-01-31,Expenses,1\
2020-01-31,Loans,1\
2020-01-31,Miscellaneous,1\
2020-02-01,Income,5\
2020-02-15,Income,6\
2020-02-28,Expenses,2\
2020-02-28,Loans,1\
2020-02-28,Miscellaneous,1\
2020-03-01,Income,5\
Save this file in the same directory as your Python script.

**Step 4:** Place the CSV File\
Ensure that the budget_data.csv file is located in the same directory as your Python script (e.g., budget_tracker.py). This allows the script to access the data without any path issues.

**Step 5:** Run the Script\
Navigate to the directory where your script is located using the terminal or command prompt. Then, execute the following command:
**python budget_visualization.py**

**Step 6:** Input Year\
Once the script is running, it will prompt you to enter a year for which you want to visualize the budget data. Type in the desired year (e.g., 2022) and press Enter.

**Step 7:** View the Visualization\
After processing the data, an interactive bar chart will be generated and displayed in your default web browser. You can hover over the bars to see detailed information about the amounts for each type of financial data (Income, Loans, Miscellaneous Expenses) for each month.

**Step 8:** Analyze the Results\
Take some time to analyze the chart. Look for trends in your income and expenses, and consider how you might adjust your budget based on the insights gained from the visualization.

## Summary of Results
- **Total Income:** Analyzed overall income for the year, identifying peak months.
- **Total Expenses:** Summarized expenses by category, highlighting major spending areas.
- **Net Savings:** Calculated net income (income minus expenses) to assess financial health.
- **Visual Insights:** Created an interactive bar chart for easy comparison of income and expenses.
- **Key Observations:** Identified seasonal trends and months with high expenses for potential budget adjustments.
- **Recommendations:** Regularly review budget data, set financial goals, and explore additional visualizations for deeper insights.

## Challenges Faced
- **Data Quality:** Issues with accuracy and completeness.
- **Integration Issues:** Difficulty combining data from multiple sources.
- **Time Constraints:** Limited time for in-depth analysis.
- **Technical Limitations:** Software restrictions on visualizations.
- **Stakeholder Communication:** Misalignment of expectations.
- **Changing Requirements:** Frequent adjustments causing delays.
- **Resource Availability:** Limited access to necessary tools.

