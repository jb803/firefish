"""
Test writing of default thermophysical properties
"""
import os

import pytest

from firefish.case import (
    Case)
import firefish.fluids as fl

@pytest.fixture
def tmpcase(tmpdir):
    """An empty Case instance which has been created in a temporary directory.

    """
    from firefish.case import Case
    case_dir = tmpdir.join('temp_case')
    return Case(case_dir.strpath)

def test_dimensionless_air(tmpcase):
    """Tests dimensionless air writes to a file"""
    fl.write_thermophysical_properties(tmpcase,fl.Fluid.DIMENSIONLESS_AIR)
    dict_path = os.path.join(tmpcase.root_dir_path, 'constant', 'thermophysicalProperties')
    assert os.path.isfile(dict_path)


def test_dimensionless_air(tmpcase):
    """Tests dimensionless air writes to a file"""
    fl.write_thermophysical_properties(tmpcase,fl.Fluid.AIR)
    dict_path = os.path.join(tmpcase.root_dir_path, 'constant', 'thermophysicalProperties')
    assert os.path.isfile(dict_path)
