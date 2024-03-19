import pandas as pd
import numpy as np

def infer_and_convert_data_types(df):
    for col in df.columns:
        unique_values = df[col].unique()
        inferred_type = None
        
        # Group conversion logic by value type
        for value in unique_values:
            if isinstance(value, str):
                # Check if the value can be converted to datetime
                try:
                    pd.to_datetime(value)
                    df[col] = pd.to_datetime(df[col]).dt.date 
                    inferred_type = 'date'
                    break
                except ValueError:
                    pass
                
                # Check if the value can be converted to timedelta
                try:
                    pd.to_timedelta(value)
                    df[col] = pd.to_timedelta(df[col])
                    inferred_type = 'timedelta'
                    break
                except ValueError:
                    pass
                
                # Check if the value can be converted to complex
                try:
                    complex(value)
                    df[col] = df[col].apply(complex)
                    inferred_type = 'complex'
                    break
                except ValueError:
                    pass
                
                # Check if the value can be converted to numeric
                if value.replace('.', '', 1).isdigit():
                    df[col] = pd.to_numeric(df[col], errors='coerce')
                    inferred_type = 'numeric'
                    break

                # Check if the value can be converted to boolean
                if value.lower() in ['true', 'false']:
                    df[col] = df[col].astype(bool)
                    inferred_type = 'boolean'
                    break

                # Check if the column should be categorical
                if len(df[col].unique()) / len(df[col]) < 0.5:
                    inferred_type = 'categorical'
                    df[col] = pd.Categorical(df[col])
                    mode_value = df[col].mode()[0]
                    df[col] = df[col].fillna(mode_value)
                    break
            
            elif isinstance(value, (float, np.floating)) or isinstance(value, (int, np.integer)):
                # Check if the value is an integer
                try:
                    if np.isnan(value):
                        continue  # Skip NaN values
                    elif value.is_integer():
                        df[col] = pd.to_numeric(df[col], errors='coerce')
                        inferred_type = 'numeric'
                        break
                except AttributeError:
                    pass
                # Check if the value is a float
                if isinstance(value, (float, np.floating)):
                    inferred_type = 'float'
                    df[col] = pd.to_numeric(df[col], errors='coerce')
                    df[col] = df[col].fillna(df[col].mean())
                    break

            elif isinstance(value, complex):
                inferred_type = 'complex'
                df[col] = df[col].apply(complex)
                break

            elif isinstance(value, bool):
                inferred_type = 'boolean'
                df[col] = df[col].astype(bool)
                break

        # Fill missing values outside the loop to avoid repetition
        if inferred_type in ['numeric', 'boolean', 'float', 'complex']:
            df[col] = df[col].fillna(0)
        elif inferred_type == 'date':
            df[col] = df[col].fillna(pd.Timestamp('2000-01-01').date())

        # Fill categorical values
        if inferred_type == 'categorical':
            mode_value = df[col].mode()[0]
            df[col] = df[col].fillna(mode_value)

        # Set default inferred type if not detected
        if inferred_type is None:
            inferred_type = 'string'

    return df
