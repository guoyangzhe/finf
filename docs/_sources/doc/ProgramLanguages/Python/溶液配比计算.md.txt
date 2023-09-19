# 溶液配比计算
* created by: [scibro](https://blgxwk.me/)

* created at: 2023-04-24 20:00:00

* 将以下代码保存为`calc.py`，然后在命令行中运行`python calc.py`即可。

```python
# -*- coding: utf-8 -*-
def calculate_concentration(moles=None, mass=None, volume=None, molar_mass=None):
    """
    Calculate the missing parameter for a solution given any three of the following parameters:
    moles, mass, volume, molar_mass

    Args:
        moles (float): Number of moles of solute is mol/L(M)
        mass (float): Mass of solute in grams (mg)
        volume (float): Volume of solution in liters (mL)
        molar_mass (float): Molar mass of solute in grams per mole  (g/mol)

    Returns:
        float: The missing parameter
    """
    if moles is not None and mass is not None and volume is not None:
        # Calculate molarity
        return mass / (volume * moles)  # Convert from liters to milliliters
    elif moles is not None and mass is not None and molar_mass is not None:
        # Calculate volume
        return mass / (molar_mass * moles)  # Convert from milliliters to liters
    elif mass is not None and volume is not None and molar_mass is not None:
        # Calculate moles
        return mass / (volume * molar_mass)
    elif moles is not None and volume is not None and molar_mass is not None:
        # Calculate mass
        return moles * molar_mass * volume
    else:
        raise ValueError("Exactly three arguments must be provided.")

#==========================================
molar_mass = input("please input MW(g/mol): ")
if molar_mass == "":
    molar_mass = None
else:
    molar_mass = float(molar_mass)
mass = input("please input mass_g(mg): ")
if mass == "":
    mass = None
else:
    mass = float(mass)
moles = input("please input M(mol/L): ")
if moles == "":
    moles = None
else:
    moles = float(moles)
volume = input("please input V(mL): ")
if volume == "":
    volume = None
else:
    volume = float(volume)

if mass is not None and moles is not None and volume is not None:
    # Calculate molarity given moles, mass, and volume
    MW = calculate_concentration(moles=moles, mass=mass, volume=volume)
    print('MW =', "{:.2f}".format(MW), 'g/mol')
elif moles is not None and volume is not None and molar_mass is not None:
    # Calculate mass given molarity, volume, and molar mass
    mass_g = calculate_concentration(moles=moles, volume=volume, molar_mass=molar_mass)
    print('mass =', "{:.5f}".format(mass_g), 'mg')
elif mass is not None and volume is not None and molar_mass is not None:
    # Calculate moles given mass, volume, and molar mass
    M = calculate_concentration(mass=mass, volume=volume, molar_mass=molar_mass)
    print('M =', "%.0e" % M, 'M(mol/L)')
elif moles is not None and mass is not None and molar_mass is not None:
    # Calculate volume given moles, mass, and molarity
    V = calculate_concentration(moles=moles, mass=mass, molar_mass=molar_mass)
    print('V =', "{:.0f}".format(V), 'mL')
else:
    raise ValueError("Exactly three arguments must be provided.")
```
