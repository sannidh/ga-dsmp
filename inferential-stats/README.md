### Project Overview

 Bank Of New York wants to expand its branches. It has data of 9578 customers with 15 features including borrower & loan profiles. 


### Approach taken to solve the problem

 1. Validity of Central Limit Theorem for installment column with histograms of random samples of different sizes
2. The bank manager believes that people with purpose as 'small_business' have been given int.rate more due to the risk assosciated. After converting the interest rate to float, we want to test our hypothesis whether the lending rate for small businesses is statistically higher than the others using a z-value.
3. The bank thinks that monthly installments (installment) customers have to pay might have some sort of effect on loan defaulters. We wish to do a z-test to determine whether amount of installment has something to do with loan defaults or not.
4. Bank suspects is that there is a strong association between purpose of the loan(purpose column) of a person and whether that person has paid back loan (paid.back.loan column). Since, both are categorical variables, we will do a chi-square contingency test to determine if the purpose for loan-defualters is different to non-defaulters.


