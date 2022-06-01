# UK-election-modelling
"""
Scripts to model UK elections

Although elections can be considered a true measurement of public sentiment it is likely that randomness affects a certain fraction voters. For example, there may be people who intend to vote but due to some mishap are unable. Also there may be people who 'make their mind up on the day' and are affected by random events to finalise the choice.

This code allows the impact of various levels of randomness on the 2017 UK general election results to be investigated. The primary variable in the code to affect this is 'errRate' which is currently set to 0.01 (i.e. 1%). Additionally, the number of 'elections' is set to 30 for a low runtime, a setting of at least 100 is recommended to produce representative histograms.

"""
