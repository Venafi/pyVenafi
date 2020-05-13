from abc import abstractmethod


class GeneratorType:
    html = 'html'


class Generator:
    def __init__(self, generator_type: str):
        self._generator_type = generator_type

    def __str__(self):
        return self._generator_type

    def __repr__(self):
        return self._generator_type

    @abstractmethod
    def generate(self, log_file: str):
        pass
