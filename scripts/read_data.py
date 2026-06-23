from frictionless import Package

def main():
    package = Package("datapackage.json")

    resource = package.get_resource("data")

    print(resource)

    data = resource.to_pandas()

    print(data.head())

if __name__=="__main__":
    main()