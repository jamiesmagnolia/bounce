# Notes
Because I forget things (unfortunately).

## Pymunk
Pymunk is a physics library (?). It quite literally helps visualise physics simulation in python.

- In pymunk, you can create **physics objects** by combining **bodies** and **shapes**.
    - Physics Object = Body + Shape

- These work together to simulate real life physics. 
- **Body**: representation of physical properties of an object.
    - Properties:
        1. Mass: how heavy
        2. Position: location/coordinates (x, y)
            - (0, 0) or origin is bottom left of window
            - x-axis: increases from left->right
            - y-axis: increases from down->up
        3. Velocity: how fast AND which direction it moves

    - **Think**: body as the container for the phys.-related data. It's **not** the actual shape. This is what Shape is for.

    - Types of Bodies:
        1. Static: e.g. floor
        2. Dynamic: e.g. bouncing ball

- **Shape**: this defines the geometry (hence, name).
    - Examples:
        1. Circle (specify radius)
        2. Segment (a line between 2 points **a** and **b**)
            - Parameters:
                - radius: 
                    - Thickness of line
                    - Why named radius? Because phys. engines like Pymunk think of lines as a line with rounded edges (a capsule-like shape)

        3. Polygon (define shape via **list of vertices**/location of vertices)
        4. Etc.
    - Elasticity: bounciness, springiness
    - Friction: how much resistance an object experience when sliding on surfaces (it's just like IRL physics...)

- **Body AND Shape**:
    - Shape is attached to Body.
    - Shape handles geometry.
    - Body handles physics.

- **Moment**: 
    - Moment of inertia (or just moment).
    - Measure of object's **resistance to rotational motion**.
    - Determines how hard it is to rotate the object around its center.

## Pyglet