import logging
logging.basicConfig(level=logging.INFO)


class Search:

    """given a text and a word, lookup the occurance of the word with start/end index
    
    parameter:
    serach_term -- string
    input_text -- string
    url -- if false only output searchterm and start/end string index
    exact_match -- if True (default) only looks for word, if False, lookup words that start with word
    case_sensitive -- if False, lowercase search_term
    
    sindex -- cursor moving along string index
    oindex -- start index of first occurance
    tindex -- cursor if exact_match == False to traverse word until boundary
    
    usage:
                word = "Bridge",
                text = "Bridges be Bridges."
                
                wb = False -> output: [("Bridges", 0, 6), ("Bridges", 11, 17)]
                wb = True  -> output: []
                
                wb = False, url = "http://here.com" -> output: ["http://here.com", ("Bridges", 0, 6), ("Bridges", 11, 17)]
                
    """

    sindex = 0  # cursor moving along string index
    oindex = 0  # start index of first occurance
    

    def __init__(self, search_term, input_text, url=False, exact_match=True, case_sensitive=True, logger=None):

        self.logger = logger or logging.getLogger(__name__)
        self.search_term = search_term
        self.input_text = input_text
        self.occurance = list()
        self.exact_match = exact_match
        self.case_sensitive = case_sensitive
        self._is_executed = False
        
        self._validate_input()
        self._is_sentence()

        if not case_sensitive:
            self.search_term = self.search_term.lower()
            self.input_text = self.input_text.lower()

        self.logger.info("search_term: {}".format(self.search_term))
        self.logger.info("input_text: {}".format(self.input_text))
        self.logger.info("exact_match: {}".format(self.exact_match))
        self.logger.info("case_sensitive: {}".format(self.case_sensitive))

        

    def __repr__(self):
        return """WordSearch(search_term="{search_term}", input_text="{input_text}", 
        is_executed={is_executed}, exact_match={exact_match}, case_sensitive={case_sensitive})""".format(
            search_term=self.search_term,
            input_text=self.input_text,
            is_executed=self._is_executed,
            exact_match=self.exact_match,
            case_sensitive=self.case_sensitive
        )

    def run(self):
        self.logger.info(
            "Searching for '{}' in input_text".format(self.search_term))
        if not self._is_executed:
            while self.oindex != -1:
                self.oindex = self.input_text[self.sindex:].find(
                    self.search_term)

                if self.exact_match:
                    self._traverse_input_exact_match()
                    self.sindex = self.sindex + \
                        len(self.search_term) + self.oindex

                else:
                    if self.oindex != -1:
                        self.ext_search_term = self.search_term
                        self._traverse_input()

                self.sindex = self.sindex + len(self.search_term) + self.oindex

        self.logger.info("Search completed")
        self.logger.info("Found: \n {}".format(self.occurance))
        self._is_executed = True
        

    def _traverse_input_exact_match(self):
        """traverse input_text string and append exact search_term matches to occurances
        """

        if (
            self.oindex != -1 and
            (
                self.input_text[self.oindex + len(self.search_term) + self.sindex] in " ." and
                self.oindex + len(self.search_term) +
                self.sindex < (len(self.input_text))
            )
        ):

            self.occurance.append(
                (
                    self.search_term,
                    self.oindex + self.sindex,
                    self.oindex + self.sindex + len(self.search_term) - 1
                )
            )

    def _traverse_input(self):
        """traverse input_text string and append terms matches to occurances
        that start with search_term but do not yet reach word boundary
        """
        
        self.tindex = 0  # cursor if exact_match == False to traverse word until boundary
        while (
            self.input_text[
                self.oindex +
                len(self.search_term) +
                self.sindex + self.tindex] != " "
            and self.oindex + len(self.search_term) +
            self.sindex + self.tindex < (len(self.input_text) - 1)
        ):

            self.tindex += 1
            self.ext_search_term = self.ext_search_term + self.input_text[
                self.oindex +
                len(self.search_term) +
                self.sindex - 1 + self.tindex
            ]  # increment self.oindex until word boundary

        self.occurance.append(
            (
                self.ext_search_term,
                self.oindex + self.sindex,
                self.oindex + self.sindex +
                len(self.search_term) + self.tindex - 1
            )
        )

    def _is_sentence(self):
        """append sentence delimiter
        """
        if self.input_text and self.input_text[-1] not in list("!?."):
            self.input_text = self.input_text + "."

    def _isin_text(self):
        """initial check if search_term is in input_text
        if not raise NotFound error
        """
        return self.search_term in self.input_text

    def _validate_input(self):
        """validate search_term and input_text input
        """

        if not isinstance(self.case_sensitive, bool):
            self.logger.error("case_sensitive is either True or False".format(
                type(self.search_term)
            ))
            raise ValueError(
                "case_sensitive is either True or False".format(
                    type(self.search_term)
                )
            )

        if not isinstance(self.exact_match, bool):
            self.logger.error("exact_match is either True or False".format(
                type(self.search_term)
            ))
            raise ValueError(
                "exact_match is either True or False".format(
                    type(self.search_term)
                )
            )
        

        if not isinstance(self.search_term, str):
            self.logger.error("Provide a search term as string: type {} invalid".format(
                type(self.search_term)
            ))
            raise ValueError(
                "Provide a search term as string: type {} invalid".format(
                    type(self.search_term)
                )
            )

        if not isinstance(self.input_text, str):
            self.logger.error("Provide an input text as string: type {} invalid".format(
                type(self.input_text)
            ))
            raise ValueError(
                "Provide an input text as string: type {} invalid".format(
                    type(self.input_text)
                )
            )

        if not all([self.search_term, self.input_text]):
            self.logger.error(
                "Provide a search term and input text as string"
            )
            raise ValueError("Provide a search term and input text as string")


        if not self._isin_text():
            self.logger.error("search_term: {} not in input_text: {}".format(
                self.search_term,
                self.input_text
            ))
            raise NotFoundError(
                "search_term: {} not in input_text: {}".format(
                    self.search_term,
                    self.input_text
                )
            )


class NotFoundError(Exception):
    """Custom exception to be raised if search_term is not in input_text
    """
    pass
    
