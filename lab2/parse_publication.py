import re
from typing import Optional


def parse_publication(reference: str) -> Optional[dict]:
    """
    Parse academic publication reference and extract structured information.

    Expected reference format:
    Lastname, I., Lastname2, I2. (Year). Title. Journal, Volume(Issue), StartPage-EndPage.

    Example:
    Kowalski, J., Nowak, A. (2023). Analiza algorytmów tekstowych. Journal of Computer Science, 45(2), 123-145.

    Args:
        reference (str): Publication reference string

    Returns:
        Optional[dict]: A dictionary containing parsed publication data or None if the reference doesn't match expected format
    """
    # TODO: Implement regex patterns to match different parts of the reference
    # You need to create patterns for:
    # 1. Authors and year pattern
    # 2. Title and journal pattern
    # 3. Volume, issue, and pages pattern
    authors_year_pattern = r"^(.*?)\s*\((\d{4})\)\."
    title_journal_pattern = r"\s*(.*?)\.\s*(.*?),"
    volume_issue_pages_pattern = r"\s*(\d+)(?:\((\d+)\))?,\s*(\d+)-(\d+)\.$"

    # TODO: Combine the patterns
    # full_pattern = authors_year_pattern + title_journal_pattern + volume_issue_pages_pattern
    full_pattern = authors_year_pattern + title_journal_pattern + volume_issue_pages_pattern

    # TODO: Use re.match to try to match the full pattern against the reference
    # If there's no match, return None
    match = re.match(full_pattern, reference.strip())
    if not match: return None

    # TODO: Extract information using regex
    # Each author should be parsed into a dictionary with 'last_name' and 'initial' keys

    # TODO: Create a pattern to match individual authors
    author_pattern = r"^\s*([^.]+?),\s*([A-Z])\.?$"

    # TODO: Use re.finditer to find all authors and add them to authors_list
    authors_list = []
    authors_str = match.group(1).strip()
    for author in re.split(r"(\.,)", authors_str):
        author_match = re.match(author_pattern, author)
        if author_match:
            authors_list.append({'last_name' : author_match.group(1).strip(), 'initial' : author_match.group(2).strip()})

    # TODO: Create and return the final result dictionary with all the parsed information
    # It should include authors, year, title, journal, volume, issue, and pages

    result = {
        'authors' : authors_list,
        'year' : int(match.group(2)),
        'title' : match.group(3).strip(),
        'journal' : match.group(4).strip(),
        'volume' : int(match.group(5)),
        'issue' : int(match.group(6)) if match.group(6) else None,
        'pages' : {
            'start' : int(match.group(7)),
            'end' : int(match.group(8))
        }
    }

    return result