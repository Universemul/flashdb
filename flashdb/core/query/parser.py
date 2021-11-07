from typing import List, Union, Any


class Lexer:

    @staticmethod
    def tokenize(query: Union[str, bytes], encoding: str = "utf-8") -> List[tuple[Token, Any]]:
        pass