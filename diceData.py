import random
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go

dice_results = []
for i in range(1000):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice_results.append(dice1 + dice2)

mean = sum(dice_results)/len(dice_results)

median = statistics.median(dice_results)

mode = statistics.mode(dice_results)

standard_deviation = statistics.stdev(dice_results)

first_standard_deviation_start , first_standard_deviation_end = mean - standard_deviation, mean + standard_deviation
second_standard_deviation_start, second_standard_deviation_end = mean - (2*standard_deviation), mean + (2*standard_deviation)

list_of_data_within_first_standard_deviation = [result for result in dice_results if result > first_standard_deviation_start and result < first_standard_deviation_end ]
list_of_data_within_second_standard_deviation = [result for result in dice_results if result > second_standard_deviation_start and result <second_standard_deviation_end ]

print("Mean of the data is {}".format(mean))
print("Median of the data is {}".format(median))
print("Mode of the data is {}".format(mode))
print("Standard deviation of the data is {}".format(standard_deviation))
print("{}% of data lies within first standard daviation".format((len(list_of_data_within_first_standard_deviation)*100)/len(dice_results)))
print("{}% of data lies within first standard daviation".format((len(list_of_data_within_second_standard_deviation)*100)/len(dice_results)))

fig = ff.create_distplot([dice_results], ["Results"], show_hist = False)

fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.17], mode = "lines", name = "mean"))
fig.add_trace(go.Scatter(x = [first_standard_deviation_start, first_standard_deviation_start], y = [0, 0.17], mode = "lines", name = "Standard Deviation 1"))
fig.add_trace(go.Scatter(x = [first_standard_deviation_end, first_standard_deviation_end], y = [0, 0.17], mode = "lines", name = "Standard Deviation 1"))
fig.add_trace(go.Scatter(x = [second_standard_deviation_start, second_standard_deviation_start], y = [0, 0.17], mode = "lines", name = "Standard Deviation 2"))
fig.add_trace(go.Scatter(x = [second_standard_deviation_end, second_standard_deviation_end], y = [0, 0.17], mode = "lines", name = "Standard Deviation 2"))

fig.show()