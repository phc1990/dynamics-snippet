# Copyright © Loft Orbital Solutions Inc.

from abc import ABC, abstractclassmethod
from app.coordinates import Coordinates


class Contributor(ABC):
    """A contributor to the dynamic equations.
    """
    def __init__(self) -> None:
        super().__init__()

    @abstractclassmethod
    def declare_coordinates(self, coordinates: Coordinates) -> None:
        """Declares the coordinates of interest. This is only called ONCE
        for efficiency purposes.
        """
        pass

    @abstractclassmethod
    def declare_contributions(self, coordinates: Coordinates) -> None:
        """Computes and declares its contributions. This is called at EACH
        integration step.
        """
        pass
