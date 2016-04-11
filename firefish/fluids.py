"""
This module provides shortcuts to commonly used fluids
"""

import enum

from firefish.case import (
    Case, FileName )

class Fluid(enum.enum):
    """An enumeration of commonly used fluids"""
    AIR = 0
    DIMENSIONLESS_AIR = 1

def write_thermophyiscal_properties(case, fluid):
    thermo_dict = None

    if (fluid == Fluid.AIR):

        
    elif (fuluid == Fluid.DIMENSIONLESS_AIR):
        thermo_dict = {
            'thermoType' : {'type' : 'hePsiThermo', 'mixture' : 'pureMixture',
                            'transport' : 'const', 'thermo'  : 'hConst',
                            'equationOfState' : 'perfectGas', 'specie' : 'specie',
                            'energy' : 'sensibleInternalEnergy'},
            'mixture' : {'specie' : {'nMoles' : 1, 'molWeight' : 11640.3},
                        'thermodynamics' : {'Cp' : 2.5, 'Hf' : 0},
                        'transport' : {'mu' : 0, 'Pr' : 1}}}

    with case.mutable_data_file(FileName.THERMOPHYSICAL_PROPERTIES) as d:
        d.upate(thermo_dict)