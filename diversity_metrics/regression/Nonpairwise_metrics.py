import numpy as np
from .NonPairwise_base_metric import NonPairwiseRegressionMetric


class VarianceOutputs(NonPairwiseRegressionMetric):
    """
    Calculate the Variance of Outputs metric for an ensemble of regressors.
    """

    def calculate(self):
        """
        Calculate the Variance of Outputs metric.

        Returns:
        float: The average variance of outputs across all data points.
        """
        
        
        # Calculate the mean prediction for each data point across all regressors
        mean_predictions = np.mean(self.predictions, axis=0)
        
        # Calculate the variance for each data point
        variances = np.mean((self.predictions - mean_predictions) ** 2, axis=0)
        
        # Return the average variance across all data points
        
        return np.mean(variances)


# class Ambiguity(NonPairwiseRegressionMetric):
#     """
#     Calculate the Ambiguity metric for an ensemble of regressors.
#     """

#     def calculate(self):
#         """
#         Calculate the Ambiguity metric.

#         Returns:
#         float: The average ambiguity across all data points.
#         """
        
#         # Calculate the mean prediction for each data point across all regressors
#         mean_predictions = np.mean(self.predictions, axis=0)
        
#         # Calculate the variance for each data point
#         variances = np.mean((self.predictions - mean_predictions) ** 2, axis=0)
        
        