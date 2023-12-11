import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE

def preprocess_data(df):
    """
    Preprocess the given DataFrame.

    Parameters:
    df (DataFrame): The DataFrame to preprocess.

    Returns:
    DataFrame: The preprocessed DataFrame.
    """
    # Handling missing values
    imputer = SimpleImputer(strategy='mean')
    df.iloc[:, :] = imputer.fit_transform(df)

    # Dealing with outliers using Z-score
    z_scores = (df - df.mean()) / df.std()
    df = df[(z_scores > -3).all(axis=1) & (z_scores < 3).all(axis=1)]

    # Normalizing data
    scaler = StandardScaler()
    df.iloc[:, :] = scaler.fit_transform(df)

    # Addressing class imbalance
    y = df['Outcome']  # Target variable
    X = df.drop('Outcome', axis=1)

    y = y.astype(int)
    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Use SMOTE to oversample the minority class in the training set
    smote = SMOTE(random_state=42)
    X_train, y_train = smote.fit_resample(X_train, y_train)

    return X_train, X_test, y_train, y_test
