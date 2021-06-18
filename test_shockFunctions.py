import pytest
import shocks

def test_idealGas():
    assert shocks.idealGas(287,P=101325, T=298.15) == 101325 / (287 * 298.15)
