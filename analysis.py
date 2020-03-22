# !git clone https://github.com/kylemath/375Data_2020.git
# !cd 375Data_2020/

# Import code libraries we will use
import numpy as np   #for math 
import pandas as pd  # for data
import matplotlib.pyplot as plt #for plotting
# %matplotlib inline #so plots stay in this page

# Load and plot the data
conditions = [ #list of condition names of each file
	'ClosedFrontal',
	# 'OpenFrontal',
	# 'ClosedTemporal',
	# 'OpenTemporal'
]

condition_mean = {}; # place to save means for each condition
condition_std = {};
freqs = list(range(29)) # create an array of the frequencies from 1 to 30

for condition in conditions: # For each condition
	df = pd.read_csv('./' + condition + '.csv') #read in the data file for that condition
	df = df.drop(['Lab ID Number'], axis=1)
	sub_mean = df.mean(axis=1)
	print(np.tile(sub_mean, (30, 1)))
	print(df - np.tile(sub_mean, (30, 1)).transpose())

	# df.drop('Lab ID Number', axis=1)
	# print(df.mean(axis=1))

plt.xlabel('Frequency (Hz)') #axis labels
plt.ylabel('Power ($\u03BCV^2$)')
plt.legend(conditions) #legend with condition names
plt.show() #show the plot
