from ddgs import DDGS
def web_search(query: str) -> dict:
    print("\n[ToolCall] Using web search ...")

    if not isinstance(query, str):
        raise ValueError("Search query must be a string")

    query = query.strip()

    if len(query) < 2:
        raise ValueError("Search query is too short")

    if len(query) > 300:
        raise ValueError("Search query is too long")

    try:

        search_engine = DDGS(timeout=15)

        raw_results = search_engine.text(
            query=query,
            region="us-en",
            safesearch="moderate",
            max_results=5,
            backend="auto"
        )

    except Exception as error:

        raise ValueError(
            f"Web search failed: {type(error).__name__}"
        ) from error

    results = []

    for item in raw_results:

        url = item.get("href", "")

        if not url.startswith(("https://", "http://")):
            continue

        results.append({
            "title": (item.get("title") or "")[:200],
            "url": url[:1000],
            "snippet": (item.get("body") or "")[:700]
        })

    return {
        "query": query,
        "result_count": len(results),
        "results": results
    }