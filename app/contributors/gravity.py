# Copyright © Loft Orbital Solutions Inc.

from app.contributor import Contributor
from app.coordinates import Coordinates


class UnidirectionalGravity(Contributor):
    """Unidirectional gravity contributor (i.e. 'weight').
    """
    def __init__(self, acceleration: float,
                 z_key: str, 
                 z_dot_key: str) -> None:
        super().__init__()
        self.acceleration = acceleration
        self.z_key = z_key
        self.z_dot_key = z_dot_key

    def declare_coordinates(self, coordinates: Coordinates) -> None:
        self.z_index: int = coordinates.register_coordinate(self.z_key)
        self.z_dot_index: int = coordinates.register_coordinate(self.z_dot_key)

    def declare_contributions(self, coordinates: Coordinates) -> None:
        coordinates.register_contribution(index=self.z_dot_index, value=self.acceleration)
