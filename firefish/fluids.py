"""
This module provides shortcuts to commonly used fluids
"""

import enum

from firefish.case import (
    FileName)

class Fluid(enum.Enum):
    """
    An enumeration of commonly used fluids

    AIR generates the recommended OpenFoam thermophysicalProperties for air.

    DIMENSIONLESS_AIR generates a normalised gas whith gamma=7/5 and with
    the property that at 1 temperature unit the speed of sound is 1
    velocity unit"""
    AIR = 0
    DIMENSIONLESS_AIR = 1

def write_thermophysical_properties(case, fluid):
    """"
    Writes a thermophysicalProperties dict in the given case for the
    specified fluid.

    Args:
        case (firefish.case.Case): the case in which to write the dict
        fluid (firefish.fluids.Fluid): the fluid to use
    """

    thermo_dict = None

    if fluid == Fluid.AIR:
        thermo_dict = {
            'thermoType' : {'type' : 'hePsiThermo', 'mixture' : 'pureMixture',
                            'transport' : 'const', 'thermo'  : 'hConst',
                            'equationOfState' : 'perfectGas', 'specie' : 'specie',
                            'energy' : 'sensibleInternalEnergy'},
            'mixture' : {'specie' : {'nMoles' : 1, 'molWeight' : 28.96},
                         'thermodynamics' : {'Cp' : 1004.5, 'Hf' : 2.544e+06},
                         'transport' : {'mu' : 0, 'Pr' : 1}}}
    elif fluid == Fluid.DIMENSIONLESS_AIR:
        thermo_dict = {
            'thermoType' : {'type' : 'hePsiThermo', 'mixture' : 'pureMixture',
                            'transport' : 'const', 'thermo'  : 'hConst',
                            'equationOfState' : 'perfectGas', 'specie' : 'specie',
                            'energy' : 'sensibleInternalEnergy'},
            'mixture' : {'specie' : {'nMoles' : 1, 'molWeight' : 11640.3},
                         'thermodynamics' : {'Cp' : 2.5, 'Hf' : 0},
                         'transport' : {'mu' : 0, 'Pr' : 1}}}

    with case.mutable_data_file(FileName.THERMOPHYSICAL_PROPERTIES) as d:
        d.update(thermo_dict)
