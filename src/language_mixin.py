class LanguageMixin:
    """
    Миксин для хранения и изменения языка клавиатуры.
    """
    SUPPORTED_LANGUAGES = {'EN', 'RU'}

    def __init__(self, *args, **kwargs):
        self._language = 'EN'
        super().__init__(*args, **kwargs)

    @property
    def language(self):
        """
        Возвращает текущий язык клавиатуры.
        """
        return self._language

    @language.setter
    def language(self, new_language):
        """
        Устанавливает язык клавиатуры.

        :param new_language: Новый язык клавиатуры.
        """
        if new_language in self.SUPPORTED_LANGUAGES:
            self._language = new_language
        else:
            raise ValueError(f"Unsupported language: {new_language}")

    def change_lang(self):
        """
        Изменяет язык клавиатуры на следующий.
        """
        if self._language == 'EN':
            self._language = 'RU'
        else:
            self._language = 'EN'
