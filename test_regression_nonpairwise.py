from diversity_metrics.regression.Nonpairwise_metrics import VarianceOutputs


predictions= ([4.0, 5.0, 7.1, 3.8],
              [4.0, 8.4, 3.1, 9.8],
              [4.0, 5.7, 4.1, 3.8]
              )

def test_variances_of_output():
    variancemetric = VarianceOutputs(predictions=predictions)
    results = variancemetric.calculate()
    print("variancemetric :", results)


test_variances_of_output()