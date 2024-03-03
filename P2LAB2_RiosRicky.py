#Your Name

#Date

#Assignment Name

#A brief description of the project

num_1=float(input())
num_2=float(input())
num_3=float(input())
num_4=float(input())

all_nums=(num_1,num_2,num_3,num_4)
num_all_product=float(num_1*num_2*num_3*num_4)
num_avg_all=float(sum(all_nums)/len(all_nums))

print(f'{num_all_product:.0f}',f'{num_avg_all:.0f}')
print(f'{num_all_product:.3f}',f'{num_avg_all:.3f}')
