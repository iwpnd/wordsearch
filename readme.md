### WordSearch

I wanted to see if I can write a small search algorithm without any external libraries to search for given search terms in an input text.

## installation

```
git clone https://github.com/iwpnd/wordsearch.git
cd wordsearch
pip install -e .
pytest tests/unit

```

## Usage

```python

from WordSearch import Search

input_text = 'Haters gonna hate'
search_term = 'Hate'

result = Search(search_term=search_term, input_text=input_text, exact_match=True, case_sensitive=True)
result.run()

>> []

result = Search(search_term=search_term, input_text=input_text, exact_match=False, case_sensitive=True)
result.run()

>> [('Haters', 0, 5)]

result = Search(search_term=search_term, input_text=input_text, exact_match=False, case_sensitive=False)
result.run()

>> [('haters', 0, 5), ('hate', 13, 16)]
```
