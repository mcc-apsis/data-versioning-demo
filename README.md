# Data versioning and description

## Quick test

```sh
# (Install uv https://docs.astral.sh/uv/getting-started/installation/)
uv sync

# If your username is different to your username at PIK:
dvc remote modify --local pik-project-storage user [YOUR-USERNAME]

uv run dvc pull # enter password.
uv run python scripts/read_data.py
```

This repo doesn't commit data with git. Instead, dvc tracks the `data` folder and keeps a remote copy on our shared drive. Pulling this retrieves the data.

## Background

We version code with git, and in this way can partially reproduce a pipeline run at a certain time.

But because we do not version control data, the pipeline is not fully reproducible.

We also don't have a clear idea of what data we have where, or how we can re-use it.

This repo shows how some additional tools can begin to address these problems

## DVC

Usually, our git projects have a folder `data` that is .gitignored, and contains the data our scripts analyse. This might be training data which we don't want to share publicly, or large datasets that are too big for gitlab.

[Data Version Control](https://doc.dvc.org/start) allows us to version control that `data` folder.

## Frictionless Data

We should do better at describing our datasets. The datapackage format offers a standardised way to do this. It doesn't take too much extra effort using [frictionless](https://framework.frictionlessdata.io/), see `scripts/write_data.py`.

## Open Metadata

We could use [this](https://open-metadata.org) to automatically build a catalogue of all the data in our repositories that is described by a datapackage.

## Open questions
- How to set up dvc cache on our shared storage, one folder per repo? Or everything in one folder?