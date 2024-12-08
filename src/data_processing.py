import pandas as pd

def load_and_process_data(file_path, year):
    # Read the predefined dataset from a CSV file
    budget_df = pd.read_csv(file_path)

    # Convert the 'Date' column to datetime format for easier manipulation
    budget_df['Date'] = pd.to_datetime(budget_df['Date'])

    # Extract the year from the 'Date' column for filtering
    budget_df['Year'] = budget_df['Date'].dt.year

    # Filter the DataFrame for the specified year
    budget_df = budget_df[budget_df['Year'] == year]

    if budget_df.empty:
        return None

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

    return monthly_summary