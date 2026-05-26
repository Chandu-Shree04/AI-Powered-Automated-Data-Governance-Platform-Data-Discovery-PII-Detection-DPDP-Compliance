def summarize_profile(profile):

    summary = f"""
    Dataset contains {profile['rows']} rows
    and {profile['columns']} columns.

    Duplicate rows:
    {profile['duplicates']}
    """

    return summary