'''
The purpose of this file is to store personal examples from ch 2
'''

import thinkstats2
hist = thinkstats2.Hist([1, 2, 2, 3, 5])
hist


hist.Freq(2)

hist.Values()

for val in sorted(hist.Values()):
    print(val, hist.Freq(val))

for val, freq in hist.Items():
         print(val, freq)

## Plotting histograms

import thinkplot

thinkplot.Hist(hist)
thinkplot.Show(xlabel='value', ylabel='frequency')


## NSFG variables

import nsfg

# start by reading the data and selecting records for live births
preg = nsfg.ReadFemPreg()
live = preg[preg.outcome == 1]

# generate and plot the histogram of birthwgt_lb for live births
hist = thinkstats2.Hist(live.birthwgt_lb, label='birthwgt_lb')
thinkplot.Hist(hist)
thinkplot.Show(xlabel='pounds', ylabel='frequency')


## Outliers

# this function takes an integer and returns the largest or smallest x values

# smallest
for weeks, freq in hist.Smallest(10):
    print(weeks, freq)

# largest
for weeks, freq in hist.Largest(10):
    print(weeks, freq)

## First Babies

#divided the DataFrame of live births using birthord
firsts = live[live.birthord == 1]
others = live[live.birthord != 1]

# and computed their histograms
first_hist = thinkstats2.Hist(firsts.prglngth)
other_hist = thinkstats2.Hist(others.prglngth)

# plot
width = 0.45
thinkplot.PrePlot(2)
thinkplot.Hist(first_hist, align='right', width=width)
thinkplot.Hist(other_hist, align='left', width=width)
thinkplot.Show(xlabel='weeks', ylabel='frequency')

# pandas methods for mean, variance and standard deviation
mean = live.prglngth.mean()
var = live.prglngth.var()
std = live.prglngth.std()

# Cohen's d

def CohenEffectSize(group1, group2):
    diff = group1.mean() - group2.mean()
    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)
    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    d = diff / math.sqrt(pooled_var)
    return d

# test it out
CohenEffectSize(firsts.prglngth, others.prglngth)