import unittest
from diversity_metrics.regression.pairwise_metrics import  CorrelationCoefficient, mean_squared_difference,Disagreement_Mesure,Rank_Correlation , Q_statistic , Covariance_Error,Partial_Correlation_coefficient, Double_Fault_Measure

# Example usage

# Example predictions from two regressors
y1 = [2.0, 3.0, 4.0, 5.0]
y2 = [2.2, 3.9, 4.4, 5.2]
y_true = [2.5, 3.3, 4.1, 5.0]

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

def test_rank_correlation():
    rank_correlation_metric = Rank_Correlation(y1, y2)
    result = rank_correlation_metric.calculate()
    print("Rank Correlation:", result)


def test_q_statistic():
    q_statistic_metric = Q_statistic(y1, y2, y_true=y_true)
    result = q_statistic_metric.calculate()
    print("Q Statistic:", result)
    
def test_covariance_error():
    covariance_error_metric = Covariance_Error(y1, y2, y_true=y_true)
    result = covariance_error_metric.calculate()
    print("Covariance Error:", result)


def test_partial_correlation_coefficient():
    partial_correlation_coefficient_metric = Partial_Correlation_coefficient(y1, y2, y_true=y_true)
    result = partial_correlation_coefficient_metric.calculate()
    print("Partial Correlation Coefficient:", result)

def test_double_fault_measure():
    double_fault_measure_metric = Double_Fault_Measure(y1, y2, y_true=y_true, threshold=0.05)
    result = double_fault_measure_metric.calculate()
    print("Double Fault Measure:", result)


test_double_fault_measure()



test_partial_correlation_coefficient()