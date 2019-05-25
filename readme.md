### WordSearch

I wanted to see if I can write a small search algorithm without any external libraries to search for given search terms in an input text.

## installation

```
git clone https://github.com/iwpnd/wordsearch.git
cd wordsearch
pip install -e .
```

## Usage

```python

from WordSearch import WordSearch

input_text = 'Haters gonna hate'
search_term = 'Hate'

result = WordSearch(search_term=search_term, input_text=input_text, exact_match=True, case_sensitive=True)
result.run()

>> []

result = WordSearch(search_term=search_term, input_text=input_text, exact_match=False, case_sensitive=True)
result.run()

>> [('Haters', 0, 5)]

result = WordSearch(search_term=search_term, input_text=input_text, exact_match=False, case_sensitive=False)
result.run()

>> [('haters', 0, 5), ('hate', 13, 16)]
```

TO-DO: 
- tests
- exact_match=False, case_sensitive=False IndexError