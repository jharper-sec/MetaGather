import meta_gather as mg


def test_hello() -> None:
    hello = mg.hello()
    assert hello == "Hello from meta-gather!"
