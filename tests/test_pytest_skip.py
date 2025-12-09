import pytest


@pytest.mark.skip(reason="Фича в разработке")  # Указываем маркировку, которая пропустит данный автотест
def test_feature_in_development():
    pass


@pytest.mark.skip(reason="Фича в разработке")
class TestSuiteSkip:
    def feature_in_development_1(selfs):
        ...

    def feature_in_development_2(selfs):
        ...
