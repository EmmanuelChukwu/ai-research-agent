from langchain.tools import tool
import arxiv

@tool
def search_arxiv(query: str) -> str:
    """
    Search academic papers on ArXiv.
    Use this for scientific research and academic topics.
    """
    search = arxiv.Search(
        query=query,
        max_results=3,
        sort_by=arxiv.SortCriterion.Relevance
    )

    results = []

    for paper in search.results():
        results.append(
            f"""
Title: {paper.title}
Authors: {', '.join(a.name for a in paper.authors)}
Summary: {paper.summary}
Link: {paper.entry_id}
"""
        )

    return "\n\n".join(results)
