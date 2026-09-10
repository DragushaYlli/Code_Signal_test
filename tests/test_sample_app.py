import unittest

from sample_app import delivery_progress, risk_label


class DeliveryProgressTests(unittest.TestCase):
    def test_returns_percentage(self) -> None:
        self.assertEqual(delivery_progress(3, 4), 75.0)

    def test_rejects_empty_plan(self) -> None:
        with self.assertRaises(ValueError):
            delivery_progress(0, 0)

    def test_rejects_completed_count_above_total(self) -> None:
        with self.assertRaises(ValueError):
            delivery_progress(5, 4)


class RiskLabelTests(unittest.TestCase):
    def test_maps_each_risk_band(self) -> None:
        self.assertEqual(risk_label(20), "LOW")
        self.assertEqual(risk_label(50), "MEDIUM")
        self.assertEqual(risk_label(80), "HIGH")

    def test_rejects_score_outside_range(self) -> None:
        with self.assertRaises(ValueError):
            risk_label(101)


if __name__ == "__main__":
    unittest.main()
