class MultipleSentencesError(ValueError):
    pass


class FirstLetterCaseError(ValueError):
    pass


class Sentence:
    MARKS_AT_END = ('...',  '!..', '?..', '?!.', '!?.', '?!', '!?', '?', '!', '.')
    OTHER_MARKS = (',', ';', ':', '"', '\'')
    MARK_CHARS = ('.', '?', '!', ',', ';', ':', '"', '\'')

    def __init__(self, sentence: str):
        self._sentence = sentence
        self.validate_sentence()
        self._index = 0
        self._sentence_without_marks = self.get_sentence_without_marks()

    def __iter__(self):
        return SentenceIterator(self._index, self._sentence_without_marks)

    def __repr__(self):
        return f'<{self.__class__.__name__}(words={len(self.words)}, other_chars={len(self.other_chars)})>'

    def __getitem__(self, key):
        if isinstance(key, int):
            return self.words[key]
        if isinstance(key, slice):
            return ' '.join(self.words[key])
        else:
            raise TypeError

    @property
    def words(self):
        return self._sentence_without_marks.split()

    @property
    def other_chars(self):
        return [char for char in self._sentence if char in Sentence.MARK_CHARS]

    def _words(self):
        return (word for word in self._sentence_without_marks.split())

    def validate_sentence(self):
        if not isinstance(self._sentence, str):
            raise TypeError('the sentence must be a string')

        if not self._sentence.endswith(Sentence.MARKS_AT_END):
            raise ValueError('the sentence is not completed')

        sentence_without_end_marks = self._sentence
        for char in Sentence.MARKS_AT_END:
            sentence_without_end_marks = sentence_without_end_marks.rstrip(char)
        if any(mark in sentence_without_end_marks for mark in Sentence.MARKS_AT_END):
            raise MultipleSentencesError('the sentence must be one')

        if not (self._sentence[0].isalpha() and self._sentence[0].isupper()):
            raise FirstLetterCaseError('the sentence must start with capital letter')

    def get_sentence_without_marks(self):
        sentence_without_marks = self.clear_duplicate_spaces(self._sentence)
        for mark in list(Sentence.MARKS_AT_END + Sentence.OTHER_MARKS):
            sentence_without_marks = sentence_without_marks.replace(mark, '')
        return sentence_without_marks

    @staticmethod
    def clear_duplicate_spaces(text):
        return " ".join(text.split())


class SentenceIterator:
    def __init__(self, index, sentence_without_marks):
        self._index = index
        self._sentence_without_marks = sentence_without_marks

    def get_word(self):
        if self._index == -1:
            raise StopIteration
        next_space_ind = self._sentence_without_marks.find(' ', self._index)
        if next_space_ind == -1:
            word = self._sentence_without_marks[self._index:]
            self._index = next_space_ind
        else:
            word = self._sentence_without_marks[self._index:next_space_ind]
            self._index = next_space_ind + 1
        return word

    def __next__(self):
        return self.get_word()

    def __iter__(self):
        return self
