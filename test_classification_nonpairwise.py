import unittest
from diversity_metrics.classification.NonPairwise.Non_pairwise_metrics import Entropy, KohaviWolpertVariance


predictions= ([1, 0, 1, 0],
              [1, 1, 0, 0],
              [1, 0, 0, 1],
              )

y_true = [1, 0, 1, 1]

def test_entropy():
    entropy_metric = Entropy(predictions=predictions, y_true=y_true)
    results = entropy_metric.calculate()
    print("Entropy :", results)

def test_KohaviWolpertVariance():
    KW_metric = KohaviWolpertVariance(predictions=predictions, y_true=y_true)
    results = KW_metric.calculate()
    print("KohaviWolpertVariance :", results)

test_KohaviWolpertVariance()
    
