# Exploratory Data Analysis (EDA) in Python

## Overview
This project demonstrates **Exploratory Data Analysis (EDA)** on a dataset using Python. The primary focus is on understanding the distribution of variables, identifying outliers, and checking for correlations between variables. Various visualizations, including bar charts, scatter plots, and line charts, are used to gain insights from the data.

EDA is an essential step in the data analysis pipeline, helping to uncover patterns, detect anomalies, and test assumptions through summary statistics and graphical representations.

## Project Details

### Libraries Used
- **pandas**: For data manipulation and analysis.
- **numpy**: For numerical operations.
- **matplotlib**: For visualization.
- **seaborn**: For statistical data visualization.
- **datetime**: For handling date/time data.

### Key Operations
- **Data Cleaning:**
  - Loaded and displayed the dataset.
  - Removed duplicate records to maintain data integrity.
  - Dropped unnecessary columns (`thumbnail_link`, `description`).
  - Converted date columns into proper datetime format.
- **Feature Engineering:**
  - Extracted `publish_month`, `publish_day`, and `publish_hour` from `publish_time`.
  - Mapped `category_id` to human-readable `category_name`.
- **Data Visualization:**
  - **Bar Charts:** Displayed total videos and total views per year.
  - **Scatter Plots:** Visualized the relationship between views and likes.
  - **Count Plots:** Analyzed the distribution of categories and publish times.
  - **Line Charts:** Showed the number of videos published over time.
  - **Correlation Analysis:** Examined relationships between numerical features.

## Getting Started

### Prerequisites
- Python 3.x
- Required libraries installed:

```bash
pip install pandas numpy matplotlib seaborn
```

### Usage Instructions
1. Clone the repository to your local machine.

   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory.

   ```bash
   cd exploratory-data-analysis
   ```

3. Run the Python script to execute the data analysis tasks.

   ```bash
   python eda.py
   ```

### Example Functionality
Once executed, the script will generate various charts and summary statistics. These visualizations help identify trends, outliers, and relationships within the dataset. Users can modify the script to explore additional insights based on their specific data analysis needs.

## Conclusion
This project serves as a foundation for **Exploratory Data Analysis (EDA)**, which is a critical step in understanding and preparing data for further analysis or machine learning. By leveraging Python’s powerful libraries, this project enables users to make data-driven decisions efficiently.

---

### Author
Your Name
