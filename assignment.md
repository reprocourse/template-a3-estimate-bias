# A simple simulation to estimate the bias of the effect size due to the file drawer effect

The goal is to create a little simulation environment for you to get a practical feeling of the bias. 
This is the experiment.

Let's stay I have normally distributed data. I am sampling (participants, animals) in this distribution. The effect size is .4 and the standard deviation is 1. So, I am sampling in  N(0.4, 1). 

Say I sample 25 samples. Calculate the mean, and test if this is different from zero, at the 5% level.

Redo this experiment 200 times. What is the average effect found for the "significant" experiment ?

```
# imports
import scipy.stats as sst

# create a normal distribution with mean .4 and std 1:
norm = sst.norm(.4, 1)

# sample 25 from it:
group1 = norm.rvs(size=(25,))

# measured effect size of group 1 ?
print(group1.mean())

# do the test : is this measured effect size significant at $\alpha = .05$

# redo the experiment N=200 times - what is the mean of the "significant effet sizes" ?
```

