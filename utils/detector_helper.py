def contains_keywords(text, keywords):
    """
    Checks if all keywords exist somewhere in the text.
    """
    text = text.lower()
    return all(keyword.lower() in text for keyword in keywords)

def quick_contains(text, keywords):
    """
    Checks if ANY keyword exists in the text (not all required).
    """
    text = text.lower()
    return any(keyword.lower() in text for keyword in keywords)
