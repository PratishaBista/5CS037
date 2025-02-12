def analyze_column(data, columns=None):
    columns = columns or data.columns

    for column in columns:
        stats = data[column].describe()
        Q1, Q3 = stats["25%"], stats["75%"]
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        skewness = data[column].skew()
        skew_label = (
            "Left-skewed (Negative) → Mean < Median < Mode" if skewness < -0.5 else 
            "Right-skewed (Positive) → Mode < Median < Mean" if skewness > 0.5 else 
            "Symmetric → Mean ≈ Median ≈ Mode"
        )

        outliers_above = data[data[column] > upper_bound][column].tolist()
        outliers_below = data[data[column] < lower_bound][column].tolist()
        outlier_count = len(outliers_above) + len(outliers_below)

        print(f"""
        TARGET VARIABLE: {column.upper()}
        Lower Bound for Outliers: {lower_bound:.2f}
        Upper Bound for Outliers: {upper_bound:.2f}
        Skewness Analysis: {skew_label}

        Outlier Detection
           - Total Outliers: {outlier_count}
           - Outliers Above Upper Bound: {outliers_above if outliers_above else 'None'}
           - Outliers Below Lower Bound: {outliers_below if outliers_below else 'None'}
        """)

