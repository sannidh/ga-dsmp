### Project Overview

 Lending Club connects people who need money (borrowers) with people who have money (investors). As an investor one would want to invest in people who showed a profile of having a high probability of paying the amount back. We want to compute the probability that the borrower paid back their loan in full. 


### Approach taken to solve the problem

 1. Joint probability is important from the perspective that conditions are independent from one other. On checking whether the condition fico credit score is greater than 700 and purpose == 'debt_consolidation' are independent from each other, it's found that they are not independent of each other
2. By calculating with the help of Bayes' theorem on whether the probability of credit policy is yes and then the person is given the loan.
3. Visualization of a bar plot for the purpose, using condition where loan is not paid back.
4. Plotting histogram for visualization of the continuous variable installment & annual income to see the trends.


