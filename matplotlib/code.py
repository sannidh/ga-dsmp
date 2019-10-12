# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Code starts here
data = pd.read_csv(path)
loan_status = data['Loan_Status'].value_counts()
loan_status.plot(kind='bar')


# --------------
#Code starts here
property_and_loan = data.groupby(['Property_Area','Loan_Status']).size().unstack()
property_and_loan.plot(kind='bar', stacked=False, figsize=(15,10))
plt.xlabel('Property Area')
plt.ylabel('Loan Status')
plt.xticks(rotation=45)
plt.show()


# --------------
#Code starts here
education_and_loan = data.groupby(['Education', 'Loan_Status']).size().unstack()
education_and_loan.plot(kind='bar', stacked=False, figsize=(15,10))
plt.xlabel('Education Status')
plt.ylabel('Loan Status')
plt.xticks(rotation=45)
plt.show()


# --------------
#Code starts here
graduate = data[data['Education']=='Graduate']
not_graduate = data[data['Education']=='Not Graduate']
graduate.plot(y='LoanAmount',kind='density', label='Graduate')
not_graduate.plot(y='LoanAmount', kind='density', label='Non Graduate')
plt.show()
#Code ends here
#For automatic legend display
plt.legend()


# --------------
#Code starts here
fig ,(ax_1,ax_2,ax_3) = plt.subplots(nrows=3, ncols=1, figsize=(8,24))
data.plot.scatter(x='ApplicantIncome', y='LoanAmount', ax=ax_1)
ax_1.set_title('Applicant Income')
data.plot.scatter(x='CoapplicantIncome', y='LoanAmount', ax=ax_2)
ax_2.set_title('Coapplicant Income')
data['TotalIncome'] = data['ApplicantIncome'] + data['CoapplicantIncome']
data.plot.scatter(x='TotalIncome', y='LoanAmount', ax=ax_3)
ax_3.set_title('Total Income')
plt.tight_layout()


