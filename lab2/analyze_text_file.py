import re
from collections import Counter


def analyze_text_file(filename: str) -> dict:
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
    except Exception as e:
        return {"error": f"Could not read file: {str(e)}"}

    # Common English stop words to filter out from frequency analysis
    stop_words = {
        "the",
        "a",
        "an",
        "and",
        "or",
        "but",
        "in",
        "on",
        "at",
        "to",
        "for",
        "with",
        "by",
        "about",
        "as",
        "into",
        "like",
        "through",
        "after",
        "over",
        "between",
        "out",
        "of",
        "is",
        "are",
        "was",
        "were",
        "be",
        "been",
        "being",
        "have",
        "has",
        "had",
        "do",
        "does",
        "did",
        "this",
        "that",
        "these",
        "those",
        "it",
        "its",
        "from",
        "there",
        "their",
    }

    # TODO: Implement word extraction using regex
    # Find all words in the content (lowercase for consistency)
    words = re.findall(r"\b[^\W\d_]+\b", content.lower())
    word_count = len(words)

    # TODO: Implement sentence splitting using regex
    # A sentence typically ends with ., !, or ? followed by a space
    # Be careful about abbreviations (e.g., "Dr.", "U.S.A.")
    sentence_pattern = r"[A-Z](?:.*?)(?<!Prof)(?<!\.)[.!?](?=\s+[A-Z]|\s*$)"
    sentences = re.findall(sentence_pattern, content, re.MULTILINE)
    sentence_count = len(sentences)

    # TODO: Implement email extraction using regex
    # Extract all valid email addresses from the content
    email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
    emails = re.findall(email_pattern, content)

    # TODO: Calculate word frequencies
    # Count occurrences of each word, excluding stop words and short words
    # Use the Counter class from collections
    words = re.findall(r'\b(?!' + '|'.join(re.escape(word) + r'\b' for word in stop_words) + r')[^\W\d_]{2,}\b', content.lower())
    frequent_words = dict(Counter(words).most_common(10))

    # TODO: Implement date extraction with multiple formats
    # Detect dates in various formats: YYYY-MM-DD, DD.MM.YYYY, MM/DD/YYYY, etc.
    # Create multiple regex patterns for different date formats
    date_patterns = [r"\d{4}-\d{2}-\d{2}", r'\d{1,2}\.\d{1,2}\.\d{4}', r'\d{1,2}/\d{1,2}/\d{4}', r'\b\d{2}-\d{2}-\d{4}\b', r'\b[\w]+\s{1}\d+,\s\d+\b']
    dates = []
    for pattern in date_patterns:
        dates.extend(re.findall(pattern, content))

    # TODO: Analyze paragraphs
    # Split the content into paragraphs and count words in each
    # Paragraphs are typically separated by one or more blank lines
    paragraphs = re.split(r"\n\s*\n", content)
    words_pattern = r"\b[^\W\d_]+\b"
    paragraph_sizes = {}

    for i, paragraph in enumerate(paragraphs):
        words_in_paragraph = re.findall(words_pattern, paragraph)
        paragraph_sizes[i] = len(words_in_paragraph)

    return {
        "word_count": word_count,
        "sentence_count": sentence_count,
        "emails": emails,
        "frequent_words": frequent_words,
        "dates": dates,
        "paragraph_sizes": paragraph_sizes,
    }