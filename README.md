# vis3dvf

<p align="center">
  <img src="https://github.com/LukasDrsman/vis3dvf/blob/main/assets/screenshot.png" width="800">
</p>

## Dependencies
 - `pygame`
 - `PyOpenGL`
 - `PyOpenGL_accelerate`

To install the necessary dependencies, use:
```sh
pip install pygame PyOpenGl PyOpenGL_accelerate
```

## Quickstart
A simple example of a time-dependent vector field can be found in the `example.py` file. To quickstart this example, run:
```sh
pip install pygame PyOpenGl PyOpenGL_accelerate

git clone https://github.com/LukasDrsman/vis3dvf.git
cd vis3dvf
python3 example.py
```

## Usage
### *plot*.Figure(window width, window height)
 - Figure constructor, necessary for rendering.
 - "Public" methods:
   - **add**(*plot*) - adds *plot* object to the render que (*plot* object must have an implemented **render**() method)
   - **show**() - creates a window and starts rendering

### *vectorfield*.VectorField(u, v, w, density)
 - Static vector field plot object constructor
 - Parameters:
   - u = **u**(x,y,z) - the x component of the vector field at (x,y,z) (function)
   - v = **v**(x,y,z) - the y component of the vector field at (x,y,z) (function)
   - w = **w**(x,y,z) - the z component of the vector field at (x,y,z) (function)


### *vectorfield*.VectorFieldT(u, v, w, density, initial time, final time, time delta)
 - Time-dependent vector field plot object constructor
 - Parameters:
   - u = **u**(x,y,z,t) - the x component of the vector field at (x,y,z) and time t (function)
   - v = **v**(x,y,z,t) - the y component of the vector field at (x,y,z) and time t (function)
   - w = **w**(x,y,z,t) - the z component of the vector field at (x,y,z) and time t (function)
