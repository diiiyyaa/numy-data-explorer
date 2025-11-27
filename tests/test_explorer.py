# tests/test_explorer.py
import numpy as np
from explorer import axis_statistics, reshape_array

def test_axis_stats():
    a = np.array([[1,2],[3,4]])
    stats = axis_statistics(a, axis=0)
    assert isinstance(stats['mean'], list)
    assert stats['sum'] == [4,6]

def test_reshape():
    a = np.arange(6)
    b = reshape_array(a, (2,3))
    assert b.shape == (2,3)
