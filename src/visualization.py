import pandas as pd
import plotly.express as px
from data_processing import load_and_process_data

def visualize_budget_data(monthly_summary, year):
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
                 color_discrete_map=color_map)

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

    # Set the Y-axis range from 0 to 20
    fig.update_yaxes(range=[0, 20])

    # Show the figure without text on bars
    fig.show()

if __name__ == "__main__":
    # Take user input for the year
    year_input = input("Please enter a year to display the budget data: ")

    try:
        year = int(year_input)
        monthly_summary = load_and_process_data('budget_data.csv', year)

        if monthly_summary is None:
            print(f"No data available for the year {year}.")
        else:
            visualize_budget_data(monthly_summary, year)

    except ValueError:
        print("Invalid input. Please enter a valid year.")