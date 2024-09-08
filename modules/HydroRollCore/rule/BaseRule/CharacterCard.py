from dataclasses import dataclass


@dataclass
class Custom(object):
    """Docstring for Custom."""

    property: type


class Attribute(Custom): ...


class Skill(Custom): ...


class Information(Custom): ...
