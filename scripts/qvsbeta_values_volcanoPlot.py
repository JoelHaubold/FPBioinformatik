import seaborn as sns
import pandas as pd
import os
import math

path = os.path.abspath('sleuthResults/sleuth_wald_results.tsv')
samples = pd.read_table(path)

#print(samples.loc[:,'qval'])
samples.loc[:,'qval'] = samples.loc[:,'qval'].apply(lambda x: -math.log10(x))
samples['color'] = ""
for row in samples.index:
	if abs(samples.loc[row,"b"])>1:
		if samples.loc[row,"qval"]>4:
			samples.loc[row,"color"] = 'green'
		else:
			samples.loc[row,"color"] = 'orange'
	else:
		if samples.loc[row,"qval"]>4:
			samples.loc[row,"color"] = 'red'
		else:
			samples.loc[row,"color"] = 'black'
	#print(samples.loc[row,"color"])
#print(samples.loc[:,'qval'])
palette ={"green":"g","orange":"orange","red":"r", "black":"k"}
plot = sns.scatterplot(x = "b",y = "qval",data = samples,hue="color",palette = palette)
for row in samples.index:
	if samples.loc[row,"color"] == "green":
		plot.text(samples.loc[row,"b"]+0.05, samples.loc[row,"qval"]+0.05, samples.loc[row,"target_id"], horizontalalignment='left', size='small', color='black')#, weight='semibold')
#figure = plot.get_figure()
plot.set(xlabel='beta_value', ylabel='-log10(q_value)')
plot.get_figure().savefig("plots/qvsbeta_values_volcanoPlot.pdf")
