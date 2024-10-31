import unittest
from diversity_metrics.regression.pairwise_metrics import CorrelationCoefficient, mean_squared_difference,Disagreement_Mesure


# Example usage

# Example predictions from two regressors
y1 = [2.3, 4.5, 3.2, 5.1]
y2 = [2.1, 4.6, 3.3, 5.0]


def test_correlation_coefficient():
    
    correlation_metric = CorrelationCoefficient(y1, y2)
    result = correlation_metric.calculate()
    print("Correlation Coefficient:", result)

def test_mean_squared_difference():
    mean_squared_difference_metric = mean_squared_difference(y1, y2)    
    result = mean_squared_difference_metric.calculate()
    print("Mean Squared Difference:", result)

def test_disagreement_mesure():
    disagreement_mesure_metric = Disagreement_Mesure(y1, y2,threshold=0.05)
    result = disagreement_mesure_metric.calculate()
    print("Disagreement Mesure:", result)

test_disagreement_mesure()