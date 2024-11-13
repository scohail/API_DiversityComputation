import unittest
from diversity_metrics.classification.Pairwise.pairwise_metrics import  CorrelationCoefficient, QStatistics

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


test_q_statistics()

