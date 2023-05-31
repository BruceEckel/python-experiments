# From https://yukinarit.github.io/pyserde/guide/getting-started.html
from dataclasses import dataclass
from serde import serde
from serde.json import from_json, to_json

@serde
@dataclass
class Foo:
    i: int
    s: str
    f: float
    b: bool


f = Foo(i=10, s='foo', f=100.0, b=True)
fj = to_json(f)
print(fj)
print(from_json(Foo, fj))

s = '{"i": 11, "s": "bar", "f": 200.0, "b": false}'
print(s)
print(from_json(Foo, s))
