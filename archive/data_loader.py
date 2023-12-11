{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "f64c82a9-7f6d-4e14-a9e2-0dabcf40c216",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "File loaded successfully.\n",
      "   Pregnancies  Glucose  BloodPressure  SkinThickness  Insulin   BMI  \\\n",
      "0            2      138             62             35        0  33.6   \n",
      "1            0       84             82             31      125  38.2   \n",
      "2            0      145              0              0        0  44.2   \n",
      "3            0      135             68             42      250  42.3   \n",
      "4            1      139             62             41      480  40.7   \n",
      "\n",
      "   DiabetesPedigreeFunction  Age  Outcome  \n",
      "0                     0.127   47        1  \n",
      "1                     0.233   23        0  \n",
      "2                     0.630   31        1  \n",
      "3                     0.365   24        1  \n",
      "4                     0.536   21        0  \n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "def load_csv(filepath):\n",
    "    \"\"\"\n",
    "    Load a CSV file into a Pandas DataFrame.\n",
    "\n",
    "    Parameters:\n",
    "    filepath (str): The path to the CSV file.\n",
    "\n",
    "    Returns:\n",
    "    DataFrame: The loaded data as a Pandas DataFrame.\n",
    "    \"\"\"\n",
    "    try:\n",
    "        df = pd.read_csv(filepath)\n",
    "        print(\"File loaded successfully.\")\n",
    "        return df\n",
    "    except FileNotFoundError:\n",
    "        print(\"File not found. Please check the file path.\")\n",
    "    except Exception as e:\n",
    "        print(f\"An error occurred: {e}\")\n",
    "\n",
    "# Example usage\n",
    "file_path = '/Users/damonnamin/desktop/MLHealth/data/diabetes-dataset.csv'  # Replace with your file path\n",
    "dataframe = load_csv(file_path)\n",
    "\n",
    "# Optional: Display the first few rows of the dataframe\n",
    "if dataframe is not None:\n",
    "    print(dataframe.head())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a4f187cf-84e1-4f66-abda-905f7140a2d2",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
