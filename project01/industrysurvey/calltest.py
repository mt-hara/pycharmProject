import typing
import dataclasses

@dataclasses.dataclass
class MyConfig:
    foo : int
    bar : float
    baz : typing.List[str]

config = MyConfig(foo = 1, bar=2.0, baz = ["3 and 4"])

print(config.foo)