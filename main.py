from flask import Flask, render_template, request, jsonify
import pandas as pd
import matplotlib.pyplot as plt
import base64
import io
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)

# Load the dataset
df = pd.read_csv("DefaulterList - Sheet1 (1).csv")

# Encode the target variable
le = LabelEncoder()
df['Defaulter'] = le.fit_transform(df['Defaulter'])

# Selecting only the specified columns for features
selected_columns = ['IoT', 'SE', 'HS-OB', 'OE1- SC', 'OEI-ICCF', 'IOTL']
X = df[selected_columns]

# Target variable
y = df['Defaulter']

# Splitting the dataset into the Training set and Test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

outlier_indices = []
for column in selected_columns:
    outlier_index = df[df[column] > 30].index
    outlier_indices.extend(outlier_index)

# Remove outliers from the dataset
df.drop(outlier_indices, inplace=True)

# Initialize the Random Forest classifier
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the classifier
rf_classifier.fit(X_train, y_train)


def load_data():
    # Load CSV data into a pandas DataFrame
    df = pd.read_csv("DefaulterList - Sheet1 (1).csv")
    return df


def generate_pie_chart(df):
    # Count the number of defaulters and non-defaulters for "YES" and "NO"
    yes_defaulters = df[df['Defaulter'] == 'YES'].shape[0]
    no_defaulters = df[df['Defaulter'] == 'NO'].shape[0]

    # Calculate percentages
    total = yes_defaulters + no_defaulters
    yes_percent = (yes_defaulters / total) * 100
    no_percent = (no_defaulters / total) * 100

    return [yes_percent, no_percent]


def generate_bar_graph(df):
    defaulter_counts = {}
    subjects = ['IoT', 'SE', 'HS-OB', 'OE1- SC', 'OEI-ICCF', 'IOTL']
    for subject in subjects:
        counts = df['Defaulter(' + subject + ')'].value_counts()
        defaulter_counts[subject] = counts

    # Extract counts for YES and NO
    yes_counts = [defaulter_counts[subject].get('YES', 0) for subject in subjects]
    no_counts = [defaulter_counts[subject].get('NO', 0) for subject in subjects]

    # Plotting
    fig, ax = plt.subplots(figsize=(10, 6))

    # Bar width
    bar_width = 0.35

    # Bar positions
    bar_positions = range(len(subjects))

    # Plotting "NO" counts
    ax.bar([pos - bar_width/2 for pos in bar_positions], no_counts, bar_width, label='NO', color='lightgreen')

    # Plotting "YES" counts
    ax.bar([pos + bar_width/2 for pos in bar_positions], yes_counts, bar_width, label='YES', color='lightblue')

    # Adding labels and title
    ax.set_ylabel('Count')
    ax.set_title('Defaulter Classes Distribution for Each Subject')
    ax.set_xticks(bar_positions)
    ax.set_xticklabels(subjects)
    ax.legend()

    # Save the plot to BytesIO object
    img = io.BytesIO()
    plt.xticks(rotation=45)
    plt.savefig(img, format='svg')  # Save as SVG format
    img.seek(0)

    # Encode the image as a base64 string
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')

    return plot_url


def find_outliers(df):
    outlier_indices = []
    outlier_info = []

    for column in selected_columns:
        outliers = df[df[column] > 30]
        if not outliers.empty:
            for idx, row in outliers.iterrows():
                outlier_info.append({
                    'CNumber': row['CNumber'],
                    'Name': row['Name of the Student'],
                    'Subject': column,
                    'Value': row[column]
                })
            outlier_indices.extend(outliers.index)

    return outlier_info, outlier_indices


@app.route('/')
def predict():
    return render_template('interface.html')


@app.route('/predict', methods=['POST'])
def handle_predict():
    # Extracting values from the form
    iot = int(request.form['iot'])
    se = int(request.form['se'])
    hs_ob = int(request.form['hs-ob'])
    oe1_sc = int(request.form['oe1-sc'])
    oei_iccf = int(request.form['oei-iccf'])
    iotl = int(request.form['iotl'])

    # Making prediction
    prediction = rf_classifier.predict([[iot, se, hs_ob, oe1_sc, oei_iccf, iotl]])

    # Convert prediction back to its original label
    prediction = le.inverse_transform(prediction)[0]

    return render_template('interface.html', prediction=prediction)


@app.route('/visualization')
def visualize():
    df = load_data()
    pie_chart_data = generate_pie_chart(df)
    bar_graph_data = generate_bar_graph(df)
    missing_values = X_test.isnull().sum()

    # Find outliers
    outlier_info, _ = find_outliers(df)

    return render_template('index.html', missing_values=missing_values, pie_chart_data=pie_chart_data,
                           bar_graph_data=bar_graph_data, outlier_info=outlier_info)


if __name__ == '__main__':
    app.run(debug=True)
