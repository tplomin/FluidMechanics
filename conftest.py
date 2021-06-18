import pytest

@pytest.fixture
def input_values():

    params = []
        
    for m in range(1,5):
        params.append((1.1,m+.3))
        params.append((1.4,m+.3))
        params.append((1.7,m+.3))

    return params
