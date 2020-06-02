#!/usr/bin/python3
class MyInt(int):
    """Module for class MyInt"""

    def __eq__(self, value):
        """Swap == with !=

        Args:
            value: object to compare

        Returns: True if value and self are differents
                False in otherwise
        """
        return super().__ne__(value)

    def __ne__(self, value):
        """Swap != with ==
        Args:
            value: object to compare

        Returns: False if value and self are iqual
                True in otherwise
        """
        return super().__eq__(value)
