def retrieve_metadata(metadata, query):

    results = {}

    for key, value in metadata.items():

        if query.lower() in key.lower():
            results[key] = value

    return results