"""Intentional branch-only failure used to exercise Pipeline Health."""

import unittest


class ExpectedPipelineFailure(unittest.TestCase):
    def test_pipeline_reports_a_failure(self) -> None:
        self.assertEqual("healthy", "failing-test-branch")


if __name__ == "__main__":
    unittest.main()
