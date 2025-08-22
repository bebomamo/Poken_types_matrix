Hello,

This tool was developed to help new pokemon players (competitive or not) learn type advantages/disadvantages
without needing to mully through a chart and find type weaknesses/strengths. 

All you do to use it is click on the left side type buttons to select the type of the defending pokemon.
Then the right side types will either:
    - stay transparently bordered (neutral type effectiveness), 
    - get a dark red border (defending type is 2x weak to this type),
    - get a bright red border (defending type is 4x weak to this type),
    - get a dark green border (defending type is 2x strong to this type),
    - get a bright green border (defending type is 4x strong to this type),
    - get a white border (defending type is immune to this type)
Then once you understand that pokemon's type matchups or want to check a different pokemons typing effectiveness,
simply unselect the types that are selected by clicking them as well- and move on to the new types.

Packages and versions:
This tool uses python=3.11, customtkinter(ui package), numpy(math package), and pillow(image package).
Python 3.11 can be installed very easily from the command line with...

    winget install --id Python.Python.3.11 -e

    then check if the install was successful...

    python --version

The 3 packages can then be installed by:

    pip install [insert the package name(customtkinter, numpy, pillow)]

