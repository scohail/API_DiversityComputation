from .Pairwise_base_metric import PairwiseClassificationMetric
import numpy as np






class CorrelationCoefficient(PairwiseClassificationMetric):
    """
    Correlation Coefficient (ρ) metric to measure the similarity between
    two classifiers based on their predictions and true labels.
    """

    def calculate(self):
        """
        Calculate the Correlation Coefficient (ρ) for two classifiers.

        Returns:
        float: The correlation coefficient (ρ) value between -1 and 1.

        Raises:
        ZeroDivisionError: If the denominator is zero.
        """
        # Get binary counts for A, B, C, D
        a, b, c, d = self._binary_counts()
        
        # Calculate the numerator and denominator for the correlation coefficient formula
        numerator = (a * d) - (b * c)
        denominator = np.sqrt((a + b) * (c + d) * (a + c) * (b + d))
        
        # Check for zero denominator
        if denominator == 0:
            raise ZeroDivisionError("Denominator is zero")

        # Calculate correlation coefficient
        rho = numerator / denominator
        return rho
    


class QStatistics(PairwiseClassificationMetric):
    """
    Q Statistics metric to measure the level of agreement between two classifiers.
    """

    def calculate(self):
        """
        Calculate the Q Statistics for two classifiers.

        Returns:
        float: The Q Statistics value between -1 and 1.

        Raises:
        ZeroDivisionError: If the denominator is zero.
        """
        # Get binary counts for A, B, C, D
        a, b, c, d = self._binary_counts()
        
        # Calculate the numerator and denominator for the Q Statistics formula
        numerator = (a * d) - (b * c)
        denominator = (a * d) + (c * d)
        
        # Check for zero denominator
        if denominator == 0:
            raise ZeroDivisionError("Denominator is zero")

        # Calculate Q Statistics
        q = numerator / denominator
        return q