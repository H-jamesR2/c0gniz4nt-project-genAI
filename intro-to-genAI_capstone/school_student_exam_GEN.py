import pandas as pd
import numpy as np
import os

# Create the target directory if it doesn't exist
target_directory = "intro-to-genAI_projectDATA"  # Specify the folder name
if not os.path.exists(target_directory):
    os.makedirs(target_directory)

# Generate synthetic dataset for Exam Prediction (Supervised Learning)
np.random.seed(42)
num_students = 500

study_hours = np.random.randint(0, 40, num_students)
past_scores = np.random.randint(50, 100, num_students)
attendance_rate = np.random.uniform(50, 100, num_students)
assignments_completed = np.random.randint(5, 20, num_students)

# Simulated exam result (Pass = 1, Fail = 0) based on study patterns
exam_result = (study_hours * 0.5 + past_scores * 0.3 + attendance_rate * 0.15 + assignments_completed * 0.05) > 75
exam_result = exam_result.astype(int)

exam_df = pd.DataFrame({
    "study_hours": study_hours,
    "past_scores": past_scores,
    "attendance_rate": attendance_rate,
    "assignments_completed": assignments_completed,
    "exam_result": exam_result
})

# Save as CSV
exam_df_path = os.path.join(target_directory, "exam_prediction_data.csv") # Modified path
exam_df.to_csv(exam_df_path, index=False)

# Generate synthetic dataset for Student Grouping (Clustering)
study_time_per_day = np.random.uniform(0.5, 10, num_students)
engagement_level = np.random.choice([1, 2, 3], num_students)  # 1: Low, 2: Medium, 3: High
quiz_scores = np.random.randint(50, 100, num_students)
group_project_participation = np.random.randint(1, 10, num_students)

student_group_df = pd.DataFrame({
    "study_time_per_day": study_time_per_day,
    "engagement_level": engagement_level,
    "quiz_scores": quiz_scores,
    "group_project_participation": group_project_participation
})

# Save as CSV
student_group_df_path = os.path.join(target_directory, "student_grouping_data.csv") # Modified path
student_group_df.to_csv(student_group_df_path, index=False)

print(f"Exam data saved to: {exam_df_path}")
print(f"Student group data saved to: {student_group_df_path}")