from dataclasses import replace
import pandas as pd
COL = ['Year', 'Semester', 'College', 'Department', 'Number', 'Section',
       'Instructor_first', 'Instructor_last', 'Course_name', 'Course_Level',
       'Responses', 'Hrs_Per_Week', 'Overall_Teaching_Rate',
       'Overall_Course_Rate']
# select only useful columns
df = pd.read_csv("cmu_course_without_header.csv")

# drop row with filled with all null value
df = df.dropna(how = "all")

# fillna with specific value
# df["Overall_Teaching_Rate"] = df["Overall_Teaching_Rate"].fillna(1.7514)
# df["Overall_Course_Rate"] = df["Overall_Course_Rate"].fillna(1.7514)
# df.insert(0, 'id', range(len(df["Overall_Course_Rate"])))
df= df.iloc[:, range(15)]
df.iloc[:, [13, 14]] = df.iloc[:, [13, 14]].fillna(1.7514)

# print(df)
df.to_csv("cmu_course_cleaned.csv", index=False)

