import json
from google import genai
from google.genai import types
from pydantic import BaseModel, Field
import config

# Define structure for the Gemini response
class SolutionDetails(BaseModel):
    code: str = Field(description="The complete correct code solution including the implemented starter code. Do not include markdown code block syntax inside this string.")
    explanation: str = Field(description="Brief explanation of the algorithm used.")
    time_complexity: str = Field(description="Time complexity analysis, e.g., O(N log N).")
    space_complexity: str = Field(description="Space complexity analysis, e.g., O(1).")

# Mapping of LeetCode langSlug to file extensions and standard display names
LANG_MAP = {
    "python3": {"ext": "py", "name": "Python3"},
    "python": {"ext": "py", "name": "Python"},
    "cpp": {"ext": "cpp", "name": "C++"},
    "java": {"ext": "java", "name": "Java"},
    "javascript": {"ext": "js", "name": "JavaScript"},
    "typescript": {"ext": "ts", "name": "TypeScript"},
    "rust": {"ext": "rs", "name": "Rust"},
    "golang": {"ext": "go", "name": "Go"},
    "c": {"ext": "c", "name": "C"},
    "csharp": {"ext": "cs", "name": "C#"},
    "swift": {"ext": "swift", "name": "Swift"},
    "kotlin": {"ext": "kt", "name": "Kotlin"},
    "ruby": {"ext": "rb", "name": "Ruby"},
    "scala": {"ext": "scala", "name": "Scala"},
    "php": {"ext": "php", "name": "PHP"}
}

def get_snippet_for_lang(snippets: list, target_lang: str) -> dict:
    """
    Finds the starter code snippet for the target language.
    """
    target_lang = target_lang.lower().strip()
    
    # Try direct match
    for s in snippets:
        if s["langSlug"].lower() == target_lang or s["lang"].lower() == target_lang:
            return s
            
    # Try partial match (e.g. "python" matches "python3")
    for s in snippets:
        if target_lang in s["langSlug"].lower() or target_lang in s["lang"].lower():
            return s
            
    # Return first snippet as fallback
    if snippets:
        return snippets[0]
    return {"code": "", "langSlug": target_lang, "lang": target_lang}

def generate_solution(problem_title: str, problem_description: str, difficulty: str, starter_code: str, language: str) -> SolutionDetails:
    """
    Calls the Google GenAI SDK (Gemini) to generate a solution for the given problem description.
    """
    config.validate_config()
    
    # Initialize the client. It will pick up GEMINI_API_KEY from environment variables automatically.
    client = genai.Client()
    
    system_instruction = (
        "You are an expert competitive programmer and software engineer. Your task is to solve the LeetCode "
        "problem provided. You must implement the solution inside the provided starter code template. "
        "Do not change the function signatures or class names in the starter code. "
        "Optimize your code for both time and space complexity. Write clean, readable code with helper methods if necessary. "
        "Ensure your response is valid JSON according to the response schema."
    )
    
    prompt = f"""
    Problem Title: {problem_title}
    Difficulty: {difficulty}
    Language: {language}
    
    Problem Description:
    {problem_description}
    
    Starter Code Template:
    ```
    {starter_code}
    ```
    
    Please provide:
    1. The fully implemented code solution that completes the starter template.
    2. A brief, high-level explanation of your approach.
    3. The time complexity.
    4. The space complexity.
    """
    
    # We use gemini-2.5-flash for fast and accurate code generation
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instruction=system_instruction,
            response_mime_type="application/json",
            response_schema=SolutionDetails,
            temperature=0.1 # Low temperature for more deterministic/logical code generation
        )
    )
    
    # Parse output
    try:
        data = json.loads(response.text)
        return SolutionDetails(**data)
    except Exception as e:
        # Fallback if parsing fails (unlikely with structured schema)
        raise ValueError(f"Failed to parse Gemini response: {e}. Raw response: {response.text}")
