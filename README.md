Filter Dict
===========

Filtering dicts, the easy way!

```python
from pprint import pprint
from filter_dict import filter_dict

if __name__ == '__main__':
    pprint(filter_dict(lambda p, k, v: k == 'O' or v == 1, {
            'a': {
                'A': {
                    'x': 1
                },
                'O': {
                    'a': 5
                }
            },
            'b': {
                'B': {
                    'y': 2
                },
                'O': {
                    'b': 5
                }
            }
        }))
```

the result is:

```
{
  "a": {
    "O": {
      "a": 5
    },
    "A": {
      "x": 1
    }
  },
  "b": {
    "O": {
      "b": 5
    }
  }
}
```
