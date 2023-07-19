import pandas as pd

df=pd.read_csv('stud.csv')
marks_gt_80=df[(df['marks']>89)]
max_mark=df['marks'].max()
student_with_max_mark=df[(df['marks']==max_mark)]
df['cgpa']=df['marks']/10
sum_marks=df['marks'].sum()
avg_marks=df['marks'].mean()
print("Average marks: ",avg_marks)
people_above_avg_marks=df[(df['marks']>avg_marks)]
print("People above average marks: ")
print(people_above_avg_marks)
# print(marks_gt_80)
# print("Topper data: ")
# print(student_with_max_mark)
# print("Details with cgpa: ")
print(df)
(x,y)=df.shape
print("Shape x: ",x,"y: ",y)


