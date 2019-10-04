# milkbasket
Project Created for Metric Analysis

There are two notebooks inside the items recommender:
* recommendation-MT.ipynb -> Recommendation system to suggest a customer comparsion based on shopping trends 
* Dependency issue. Will work only on Linux/Mac/Windows Subsystem for Linux
* rfm-analysis.ipynb -> Modeling customer churn for milkbasket (Predicted using the entire data set)

Please copy the csv file to \items-recommender\data with the name hackathon_data.csv to correct the dependencies, run both jupyter notebooks to find the insights.

Flask project feeds the recommender system output CSV and should be run to ensure that mobile app loads the webview.
Appropriate Flask URL changes has to be made in the mobile app source code to ensure the working of the app. A working video has been kept inside the pptx for reference

* Curated by Farhan
