import pandas as pd
import matplotlib.pyplot as plt

# import .csv data to pandas
path_to_file = "/Users/mjmatray/Desktop/mxv/aggregate.csv"
# I assigned csv as monitor_psi
monitor_psi = pd.read_csv(path_to_file)

# test here to show first 5 entries
#print(monitor_psi.head())

#filter out all columns except needed psi and well codes
selected_columns = monitor_psi[["monitor_well_code","max_pressure_differential_psi_vs_predicted_monitor"]]
#print(selected_columns)

#ascending well codes, descending psi
postsort = selected_columns.sort_values(by=["monitor_well_code","max_pressure_differential_psi_vs_predicted_monitor"], ascending=[True,False])
#print(sorted)

#group by each well code and show top 2
top2 = postsort.groupby("monitor_well_code").head(2)
print(top2)

#trying out plotting the highest two points for each well code

high_psi = top2.groupby("monitor_well_code").first().reset_index()
lower_psi = top2.groupby("monitor_well_code").last().reset_index()

plt.figure(figsize=(10,6))

plt.scatter(high_psi["monitor_well_code"],high_psi["max_pressure_differential_psi_vs_predicted_monitor"], color='g', marker='^', label = "Higher PSI")
plt.scatter(lower_psi["monitor_well_code"], lower_psi["max_pressure_differential_psi_vs_predicted_monitor"], color='r', marker='v', label = "Lower PSI")

plt.xlabel("Monitor Well Codes")
plt.ylabel("Max Pressure Differential PSI vs Predicted Monitor")
plt.title("Top 2 PSI Values for each Monitor Well Code")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()