# Notes
Because I forget things (unfortunately).

## Pymunk
- In pymunk, you can create **physics objects** by combining **bodies** and **shapes**.
    - Physics Object = Body + Shape

- These work together to simulate real life physics. 
- **Body**: representation of physical properties of an object.
    - Properties:
        1. Mass: how heavy
        2. Position: location (x, y)
        3. Velocity: how fast AND which direction it moves

    - **Think**: body as the container for the phys.-related data. It's **not** the actual shape. This is what Shape is for.

    - Types of Bodies:
        1. Static: e.g. floor
        2. Dynamic: e.g. bouncing ball

- **Shape**: this defines the geometry (hence, name).
    - Examples:
        1. Circle
        2. Segment
        3. Polygon
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