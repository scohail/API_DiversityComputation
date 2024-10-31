import unittest
from diversity_metrics.regression.pairwise_metrics import CorrelationCoefficient, DisagreementMeasure


# Example usage

# Example predictions from two regressors
y1 = [2.3, 4.5, 3.2, 5.1]
y2 = [2.1, 4.6, 3.3, 5.0]

# Instantiate the correlation coefficient metric
correlation_metric = CorrelationCoefficient(y1, y2)

# Calculate the result
result = correlation_metric.calculate()
print("Correlation Coefficient:", result)
