import unittest

import cpyfunctional


class TestCompose(unittest.TestCase):
    """
    Test compose function able to execute callable one by one an return result from all of them.
    """

    def test_able_to_compose_multiple_callable(self):
        """
        compose given multiple callable, able to return value from them.
        """
        result = cpyfunctional.compose(lambda number: number + 1, lambda number: number ** 2)(3)
        self.assertEqual(result, 10)

    def test_unable_to_accept_function(self):
        """
        compose can not accept function directly.
        """
        def add(number: int, prev_number: int) -> int:
            return number + prev_number # pragma: no cover

        with self.assertRaises(TypeError):
            cpyfunctional.compose(add(10), lambda number: number ** 2)(3)
