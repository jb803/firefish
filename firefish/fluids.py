"""
This module provides shortcuts to commonly used fluids
"""

import enum

from firefish.case import (
    Case, FileName )

class Fluid(enum.Enum):
    """An enumeration of commonly used fluids"""
    AIR = 0
    DIMENSIONLESS_AIR = 1

def write_thermophysical_properties(case, fluid):
    thermo_dict = None

    if (fluid == Fluid.AIR):
        thermo_dict = {
            'thermoType' : {'type' : 'hePsiThermo', 'mixture' : 'pureMixture',
                            'transport' : 'const', 'thermo'  : 'hConst',
                            'equationOfState' : 'perfectGas', 'specie' : 'specie',
                            'energy' : 'sensibleInternalEnergy'},
            'mixture' : {'specie' : {'nMoles' : 1, 'molWeight' : 28.96},
                        'thermodynamics' : {'Cp' : 1004.5, 'Hf' : 2.544e+06},
                        'transport' : {'mu' : 0, 'Pr' : 1}}} 
    elif (fluid == Fluid.DIMENSIONLESS_AIR):
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
