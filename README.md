# Data versioning and description

## Background

We version code with git, and in this way can partially reproduce a pipeline run at a certain time.

But because we do not version control data, the pipeline is not fully reproducible.

We also don't have a clear idea of what data we have where, or how we can re-use it.

This repo shows how some additional tools can make life a little easier

## DVC

Usually, our git projects have a folder `data` that is .gitignored, and contains the data our scripts analyse. This might be training data which we don't want to share publicly, or large datasets that are too big for gitlab.

[Data Version Control](https://doc.dvc.org/start) allows us to version control that `data` folder - or sub

## Frictionless Data

## Open Metadata

## Setting up dvc

If your system username is not the same as your PIK username, you will need to run

```
dvc remote modify --local pik-project-storage user [YOUR-USERNAME]
```