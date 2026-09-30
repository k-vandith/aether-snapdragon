"""Shared agent contract — identical on NPU and on a development reasoner."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
import json


@dataclass
class ActionItem:
    owner: str
    task: str
    due: str


@dataclass
class Brief:
    title: str
    summary: str
    decisions: list[str] = field(default_factory=list)
    actions: list[ActionItem] = field(default_factory=list)
    risks: list[str] = field(default_factory=list)
    followups: list[str] = field(default_factory=list)
    email_draft: str = ""
    answer: str = ""

    def to_json(self) -> str:
        payload = asdict(self)
        return json.dumps(payload, indent=2, ensure_ascii=False)
