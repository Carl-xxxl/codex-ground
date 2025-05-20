import sys
import types
import unittest
from unittest.mock import patch, Mock

# Create dummy modules so scripts.daily_news can be imported without real
# dependencies installed.
fake_requests = types.ModuleType('requests')
fake_requests.get = lambda *a, **k: None
fake_openai = types.ModuleType('openai')
fake_openai.ChatCompletion = types.SimpleNamespace(create=lambda *a, **k: None)
sys.modules.setdefault('requests', fake_requests)
sys.modules.setdefault('openai', fake_openai)

from scripts.daily_news import fetch_news, analyze_news

class TestDailyNews(unittest.TestCase):
    def test_fetch_news(self):
        fake_json = {
            "articles": [
                {"title": "Title1", "description": "Desc1"},
                {"title": "Title2"}
            ]
        }
        mock_resp = Mock()
        mock_resp.json.return_value = fake_json
        mock_resp.raise_for_status = Mock()
        with patch('requests.get', return_value=mock_resp) as mock_get:
            news = fetch_news('dummy', page_size=2)
            mock_get.assert_called_once()
        self.assertEqual(news, ["Title1\nDesc1", "Title2\n"])

    def test_analyze_news(self):
        fake_result = {"choices": [{"message": {"content": "summary"}}]}
        with patch('openai.ChatCompletion.create', return_value=fake_result) as m:
            res = analyze_news(['n1', 'n2'], model='x')
            m.assert_called_once()
        self.assertEqual(res, 'summary')

if __name__ == '__main__':
    unittest.main()
