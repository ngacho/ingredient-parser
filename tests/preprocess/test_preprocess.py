import pytest

from ingredient_parser import PreProcessor


@pytest.fixture
def p():
    """Define an empty PreProcessor object to use for testing the PreProcessor
    class methods.
    """
    return PreProcessor("", defer_pos_tagging=True)


class TestPreProcessor__builtins__:
    def test__str__(self):
        """
        Test PreProcessor __str__
        """
        p = PreProcessor("1/2 cup chicken broth")
        truth = """Pre-processed recipe ingredient sentence
\t    Input: 1/2 cup chicken broth
\t  Cleaned: 0.5 cup chicken broth
\tTokenized: ['0.5', 'cup', 'chicken', 'broth']"""
        assert str(p) == truth

    def test__repr__(self):
        """
        Test PreProessor __repr__
        """
        p = PreProcessor("1/2 cup chicken broth")
        assert repr(p) == 'PreProcessor("1/2 cup chicken broth")'


def normalise_test_cases() -> list[tuple[str]]:
    """
    Return a list of tuples of input sentences and their normalised form.
    Many of these examples are based on the examples in docstrings for the
    PreProcessor functions.
    """
    return [
        ("&frac12; cup warm water (105°F)", "0.5 cup warm water (105°F)"),
        ("3 1/2 chilis anchos", "3.5 chilis anchos"),
        ("six eggs", "6 eggs"),
        ("thumbnail-size piece ginger", "thumbnail-size piece ginger"),
        (
            "2 cups flour – white or self-raising",
            "2 cups flour - white or self-raising",
        ),
        ("3–4 sirloin steaks", "3-4 sirloin steaks"),
        ("three large onions", "3 large onions"),
        ("twelve bonbons", "12 bonbons"),
        ("1&frac34; cups tomato ketchup", "1.75 cups tomato ketchup"),
        ("1/2 cup icing sugar", "0.5 cup icing sugar"),
        ("2 3/4 pound chickpeas", "2.75 pound chickpeas"),
        ("1 and 1/2 tsp fine grain sea salt", "1.5 tsp fine grain sea salt"),
        ("1 and 1/4 cups dark chocolate morsels", "1.25 cups dark chocolate morsels"),
        ("½ cup icing sugar", "0.5 cup icing sugar"),
        ("3⅓ cups warm water", "3.333 cups warm water"),
        ("¼-½ teaspoon", "0.25-0.5 teaspoon"),
        ("100g green beans", "100 g green beans"),
        ("2-pound red peppers, sliced", "2 pound red peppers, sliced"),
        ("2lb1oz cherry tomatoes", "2 lb 1 oz cherry tomatoes"),
        ("2lb-1oz cherry tomatoes", "2 lb - 1 oz cherry tomatoes"),
        ("1 tsp. garlic powder", "1 tsp garlic powder"),
        ("5 oz. chopped tomatoes", "5 oz chopped tomatoes"),
        ("1 to 2 mashed bananas", "1-2 mashed bananas"),
        ("5- or 6- large apples", "5-6- large apples"),
        ("227 g - 283.5 g/8-10 oz duck breast", "227-283.5 g/8-10 oz duck breast"),
        ("400-500 g/14 oz - 17 oz rhubarb", "400-500 g/14-17 oz rhubarb"),
        ("8 x 450 g/1 lb live lobsters", "8x 450 g/1 lb live lobsters"),
        ("4 x 100 g wild salmon fillet", "4x 100 g wild salmon fillet"),
        (
            "½ - ¾ cup heavy cream, plus extra for brushing the tops of the scones",
            "0.5-0.75 cup heavy cream, plus extra for brushing the tops of the scones",
        ),
    ]


class TestPreProcessor_normalise:
    @pytest.mark.parametrize("testcase", normalise_test_cases())
    def test_normalise(self, testcase):
        """
        Test that each example sentence is normalised correctly
        """
        input_sentence, normalised = testcase
        p = PreProcessor(input_sentence, defer_pos_tagging=True)
        assert p.sentence == normalised
