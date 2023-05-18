# Copyright © Loft Orbital Solutions Inc.

import math

from app.contributor import Contributor
from app.coordinates import Coordinates


class ConstantCdAndAreaDrag(Contributor):
    """Constant drag coefficient (Cd) and cross sectional area.
    Kept two dimensional for simplicity purposes.
    """
    def __init__(self,
                 cd: float,
                 area: float,
                 x_key: str, 
                 y_key: str,
                 x_dot_key: str, 
                 y_dot_key: str,
                 mass_key: str,
                ) -> None:
        super().__init__()
        self.cd = cd
        self.area = area
        self.x_key = x_key
        self.y_key = y_key
        self.x_dot_key = x_dot_key
        self.y_dot_key = y_dot_key
        self.mass_key = mass_key

    def declare_coordinates(self, coordinates: Coordinates) -> None:
        self.x_index = coordinates.register_coordinate(self.x_key)
        self.x_dot_index = coordinates.register_coordinate(self.x_dot_key)
        self.y_index = coordinates.register_coordinate(self.y_key)
        self.y_dot_index = coordinates.register_coordinate(self.y_dot_key)
        self.mass_index = coordinates.register_coordinate(self.mass_key)

    def declare_contributions(self, coordinates: Coordinates) -> None:
        # I can obtain how high I am so that I can compute density
        y: float = coordinates.get_value(self.y_dot_index)

        # Dummy density computation (you can call a model here...)
        density: float = 1.225 * math.exp(y/8500)

        # Obtain the velocity vector and mass
        x_dot: float = coordinates.get_value(self.x_dot_index)
        y_dot: float = coordinates.get_value(self.y_dot_index)
        mass: float = coordinates.get_value(self.mass_index)

        # Work out the drag acceleration
        v2: float = math.pow(x_dot, 2) + math.pow(y_dot, 2)
        drag_acc: float = 0.5 * density * v2 * self.cd * self.area / mass
        
        # Work out drag acceleration components
        alpha: float = math.atan(y_dot/x_dot)
        x_dot_dot: float = -drag_acc * math.cos(alpha)
        y_dot_dot: float = -drag_acc * math.sin(alpha)

        coordinates.register_contribution(index=self.x_dot_index, value=x_dot_dot)
        coordinates.register_contribution(index=self.y_dot_index, value=y_dot_dot)
