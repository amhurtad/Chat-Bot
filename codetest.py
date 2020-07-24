import pytest


from module.mymodule import make_dict
from module.mymodule import selection_genre_and_cuisine
from module.mymodule import remove_punctuation


planner_day = ["monday", "tuesday", "wednesday" ]

planner_activity = ["Piatti", "Frozen 2", "Bonchon"]

def test_message():
    
    assert make_dict("Here are your plans: ") == "Here are your plans: {'monday': 'Piatti', 'wednesday': 'Frozen 2', 'friday': 'Bonchon'}

    
def test_selection_genre_and_cuisine():
    
    assert selection_genre_and_cuisine("hello", ["hello", "hi", "bye"], {"hello":"alexa", "hi":"ashley", "bye":"sofia"}, "oh my goodness") == "oh my goodness hello: alexa"
    
    assert selection_genre_and_cuisine("colors", ["colors", "cars", "food"], {"colors":"red", "cars":"truck", "food":"pizza"}, "here are") == "here are colors: red"