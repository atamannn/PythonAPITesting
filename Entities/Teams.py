from dataclasses import dataclass
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class Meta:
    version: str
    status: str
    copywrite: str


@dataclass_json
@dataclass
class Teams:
    meta : Meta
    body : str