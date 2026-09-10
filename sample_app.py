"""Tiny deterministic module used by the Code Signal webhook test repository."""


def delivery_progress(completed_items: int, total_items: int) -> float:
    """Return completion percentage for a non-empty delivery plan."""

    if total_items <= 0:
        raise ValueError("total_items must be greater than zero")
    if completed_items < 0 or completed_items > total_items:
        raise ValueError("completed_items must be between zero and total_items")
    return round((completed_items / total_items) * 100, 2)


def risk_label(score: float) -> str:
    """Map a zero-to-one-hundred risk score to a simple test label."""

    if not 0 <= score <= 100:
        raise ValueError("score must be between zero and one hundred")
    if score <= 34:
        return "LOW"
    if score <= 64:
        return "MEDIUM"
    return "HIGH"
