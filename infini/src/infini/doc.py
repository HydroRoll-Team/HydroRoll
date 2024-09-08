from typing import Dict, Optional, TypedDict

import json


class Annotation(TypedDict, total=False):
    usage: Optional[str]
    description: Optional[str]
    content: Optional[str]
    epilog: Optional[str]
    var_doc: Dict[str, str]
    sub_cmd: Dict[str, "Annotation"]


class Doc:
    pre_interceptors: Dict[str, Annotation]
    handlers: Dict[str, Annotation]
    events: Dict[str, Annotation]
    global_variables: Dict[str, Annotation]
    interceptors: Dict[str, Annotation]

    def __init__(self) -> None:
        self.pre_interceptors = {}
        self.handlers = {}
        self.events = {}
        self.global_variables = {}
        self.interceptors = {}

    def update(self, __object: "Doc") -> None:
        self.pre_interceptors.update(__object.pre_interceptors)
        self.handlers.update(__object.handlers)
        self.events.update(__object.events)
        self.global_variables.update(__object.global_variables)
        self.interceptors.update(__object.interceptors)

    def dumps(self) -> str:
        return json.dumps(
            {
                "pre_interceptors": self.pre_interceptors,
                "handlers": self.handlers,
                "events": self.events,
                "global_variables": self.global_variables,
                "interceptors": self.interceptors,
            }
        )
