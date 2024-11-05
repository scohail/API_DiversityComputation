from diversity_metrics.regression.Nonpairwise_metrics import VarianceOutputs, Ambiguity, VariationCoefficient, DiversityDensity, ErrorVariance
import numpy as np

predictions= ([4.0, 5.4, 7.1, 3.8],
              [5.7, 5.5, 3.1, 9.8],
              [3.0, 2.0, 4.1, 3.8]
              )

y_true = [4.0, 5.4, 7.1, 3.8]

def test_variances_of_output():
    variancemetric = VarianceOutputs(predictions=predictions)
    results = variancemetric.calculate()
    print("variancemetric :", results)

def test_ambiguity_metric():
    ambiguity = Ambiguity(predictions=predictions)
    results = ambiguity.calculate()
    print("Amiguity :",results)

def test_variation_coefficient():
    Variation = VariationCoefficient(predictions=predictions)
    results = Variation.calculate()
    print("Variation Coefficient :",results)
def test_diversity_density():
    diversity = DiversityDensity(predictions=predictions)
    results = diversity.calculate()
    print("Diversity Density :",results)

def test_error_variance():
    errorvariance = ErrorVariance(predictions=predictions, y_true=y_true)
    results = errorvariance.calculate()
    print("Error Variance :",results)


test_error_variance()
