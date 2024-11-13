# diversity_metrics/classification/__init__.py
from .NonPairwise_base_metric import NonPairwiseClassificationMetric
import numpy as np




class Entropy(NonPairwiseClassificationMetric):
    """
    Calculate the entropy of the ensemble predictions for a classification task.
    """
    def calculate(self):
        """
        Calculate the Entropy metric for multiple classifiers.

        Returns:
        float: The entropy value.
        """
        N = len(self.predictions[0])
        L = len(self.predictions)
        entropy_sum = 0

    
        

        for i in range(N):
            sum_Yj = sum(1 if self.predictions[j][i] == self.y_true[i] else 0 for j in range(L))
            entropy_sum += min(sum_Yj, L - sum_Yj)
            print("Entropy sum: ", entropy_sum)

        entropy = (1 / N) * (2 /( L - 1)) * entropy_sum
        return entropy



class  KohaviWolpertVariance(NonPairwiseClassificationMetric):
    """
    measure the diversity of a compound set for binary classifiers.
    """
    def calculate(self):
        """
        Calculate the Kohavi-Wolpert Variance metric for multiple classifiers.

        Returns:
        float: The Kohavi-Wolpert Variance value.
        """
        N = len(self.predictions[0])
        L = len(self.predictions)
        
        variance_sum = 0

        for i in range(N):
            sum_Yj = sum(1 if self.predictions[j][i] == self.y_true[i] else 0 for j in range(L))
            variance_sum += (sum_Yj * (L - sum_Yj)) 

        KW =  (1 / (N * L**2))* variance_sum 

        return KW
    
