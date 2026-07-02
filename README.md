# Data versioning and description

## Quick test

```sh
# (Install uv https://docs.astral.sh/uv/getting-started/installation/)
uv sync

# If your username is different to your username at PIK:
dvc remote modify --local pik-project-storage user [YOUR-USERNAME]
# this adds config override at .dvc/config.local which should remain secret

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

```bash
# Fetch data from remote
uv run dvc pull

# Track a file
dvc add path/to/file

# Clean up cache
dvc gc -waT

# Push to remote
dvc push
```

## Frictionless Data

We should do better at describing our datasets. The datapackage format offers a standardised way to do this. It doesn't take too much extra effort using [frictionless](https://framework.frictionlessdata.io/), see `scripts/write_data.py`.

### Description file
Stub for `datapackage.json`
```json
{
  "name": "package-key",
  "title": "Pretty dataset name",
  "description": "More extensive description of the dataset",
  "keywords": [
    "matching",
    "keywords"
  ],
  "resources": [
    {
      "name": "file-key",
      "path": "path/to/file.txt",
      "description": "Meaningful description of the file",
      ...
    },
    ...
  ]
}
```

Create a draft `resources` entry for a `datapackage.json` file
```bash
uv run frictionless describe path/to/file.txt --json
```


## Catalogueing data

If we document datapackages with frictionless, we could use a tool to create a catalogue that makes the data discoverable.

## Miscellaneous notes

### Remote directory permissions

The `g+s` flag in the `/data/rd5/ecs/DVC` directory means, that the parent group is assigned by default (`ecs` in our case) and the `g+x` flag is set.

https://man.archlinux.org/man/getfacl.1   
https://man.archlinux.org/man/setfacl.1

```bash
# Remote data at
/data/rd5/ecs/DVC

# By default, group members get rwx access
setfacl -d -m g::rws  /data/rd5/ecs/DVC
# By default, other users get no access
setfacl -d -m o::---  /data/rd5/ecs/DVC

# Check ACL rules
getfacl

# Check your group memberships
groups
```