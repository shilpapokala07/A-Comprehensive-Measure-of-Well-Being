This document explains each epic and story in simple step-by-step form.
Epic 1: Environment Setup
Install Python.
Open VS Code.
Open Terminal.
Run: python -m pip install numpy pandas matplotlib seaborn scikit-learn flask
Create folders: dataset, model, templates, static. Epic 2: Import Libraries
Create train_model.py.
Import numpy, pandas, matplotlib, seaborn, sklearn, pickle and flask. Epic 3: Dataset
Download dataset from Kaggle.
Place it in dataset folder.
Load using pandas.
Use head(), info(), describe().
Create basic visualizations. Epic 4: Data Preprocessing
Select X and Y.
Check missing values.
Handle null values.
Encode categorical columns if needed.
Prepare cleaned dataset. Epic 5: Train-Test Split
Use train_test_split().
Keep 80% training and 20% testing. Epic 6: Train Model
Create LinearRegression model.
Fit using training data.
Predict on test data.
Evaluate using R2 score. Epic 7: Save Model
Save model using pickle.dump().
Verify HDI.pkl is created. Epic 8: Flask Web Application
Create app.py.
Load HDI.pkl.
Create '/' and '/predict' routes.
Create templates/home.html and indexnew.html.
Create static/style.css.
Run python app.py.
Open http://127.0.0.1:5000.
Test prediction and verify output.