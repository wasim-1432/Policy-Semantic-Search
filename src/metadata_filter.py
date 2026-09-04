def filter_results(
    results,
    department=None,
    document_type=None,
    date=None,
    access_level=None
):

    filtered = []

    for result in results:

        metadata = result["metadata"]

        if department:
            if metadata["department"].lower() != department.lower():
                continue

        if document_type:
            if metadata["document_type"].lower() != document_type.lower():
                continue

        if date:
            if metadata["date"] != date:
                continue

        if access_level:
            if metadata["access_level"].lower() != access_level.lower():
                continue

        filtered.append(result)

    return filtered