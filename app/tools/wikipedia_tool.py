from langchain.tools import tool

@tool
def wikipedia_search(query: str) -> str:
    """
    Search Wikipedia for general knowledge information.
    Use this for background information on topics, definitions, historical facts, and summaries.
    """
    try:
        import wikipedia
        # Set language to English
        wikipedia.set_lang("en")
        
        # Try to get the page
        try:
            page = wikipedia.page(query, auto_suggest=True)
            # Return first 500 characters of the summary
            summary = page.summary[:500]
            return f"Wikipedia Summary for '{page.title}':\n\n{summary}"
        except wikipedia.exceptions.DisambiguationError as e:
            # Handle disambiguation
            options = e.options[:5]  # Get first 5 disambiguation options
            return f"Disambiguation: Multiple results found. Try one of these:\n" + "\n".join(options)
        except wikipedia.exceptions.PageError:
            return f"No Wikipedia page found for '{query}'"
    except ImportError:
        return "Wikipedia package not installed. Please install it with: pip install wikipedia"
    except Exception as e:
        return f"Error searching Wikipedia: {str(e)}"
