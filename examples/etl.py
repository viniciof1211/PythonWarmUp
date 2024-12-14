# Implement an ETL Pipeline kind of behaviour (it's dynamically typed)

def etl_pipeline(data):
    extracted = [d.strip() for d in data]
    transformed = [d.upper() for d in extracted]
    loaded = {i: val for i, val in enumerate(transformed)}
    return loaded