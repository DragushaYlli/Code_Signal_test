import unittest

from sample_app import delivery_progress


class DeliveryProgressTests(unittest.TestCase):
    def test_returns_percentage(self) -> None:
        self.assertEqual(delivery_progress(3, 4), 75.0)

    def test_rejects_empty_plan(self) -> None:
        with self.assertRaises(ValueError):
            delivery_progress(0, 0)

    def test_rejects_completed_count_above_total(self) -> None:
        with self.assertRaises(ValueError):
            delivery_progress(5, 4)


if __name__ == "__main__":
    unittest.main()
