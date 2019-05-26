import pytest
from WordSearch import Search, NotFoundError

input_text = 'Haters gonna hate until they dont. Hate just does that.'
search_term = 'Hate'

def test_input_validation():
    with pytest.raises(ValueError):
        result = Search(
            search_term = 1,
            input_text = input_text
        )

    with pytest.raises(ValueError):
        result = Search(
            search_term=1,
            input_text=1
        )
    
    with pytest.raises(ValueError):
        result = Search(
            search_term=search_term,
            input_text=1
        )

    with pytest.raises(ValueError):
        result = Search(
            search_term=None,
            input_text=None
        )

    with pytest.raises(ValueError):
        result = Search(
            search_term=search_term,
            input_text=input_text,
            case_sensitive=1,
        )

    with pytest.raises(ValueError):
        result = Search(
            search_term=search_term,
            input_text=input_text,
            exact_match=1,
        )

def test_searchterm_notfound():
    with pytest.raises(NotFoundError):
        result = Search(
            search_term='Love',
            input_text=input_text
        )


