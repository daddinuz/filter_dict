import typing

import chainable_iterator

K = typing.TypeVar('K')
V = typing.TypeVar('V')
P = typing.List[K]
Predicate = typing.Callable[[P, K, V], bool]
_Node = typing.NamedTuple('_Node', (('path', P), ('data', typing.Mapping)))


def _match_all(_kp: P, _k: K, _v: V) -> bool:
    return True


def _decompose_dict(the_dict: typing.Mapping[K, V], predicate: Predicate = _match_all) \
        -> typing.Generator[typing.Tuple[P, V], None, None]:
    root = chainable_iterator.ChainableIterator((_Node([], the_dict),))
    for node in root:
        path = node.path
        for k, v in node.data.items():
            path.append(k)
            if isinstance(v, dict):
                root.chain((_Node(path, v),))
            if predicate(path, k, v):
                yield path, v
            path = path[:-1]


def _recompose_dict(items: typing.Iterator[typing.Tuple[P, V]]) -> typing.Mapping[K, V]:
    the_dict = {}
    for path, value in items:
        base, last = the_dict, len(path) - 1
        for i, key in enumerate(path):
            base = base.setdefault(key, {} if i < last else value)
    return the_dict


def filter_dict(the_dict: typing.Mapping[K, V], predicate: Predicate = _match_all) -> typing.Mapping[K, V]:
    return _recompose_dict(_decompose_dict(the_dict, predicate))
