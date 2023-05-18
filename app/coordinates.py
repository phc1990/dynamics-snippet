# Copyright © Loft Orbital Solutions Inc.


class Coordinates:
    """This class acts as a 'broker' so that different 'contributors' do 
    not need to know about the problem formulation (e.g. number of coordinates).
    """
    def __init__(self) -> None:
        self._keys: list[str] = []
        self._x: list[float] = []
        self._x_dot: list[float] = []

    def register_coordinate(self, key: str) -> int:
        """Registers a new coordinate, returning its corresponding index.
        It will not be added if another contributor has registerd it already.
        """
        try:
            return self._keys.index(key)
        except ValueError:
            self._keys.append(key)
            return len(self._keys)-1

    def get_value(self, index: int) -> float:
        """Returns the value of a specific coordinate. This is to be used
        during the integration step."""
        return self._x[index]

    def get_index(self, key: str) -> int:
        """Returns the index of a specific coordinate
        """
        return self._keys.index(key)

    def register_contribution(self, index: int, value: float) -> None:
        """Register a contribution to the state derivative. This is to be
        called at each integration step."""
        self._x_dot[index] += value

    def set_x_and_x_dot(self, x: list[float], x_dot: list[float]) -> None:
        """Resets the state and its derivative."""
        self._x = x
        self._x_dot = x_dot

    def size(self) -> int:
        """Returns the number of coordinates."""
        return len(self._keys)
    