import matplotlib as mpl
import numpy as np
mpl.use('TkAgg')
import matplotlib.pyplot as plt
from epl_table_simulation import SimTeam
import variation_metrics
from scipy.interpolate import spline


Var_Data = variation_metrics.fill_data()
years = sorted(Var_Data.keys())


years_num = [int(year[:4]) for year in years if 1 in Var_Data[year]]


act_sd = [Var_Data[year][1]['act table SD'] for year in years]
sim_sd = [Var_Data[year][1]['sim table SD'] for year in years]
xv_metric = [Var_Data[year][1]['our metric'] for year in years]

'''
act_sd = [Var_Data[year][2]['act table SD'] for year in years if 2 in Var_Data[year]]
sim_sd = [Var_Data[year][2]['sim table SD'] for year in years if 2 in Var_Data[year]]
xv_metric = [Var_Data[year][2]['our metric'] for year in years if 2 in Var_Data[year]]
'''
'''
act_sd = [Var_Data[year][3]['act table SD'] for year in years if 3 in Var_Data[year]]
sim_sd = [Var_Data[year][3]['sim table SD'] for year in years if 3 in Var_Data[year]]
xv_metric = [Var_Data[year][3]['our metric'] for year in years if 3 in Var_Data[year]]
'''
plt.plot(years_num, act_sd, 'b', years_num, sim_sd, 'g', years_num, xv_metric, 'r')
plt.title("Various Metrics")
plt.xlabel("Year")
leg = ["Act Table SD", "Sim Table SD", "XV Metric"]
plt.legend(leg)

poly_deg = 5
coefs = np.polyfit(years_num, act_sd, poly_deg)
y_poly = np.polyval(coefs, years_num)
plt.plot(years_num, y_poly, 'b--')
coefs = np.polyfit(years_num, xv_metric, poly_deg)
y_poly = np.polyval(coefs, years_num)
plt.plot(years_num, y_poly, 'r--')





plt.show()