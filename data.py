import pandas as pd

def create_sample_column(df, key_columns, train_fraction=0.8):
    # Combine key columns into a single string for each row
    keys = df[key_columns].astype(str).agg("_".join, axis=1)

    # Generate a hash for each key and take the absolute value to ensure it's non-negative
    hashes = keys.apply(lambda x: abs(hash(x)) % 100)

    # Determine the training threshold based on the train fraction
    train_threshold = int(train_fraction * 100)

    # Assign each row to either 'train' or 'test' based on the hash value
    df['sample'] = hashes.apply(lambda x: 'train' if x < train_threshold else 'test')

    return df

# Example usage:
df = pd.DataFrame({'ID': [1, 2, 3, 4, 5], 'feature': ['A', 'B', 'C', 'D', 'E']})
df = create_sample_column(df, key_columns=['ID'], train_fraction=0.8)
print(df)
