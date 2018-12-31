import unittest

import cpyfunctional


class TestPipe(unittest.TestCase):
    """
    Test pipe function able to execute callable one by one an return result from all of them.
    """

    def test_able_to_pipe_multiple_callable(self):
        """
        pipe given multiple callable, able to return value from them.
        """
        result = cpyfunctional.pipe(lambda number: number + 1, lambda number: number ** 2)(3)
        self.assertEqual(result, 16)

    def test_unable_to_accept_function(self):
        """
        pipe can not accept function directly.
        """
        def add(number: int, prev_number: int) -> int:
            return number + prev_number # pragma: no cover

        with self.assertRaises(TypeError):
            cpyfunctional.pipe(add(10), lambda number: number ** 2)(3)
