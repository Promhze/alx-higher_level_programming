#!/usr/bin/python3
"""Create a rebel class from int"""


class MyInt(int):
    """A class inheriting from int
    and inverting signs."""

    def __eq__(self, other):
        """Equality becomes inequality"""

        return super().__ne__(other)

    def __ne__(self, other):
        """Inequality becomees Eequality"""

        return super().__eq__(other)
