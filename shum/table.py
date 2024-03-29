"""
Load utterances from wandb.Table in a wandb.Artifact created by uk.share
https://github.com/proger/uk/blob/main/uk/share.py
"""

from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Iterable
import json

import wandb


@dataclass
class Downloadable:
    x: Path
    def download(self):
        return str(self.x)


@dataclass
class StubArtifact:
    "wandb.Artifact stub that does not need a run to be created"

    root: Path
    def get_path(self, x):
        return Downloadable(self.root / x)


@dataclass
class Utterance:
    utt_id: str
    wav: str # relative path to wav
    transcript: str


def read_utterances(artifact_name: str) -> Iterable[Utterance]:
    """Iterate through utterances in a wandb.Table generated by
    uk.share.datadir_to_artifact

    Creates files in ./artifact/ when run the first time.

    reference: https://github.com/proger/uk/blob/main/uk/share.py#L8
    """

    index = Path(f'artifacts/{artifact_name.split("/")[-1]}') / 'index.table.json'

    if not index.exists():
        run = wandb.init()

        artifact = run.use_artifact(artifact_name, type='dataset')
        artifact_dir = artifact.download()
        index = Path(artifact_dir) / 'index.table.json'
    else:
        artifact = StubArtifact(index.parent)

    table = wandb.Table.init_from_json(json.loads(index.read_text()), artifact)

    utt_ids = table.get_column("utt_id")
    audios = table.get_column("audio")
    texts = table.get_column("text")
    for utt_id, audio, transcript in zip(utt_ids, audios, texts):
        yield Utterance(utt_id, audio._path, transcript)


if __name__ == '__main__':
    from argparse import ArgumentParser
    p = ArgumentParser()
    p.add_argument('artifact_name')
    args = p.parse_args()
    for utterance in read_utterances(args.artifact_name):
        print(json.dumps(asdict(utterance), ensure_ascii=False))
