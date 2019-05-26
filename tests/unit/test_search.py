import pytest
from WordSearch import Search, NotFoundError

input_text = 'Haters gonna hate until they dont. Hate just does that.'
search_term = 'Hate'


def test_search_exact_case_sensitive():
    result = Search(
        search_term=search_term,
        input_text=input_text,
        exact_match=True,
        case_sensitive=True
    )
    result.run()

    assert result.occurance == [('Hate', 35, 38)]

def test_search_notexact_case_sensitive():
    result = Search(
        search_term=search_term,
        input_text=input_text,
        exact_match=False,
        case_sensitive=True
    )
    result.run()

    assert result.occurance == [('Haters', 0, 5), ('Hate', 35, 38)]

def test_search_exact_not_case_sensitive():
    result = Search(
        search_term=search_term,
        input_text=input_text,
        exact_match=True,
        case_sensitive=False
    )
    result.run()

    assert result.occurance == [('hate', 13, 16), ('hate', 35, 38)]


def test_search_not_exact_not_case_sensitive():
    result = Search(
        search_term=search_term,
        input_text=input_text,
        exact_match=False,
        case_sensitive=False
    )
    result.run()

    assert result.occurance == [
        ('haters', 0, 5), ('hate', 13, 16), ('hate', 35, 38)]
