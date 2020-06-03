#!/usr/bin/python3
class MyInt(int):
    """Module for class MyInt"""

    def __eq__(self, other):
        """Swap == with !=

        Args:
            other: object to compare

        Returns: True if value and self are differents
                False in otherwise
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """Swap != with ==

        Args:
            other: object to compare

        Returns: False if value and self are iqual
                True in otherwise
        """
        return super().__eq__(other)
