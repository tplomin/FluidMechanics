from conftest import input_values
import pytest
import shocks
import numpy as np

def test_idealGas():
    """
    Test the ideal gas law
    """
    assert shocks.idealGas(287,P=101325, T=298.15) == 101325 / (287 * 298.15)

def test_speedOfSound():
    assert shocks.speedOfSound(1.4, 287, 298.15) == np.sqrt(1.4* 287* 298.15)

@pytest.mark.parametrize("gamma, m1", input_values)
def test_m2_normal(gamma, m1):
    assert shocks.m2(gamma, m1) < m1
