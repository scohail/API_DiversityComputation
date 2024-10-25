from Classification_Diversity import  Interrater_Agreement
from Classification_Diversity import  Correlation_Coefficient

from Classification_Diversity import  Q_statistic
from Classification_Diversity import Double_Fault_Measure

predictions1 = [1, 1, 1, 1]

predictions2 = [1, 1, 1,1]

true_labels = [1, 1, 1, 1]


# print(Correlation_Coefficient(predictions1,predictions2, true_labels))
# print(Double_Fault_Measure(predictions1,predictions2, true_labels))
print(Q_statistic(predictions1,predictions2, true_labels))