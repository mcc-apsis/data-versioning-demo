import pandas as pd
from random import randint
from frictionless import Package, Resource

DATA_FILE = "data/data.csv"

def main():
    n_rows = 5
    df = pd.DataFrame({
        "id": range(n_rows),
        "value": [randint(0,100) for _ in range(n_rows)]
    })
    df.to_csv(DATA_FILE, index=False)

    package = Package(
        name="dvc-demo-data",
        title="DVC Demo Data",
        description="Demo data to show how DVC and frictionless can make our lives easier",
        resources=[
            Resource(path="data.csv")
        ]
    )

    resource = package.get_resource("data")
    resource.description = "Main data table containing mock data."

    package.to_json("data/datapackage.json")


if __name__=="__main__":
    main()