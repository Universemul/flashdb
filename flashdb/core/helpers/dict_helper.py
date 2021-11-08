from typing import Dict


def with_upper_keys(dictionary: Dict) -> Dict:
    return dict((k, v.upper()) for k, v in dictionary.items())


def with_lower_keys(dictionary: Dict) -> Dict:
    return dict((k.lower(), v) for k, v in dictionary.items())
