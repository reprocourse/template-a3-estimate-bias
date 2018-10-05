# Simulate the bias on the effect size due to the "file drawer" effect

In [Button et al. (2013)](https://www.nature.com/articles/nrn3475) we read that

> Null findings locked in file drawers bias the literature

In this assignment, we'll do a small simulation to see the impact of that bias on some imagined effect.
The goal is to get a practical feeling of how bias is influencing our perception of effects in the neurosciences, and other scientific fields.

In the [SciPy lecture notes](https://www.scipy-lectures.org/packages/statistics/index.html),
we introduced two major Python packages for frequentist statistics:
- [`statsmodels`](https://www.statsmodels.org/stable/index.html)
- [`scipy.stats`](https://docs.scipy.org/doc/scipy/reference/stats.html)

We can use these packages to create our simulation.

## A small example

Let's say I have normally distributed data, and I am interested in drawing samples from this distribution.
Since this a simulation, I can precisely control the actual effect in the distribution, as well as the variance around that effect.

In this example, we'll set the effect size to 0.4 and the standard deviation to 1.
You can also write that the distribution X is X ~ N(0.4, 1); see [this StackExchange answer](https://stats.stackexchange.com/a/161814) for a deeper explanation of this notation.

First, let's generate our distribution:

```
import scipy.stats as sst

# create a normal distribution with mean 0.4 and std 1:
norm = sst.norm(0.4, 1)
```

Next, we'd like to sample 25 times from this generated distribution.

```
# sample from it 25 times:
samples = norm.rvs(size=(25,))
```

We'd then like to calculate the mean, and test if this is different from zero, at the 5% level.

```
# find the measured effect size in the obtained samples
print(samples.mean())

# do the test : is this measured effect size significant at alpha = 0.5 ?
t_statistic, p_value = sst.ttest_1samp(samples, 0)
print(p_value)
```

## This assignment

For this assignment, we'll ask you to edit [`bias_estimate.py`](https://github.com/reprocourse/template-a3-estimate-bias/blob/master/bias_estimates.py)
to repeat the above procedure 200 times.

That is, if we consider the sampling procedure above as one "experiment",
we'd like to re-do that experiment many times. We'll then only consider the significant experiments,
estimating how "publishing" or considering only significant effects impacts the literature in a field.

After you have edited [`bias_estimate.py`](https://github.com/reprocourse/template-a3-estimate-bias/blob/master/bias_estimates.py) to include the relevant code, please add your answer below:

### What is the average effect found for the "significant" experiments?

On average, the obtained effect for the significant experiments was _XX_.
