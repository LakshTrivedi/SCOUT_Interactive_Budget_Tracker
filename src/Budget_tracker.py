import pandas as pd
import plotly.express as px

# Read the predefined dataset from a CSV file
budget_df = pd.read_csv('budget_data.csv')

# Convert the 'Date' column to datetime format for easier manipulation
budget_df['Date'] = pd.to_datetime(budget_df['Date'])

# Extract the year from the 'Date' column for filtering
budget_df['Year'] = budget_df['Date'].dt.year

# Take user input for the year
year_input = input("Please enter a year to display the budget data: ")

try:
    year = int(year_input)
    
    # Filter the DataFrame for the specified year
    budget_df = budget_df[budget_df['Year'] == year]
    
    if budget_df.empty:
        print(f"No data available for the year {year}.")
    else:
        # Extract the month name from the 'Date' column for grouping
        budget_df['Month'] = budget_df['Date'].dt.month_name()

        # Filter out daily expenses (assuming daily expenses have a specific value or type)
        budget_df = budget_df[~((budget_df['Type'] == 'Expenses') & (budget_df['Amount'] == 0))]

        # Group by month and type, summing the amounts
        monthly_summary = budget_df.groupby(['Month', 'Type'], as_index=False)['Amount'].sum()

        # Define the order of months for proper display on the x-axis
        month_order = [
            'January', 'February', 'March', 'April', 'May', 'June', 
            'July', 'August', 'September', 'October', 'November', 'December'
        ]

        # Set the 'Month' column as a categorical variable with the specified order
        monthly_summary['Month'] = pd.Categorical(monthly_summary['Month'], categories=month_order, ordered=True)

        # Define a color palette for different types of financial data
        color_map = {
            'Income': 'green',          # Color for Income
            'Loans': 'yellow',          # Color for Loans
            'Miscellaneous': 'orange'   # Color for Miscellaneous
        }

        # Create an interactive bar chart
        fig = px.bar(monthly_summary, 
                     x='Month', 
                     y='Amount', 
                     color='Type', 
                     title=f'Monthly Income, Loans, and Miscellaneous Expenses ({year})',
                     labels={'Amount': 'Amount', 'Month': 'Month'},
                     barmode='group',
                     color_discrete_map=color_map)  # Removed text parameter to not show amounts on bars

        # Update layout for better readability with a dark background
        fig.update_layout(
            yaxis_title='Amount',  # Label for the y-axis
            xaxis_title='Month',   # Label for the x-axis
            legend_title='Type',   # Title for the legend
            template='plotly_dark', # Use a dark template for better contrast
            plot_bgcolor='black',   # Set plot background color to black
            paper_bgcolor='black',   # Set paper background color to black
            yaxis_tickformat='₹,1.1f', # Format Y-axis ticks to include ₹ and show as whole numbers
        )

        # Set the Y-axis range from 0 to 10
        fig.update_yaxes(range=[0, 20])

        # Show the figure without text on bars
        fig.show()

except ValueError:
    print("Invalid input. Please enter a valid year.")