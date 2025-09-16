import pandas as pd

def wrangle(filepath):
    """
    This function cleans a csv file by removing every duplicate, every inconsistency
    and filling in missing values

    Args:
        filepath (csv): contains different details on several drug transactions
    """
    
    try:
        # Import the file
        df = pd.read_csv(filepath)
        
        # Change Date column to datetime data type
        df["Date"] = pd.to_datetime(df["Date"], format="mixed")
        
        # Drop duplicates
        df.drop_duplicates(inplace=True)
        
        # Correct inconsistencies in Brand Column
        mapping = {
        'Hea1thFirst': 'HealthFirst',
        'MediPluz': 'MediPlus',
        'FarmaTrust': 'PharmaTrust',
        'Biokare': 'BioCare'
        }
        df["Brand"] = df["Brand"].replace(mapping)
        
        # Fill the missing values in this columns with Unknown
        for col in ['Pharmacy', 'Drug', 'Brand', 'Supplier_Name']:
            df[col] = df[col].fillna("Unknown")
            
        # Fill Missing values in 'Price' by the median price of the Drug and the Brand
        df["Price"] = df.groupby(
            ["Drug", "Brand"])["Price"].transform(lambda x: x.fillna(x.median())
        )

        # Fill Missing values in 'Quantity' with the median quantity of the drug and brand sold in each pharmacy
        df["Quantity"] = df.groupby(
            ["Drug", "Brand", "Pharmacy"])["Quantity"].transform(lambda x: x.fillna(x.median())
        )

        # Create a temporary sort, but keep track of original order
        df["row_order"] = range(df.shape[0])

        # Sort by Pharmacy and Date
        df = df.sort_values(["Pharmacy", "Date"])

        # Forward fill missing dates within each pharmacy
        df["Date"] = df.groupby("Pharmacy")["Date"].ffill()

        # Restore original order
        df = df.sort_values(by="row_order").drop(columns="row_order")
        
        return df
    
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return None
    except Exception as e:
        print(f"An error occured during data cleaning: {e}")
        return None