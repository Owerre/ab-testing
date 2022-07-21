# Project Overview

An e-commerce company conducted an A/B testing experiment to test if a new feature they recently introduced in their website through mobile app will increase revenue. They have measured the revenue as the outcome for each user (customer). The experiment was conducted by randomly assigning customers to the treatment with the new feature or the control without the new feature, at equal traffic. I have assumed that power analysis was conducted prior to performing this experiment.

In this project, I have implemented different statistical tests on the data in order to validate if the new feature has a positive impact on revenue. This is done by establishing a statistically significant result.  For pedagogical purposes, I have implemented the following two sample statistical tests:

1). Student's t-test

2). Welch's t-test

3). Mann-Whitney u-test


# Data Exploration
Below are some figures from exploratory data analysis.

## 1. Treatment and Control Groups
The distribution of revenue is highly right skewed as expected, since some customers spent more than others. Therefore, I have transformed it by log base 10. The mean of revenue (i.e., revenue-per-user) in the treatment group is higher than the control group. I need to establish if the difference is statistically significant. 

![fig](ab-testing/ab-testing/images/fig1.png)

## 2. Segmentation by Phone Operating Systems
The distributions below show segmentation by phone operating systems within the treatment and control groups. The results show disproportionality in the number of users (customers) and total revenue across the phone operating systems.

In practice, any interesting feature in the data should be investigated by invoking the Twyman's law. For instance, one might want to investigate if the new feature is compactible with different phone operating systems.

![fig](ab-testing/ab-testing/images/fig4.png)

![fig](ab-testing/ab-testing/images/fig3.png)

![fig](ab-testing/ab-testing/images/fig2.png)


