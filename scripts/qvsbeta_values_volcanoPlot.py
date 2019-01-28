import seaborn as sns
import pandas as pd
import os
import math

path = os.path.abspath('sleuthResults/sleuth_wald_results.tsv')
samples = pd.read_table(path)
sns.set(rc={'figure.figsize':(15.7,11.27)})
sns.set_style("white")
#sns.set_style("ticks")

#print(samples.loc[:,'qval'])
samples.loc[:,'qval'] = samples.loc[:,'qval'].apply(lambda x: -math.log10(x) if x!= 0 else -math.log10(1.1928109419438e-302))
samples['color'] = ""
for row in samples.index:
	if abs(samples.loc[row,"b"])>1:
		if samples.loc[row,"qval"]>4:
			samples.loc[row,"color"] = 'significant & highly differential'
		else:
			samples.loc[row,"color"] = 'highly differential'
	else:
		if samples.loc[row,"qval"]>4:
			samples.loc[row,"color"] = 'not differential'
		else:
			samples.loc[row,"color"] = 'insignificant'
	#print(samples.loc[row,"color"])
#print(samples.loc[:,'qval'])
palette ={"significant & highly differential":"g","highly differential":"orange","not differential":"r", "insignificant":"k"}
plot = sns.scatterplot(x = "b",y = "qval",linewidth=0,data = samples,hue="color",palette = palette)
for row in samples.index:
	if samples.loc[row,"color"] == "green":
		plot.text(samples.loc[row,"b"]+0.05, samples.loc[row,"qval"]+0.05, samples.loc[row,"target_id"], horizontalalignment='left', size='small', color='black')#, weight='semibold')
#figure = plot.get_figure()
plot.set(xlabel='beta_value', ylabel='-log10(q_value)')
plot.get_figure().savefig("plots/qvsbeta_values_volcanoPlot.pdf")
