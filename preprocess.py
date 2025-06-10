import pandas as pd

def load_and_clean_data(file_path):
    df = pd.read_csv(file_path,
                     sep=';',
                     parse_dates={'datetime': ['Date', 'Time']},
                     infer_datetime_format=True,
                     na_values=['?'],
                     low_memory=False)

    df = df.dropna()
    df['Global_active_power'] = df['Global_active_power'].astype(float)
    df = df.set_index('datetime')
    return df
