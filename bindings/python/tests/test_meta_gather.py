import meta_gather as mg


def test_sum() -> None:
    sum = mg.sum_as_string(1, 2)
    assert "3" == sum
