# Copyright © Loft Orbital Solutions Inc.

from app.contributor import Contributor
from app.coordinates import Coordinates


class Dynamics:
    """This class represents system dynamics."""
    def __init__(self) -> None:
        self.coordinates: Coordinates = Coordinates()
        self.contributors: list[Contributor] = []

    def add_contributor(self, contributor: Contributor) -> None:
        """Adds a contributor to the dynamics system."""
        contributor.declare_coordinates(self.coordinates)
        self.contributors.append(contributor)

    def get_dynamics_equation(self, x: list[float], x_dot: list[float]) -> None:
        """Computes the dynamic equations"""
        self.coordinates.set_x_and_x_dot(x=x, x_dot=x_dot)
        for contributor in self.contributors:
            contributor.declare_contributions(coordinates=self.coordinates)
    
    