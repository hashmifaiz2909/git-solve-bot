import unittest
import os
from unittest.mock import patch, MagicMock

import leetcode_client
import solver
from git_manager import GitManager

class TestLeetCodeClient(unittest.TestCase):
    def test_parse_slug_url(self):
        url = "https://leetcode.com/problems/two-sum/"
        self.assertEqual(leetcode_client.parse_slug(url), "two-sum")

    def test_parse_slug_description_url(self):
        url = "https://leetcode.com/problems/reverse-integer/description/"
        self.assertEqual(leetcode_client.parse_slug(url), "reverse-integer")

    def test_parse_slug_raw(self):
        self.assertEqual(leetcode_client.parse_slug("two-sum"), "two-sum")

    def test_fetch_problem_integration(self):
        # Fetching a known easy problem
        problem = leetcode_client.fetch_leetcode_problem("two-sum")
        self.assertEqual(problem["title"], "Two Sum")
        self.assertEqual(problem["difficulty"], "Easy")
        self.assertIn("markdown_content", problem)
        self.assertGreater(len(problem["codeSnippets"]), 0)


class TestSolver(unittest.TestCase):
    def test_get_snippet_for_lang_exact(self):
        snippets = [
            {"lang": "Python3", "langSlug": "python3", "code": "def twoSum(): pass"},
            {"lang": "C++", "langSlug": "cpp", "code": "vector<int> twoSum() {}"}
        ]
        snippet = solver.get_snippet_for_lang(snippets, "cpp")
        self.assertEqual(snippet["langSlug"], "cpp")
        self.assertEqual(snippet["code"], "vector<int> twoSum() {}")

    def test_get_snippet_for_lang_partial(self):
        snippets = [
            {"lang": "Python3", "langSlug": "python3", "code": "def twoSum(): pass"}
        ]
        snippet = solver.get_snippet_for_lang(snippets, "python")
        self.assertEqual(snippet["langSlug"], "python3")

    @patch("solver.genai.Client")
    def test_generate_solution_mock(self, mock_genai_client):
        # Setup mock client behavior
        mock_instance = MagicMock()
        mock_genai_client.return_value = mock_instance
        
        mock_response = MagicMock()
        mock_response.text = '{"code": "def test(): pass", "explanation": "Mock explanation", "time_complexity": "O(1)", "space_complexity": "O(1)"}'
        mock_instance.models.generate_content.return_value = mock_response
        
        with patch.dict(os.environ, {"GEMINI_API_KEY": "test_key"}):
            solution = solver.generate_solution(
                problem_title="Mock Problem",
                problem_description="Mock description",
                difficulty="Easy",
                starter_code="def test():",
                language="Python3"
            )
            self.assertEqual(solution.code, "def test(): pass")
            self.assertEqual(solution.time_complexity, "O(1)")
            self.assertEqual(solution.space_complexity, "O(1)")


class TestGitManager(unittest.TestCase):
    def test_init_and_paths(self):
        git = GitManager("/tmp/non-existent-path-12345")
        self.assertFalse(git.is_git_repo())

    @patch("requests.put")
    @patch("requests.get")
    def test_push_via_api(self, mock_get, mock_put):
        # Set up mocks
        mock_get_response = MagicMock()
        mock_get_response.status_code = 404  # File does not exist yet
        mock_get.return_value = mock_get_response

        mock_put_response = MagicMock()
        mock_put_response.status_code = 201  # Created
        mock_put_response.text = "success"
        mock_put.return_value = mock_put_response

        # Create temporary file to push
        import tempfile
        with tempfile.TemporaryDirectory() as tmpdir:
            temp_file = os.path.join(tmpdir, "solution.py")
            with open(temp_file, "w") as f:
                f.write("print('hello')")

            git = GitManager(tmpdir)
            success = git.push_via_api(
                filepaths=[temp_file],
                message="test commit",
                repo_owner_and_name="username/repo",
                token="test_token",
                branch="main"
            )
            
            self.assertTrue(success)
            mock_get.assert_called_once()
            mock_put.assert_called_once()
            
            # Check url called
            called_url = mock_put.call_args[0][0]
            self.assertIn("username/repo/contents/solution.py", called_url)

if __name__ == "__main__":
    unittest.main()
