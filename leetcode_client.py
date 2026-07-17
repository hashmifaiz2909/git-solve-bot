import requests
from urllib.parse import urlparse
import markdownify

def parse_slug(url_or_slug: str) -> str:
    """
    Extracts the problem title slug from a LeetCode URL or returns it directly if it's already a slug.
    """
    url_or_slug = url_or_slug.strip()
    if "leetcode.com" in url_or_slug:
        parsed = urlparse(url_or_slug)
        path_parts = [p for p in parsed.path.split("/") if p]
        if "problems" in path_parts:
            idx = path_parts.index("problems")
            if idx + 1 < len(path_parts):
                return path_parts[idx + 1]
        if path_parts:
            return path_parts[0]
    return url_or_slug.strip("/")

def fetch_leetcode_problem(title_slug: str) -> dict:
    """
    Fetches problem details (title, content/description, difficulty, code snippets) from LeetCode GraphQL API.
    """
    url = "https://leetcode.com/graphql"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Content-Type": "application/json",
        "Referer": f"https://leetcode.com/problems/{title_slug}/"
    }
    
    query = """
    query questionData($titleSlug: String!) {
      question(titleSlug: $titleSlug) {
        questionId
        questionFrontendId
        title
        titleSlug
        content
        difficulty
        codeSnippets {
          lang
          langSlug
          code
        }
      }
    }
    """
    
    payload = {
        "query": query,
        "variables": {
            "titleSlug": title_slug
        }
    }
    
    response = requests.post(url, json=payload, headers=headers, timeout=10)
    response.raise_for_status()
    
    data = response.json()
    if "data" in data and "question" in data["data"] and data["data"]["question"]:
        question = data["data"]["question"]
        
        # Clean description by converting HTML to Markdown
        html_content = question.get("content") or ""
        markdown_content = markdownify.markdownify(html_content, heading_style="ATX").strip()
        question["markdown_content"] = markdown_content
        
        return question
    else:
        raise ValueError(f"Problem '{title_slug}' not found or API error: {data}")

if __name__ == "__main__":
    # Quick sanity test
    slug = parse_slug("https://leetcode.com/problems/two-sum/")
    print(f"Parsed slug: {slug}")
    try:
        problem = fetch_leetcode_problem(slug)
        print(f"Title: {problem['title']}")
        print(f"Difficulty: {problem['difficulty']}")
        print(f"Snippets: {len(problem['codeSnippets'])} snippets fetched.")
    except Exception as e:
        print(f"Error fetching: {e}")
