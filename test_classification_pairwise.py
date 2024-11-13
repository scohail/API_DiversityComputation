import unittest
from diversity_metrics.classification.Pairwise.pairwise_metrics import  CorrelationCoefficient, QStatistics, DifferencesMeasure, DoubleFaultMeasure, CombinationD_DF

# Example usage

# Example predictions from two regressors
y1 = [1,0,1 ,0]
y2 = [1,0,1,1]
y_true = [1,1,0,1]


def test_correlation_coefficient():
    
    correlation_metric = CorrelationCoefficient(y1, y2, y_true)
    result = correlation_metric.calculate()
    print("Correlation Coefficient:", result)

def test_q_statistics():
    q_metric = QStatistics(y1, y2, y_true)
    result = q_metric.calculate()
    print("Q Statistics:", result)

def test_differences_measure():
    diff_metric = DifferencesMeasure(y1, y2, y_true)
    result = diff_metric.calculate()
    print("Differences Measure:", result)

def test_double_fault_measure():
    double_fault_metric = DoubleFaultMeasure(y1, y2, y_true)
    result = double_fault_metric.calculate()
    print("Double Fault Measure:", result)


def test_combination_d_df():
    combination_metric = CombinationD_DF(y1, y2, y_true)
    result = combination_metric.calculate()
    print("Combination D_DF:", result)


test_differences_measure()
test_double_fault_measure()
test_combination_d_df()
