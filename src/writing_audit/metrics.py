from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

from writing_audit.prose import extract_draft


@dataclass(frozen=True)
class Layer1Metrics:
    path: Path
    sentences: int
    words: int
    mean_sentence_length: float
    sentence_length_sd: float
    type_token_ratio: float

    def format(self) -> str:
        return (
            f"file: {self.path}\n"
            f"sentences: {self.sentences}\n"
            f"words: {self.words}\n"
            f"mean_sentence_length: {self.mean_sentence_length:.1f}\n"
            f"sentence_length_sd: {self.sentence_length_sd:.1f}\n"
            f"type_token_ratio: {self.type_token_ratio:.3f}"
        )


def _sentences(text: str) -> list[str]:
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [part.strip() for part in parts if part.strip()]


def compute_metrics(path: Path, text: str | None = None) -> Layer1Metrics:
    raw = text if text is not None else path.read_text()
    prose = extract_draft(raw)
    sents = _sentences(prose)
    lengths = [len(s.split()) for s in sents]
    n = len(lengths)
    mean = sum(lengths) / n if n else 0.0
    var = sum((length - mean) ** 2 for length in lengths) / n if n else 0.0
    tokens = re.findall(r"[A-Za-z']+", prose.lower())
    ttr = len(set(tokens)) / max(len(tokens), 1)
    return Layer1Metrics(
        path=path,
        sentences=n,
        words=sum(lengths),
        mean_sentence_length=mean,
        sentence_length_sd=var**0.5,
        type_token_ratio=ttr,
    )
