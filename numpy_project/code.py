# --------------
# Importing header files
import numpy as np
# Path of the file has been stored in variable called 'path'
data = np.genfromtxt(path, delimiter=',', skip_header=1)
print('\nData: \n\n', data)
print("\nType of data: \n\n", type(data))
#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]
#Code starts here
census = np.concatenate((data, new_record), axis=0)


# --------------
#Code starts here
age = census[:,0]
max_age = age.max()
min_age = age.min()
age_mean = age.mean()
age_std = np.std(age)


# --------------
#Code starts here
for i in range(5):
    exec(f'race_{i} = census[census[:,2]==i]')
    exec(f'len_{i} = len(census[census[:,2]==i])')
minority_race = [len_0, len_1, len_2, len_3, len_4].index(
                                min([len_0, len_1, len_2, len_3, len_4]))


# --------------
#Code starts here
senior_citizens = census[census[:,0]>60]
working_hours_sum = senior_citizens[:,6].sum()
senior_citizens_len = len(senior_citizens)
avg_working_hours = working_hours_sum/senior_citizens_len
print(avg_working_hours)


# --------------
#Code starts here
high = census[census[:,1]>10]
low = census[census[:,1]<=10]
avg_pay_high = high[:,7].mean()
avg_pay_low = low[:,7].mean()
better_edn_better_pay = avg_pay_high > avg_pay_low
print(better_edn_better_pay)


