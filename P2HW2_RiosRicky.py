#Your Name

#Date

#Assignment Name

#Brief description of program

m_1_grade=float(input())
print("Enter grade for Module 1:",m_1_grade)
m_2_grade=float(input())
print("Enter grade for Module 2:",m_2_grade)
m_3_grade=float(input())
print("Enter grade for Module 3:",m_3_grade)
m_4_grade=float(input())
print("Enter grade for Module 4:",m_4_grade)
m_5_grade=float(input())
print("Enter grade for Module 5:",m_5_grade)
m_6_grade=float(input())
print("Enter grade for Module 6:",m_6_grade)
print()
print("-----------Results-----------")
all_grades=[m_1_grade, m_2_grade, m_3_grade, m_4_grade, m_5_grade, m_6_grade]
sum_grades=m_1_grade+ m_2_grade+ m_3_grade+ m_4_grade+ m_5_grade+ m_6_grade
avg_grades=(m_1_grade+ m_2_grade+ m_3_grade+ m_4_grade+ m_5_grade+ m_6_grade)/6

print("Lowest Grade:", f'{min(all_grades)}')
print("Highest Grade:", f'{max(all_grades)}')
print("sum of Grades:", f'{sum_grades}')
print('Average:', f'{avg_grades:.2f}')
print("---------------------------------------")




