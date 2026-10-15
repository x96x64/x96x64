import importlib.util
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import xml.etree.ElementTree as ET

spec = importlib.util.spec_from_file_location("cards", Path(__file__).with_name("update-github-cards.py"))
cards = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cards)


class CardRefreshTests(unittest.TestCase):
    def test_preserves_metrics_geometry_and_links(self):
        original = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 80"><style>.label {font: 600 14px serif;}</style><a href="https://github.com/x96x64"><text x="10" y="20" class="label" font-family="serif">Commits: 42</text></a><path d="M0 0L1 1"/></svg>'
        transformed = ET.fromstring(cards.apply_system_font(original))
        override = transformed.find(f'{cards.NS}style[@id="profile-system-font"]')
        self.assertIn("system-ui", override.text)
        self.assertIn("!important", override.text)
        transformed.remove(override)
        self.assertEqual(ET.tostring(transformed), ET.tostring(ET.fromstring(original)))

    def test_rejects_http_success_error_cards(self):
        with self.assertRaises(ValueError):
            cards.apply_system_font('<svg xmlns="http://www.w3.org/2000/svg"><text>Something went wrong! API rate limit exceeded.</text></svg>')

    def test_rejects_invalid_provider_dimensions(self):
        with self.assertRaises(ValueError):
            cards.apply_system_font('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 -126 -1100"><text>Trophies</text></svg>')

    def test_failed_fetch_preserves_previous_set(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            existing = output / "stats-light.svg"
            existing.write_text("last successful card")
            def fetch(item):
                if item[0] == "broken.svg":
                    raise ValueError("Provider unavailable")
                return item[0], "new card"
            with patch.object(cards, "OUTPUT", output), patch.object(cards, "sources", return_value=[("stats-light.svg", ""), ("broken.svg", "")]), patch.object(cards, "fetch", side_effect=fetch):
                with self.assertRaises(ValueError):
                    cards.main()
            self.assertEqual(existing.read_text(), "last successful card")
            self.assertEqual(list(output.iterdir()), [existing])


if __name__ == "__main__":
    unittest.main()
