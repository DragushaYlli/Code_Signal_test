"""Tiny deterministic module used by the Code Signal webhook test repository."""


def delivery_progress(completed_items: int, total_items: int) -> float:
    """Return completion percentage for a non-empty delivery plan."""

    if total_items <= 0:
        raise ValueError("total_items must be greater than zero")
    if completed_items < 0 or completed_items > total_items:
        raise ValueError("completed_items must be between zero and total_items")
    return round((completed_items / total_items) * 100, 2)
