import numpy as np
from .base_metric import RegressionMetric

class CorrelationCoefficient(RegressionMetric):
    """
    Calculate the Pearson correlation coefficient between the outputs of two regressors.
    """
    
    def calculate(self):
        """
        Calculate the Pearson correlation coefficient between y1 and y2.

        Returns:
        float: Pearson correlation coefficient.
        """
        # Calculate covariance
        covariance = np.cov(self.y1, self.y2)[0, 1]
        
        # Calculate standard deviations
        std_y1 = np.std(self.y1)
        std_y2 = np.std(self.y2)
        print(std_y1, std_y2)

        denomenator = std_y1 * std_y2   
        if denomenator == 0:
            raise ZeroDivisionError("Denominator is zero")
        
        # Calculate correlation coefficient
        return covariance / denomenator
    

class mean_squared_difference(RegressionMetric):
    """
    Calculate the mean squared difference between the outputs of two regressors.
    """
    
    def calculate(self):
        """
        Calculate the mean squared difference between y1 and y2.

        Returns:
        float: Mean squared difference.
        """
        
        return np.mean((self.y1 - self.y2) ** 2)
    

class mean_absolute_difference(RegressionMetric):
    """
    Calculate the mean absolute difference between the outputs of two regressors.
    """
    
    def calculate(self):
        """
        Calculate the mean absolute difference between y1 and y2.

        Returns:
        float: Mean absolute difference.
        """
        
        return np.mean(np.abs(self.y1 - self.y2))



class error_correlation(RegressionMetric):
    """
    Calculate the error correlation between the outputs of two regressors.
    """
    
    def calculate(self):
        """
        Calculate the error correlation between y1 and y2.

        Returns:
        float: Error correlation.
        """
        
        return np.corrcoef(self.y1 - self.y_true, self.y2 - self.y_true)[0, 1]
    

class Disagreement_Mesure(RegressionMetric):
    """
    Calculate the Disagreement Measure between two regressors.
    """
        
    def calculate(self):
        """
        Calculate the Disagreement Measure between y1 and y2.

        Returns:
        float: Disagreement Measure.
        """
        
        if self.threshold is None:
            raise ValueError("Threshold must be specified")
        disagreement_count = np.sum(np.abs(self.y1 - self.y2) > self.threshold)

        return disagreement_count / len(self.y1)
