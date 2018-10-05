import scipy.stats as sst

# In the README, we simulated a distribution from which we randomly sampled
# 25 times. If we consider that sampling as one "experiment", we'd like to
# re-do that experiment many times to estimate the literature in a field.

# If we re-do the experiment 200 times, using the same distribution described
# in the README, what is the average effect size for
# only the "significant experiements" ?

norm = sst.norm(0.4, 1)
