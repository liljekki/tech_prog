import unittest
from unittest.mock import patch
import lab_2
import io
from collections.abc import MutableMapping
class TestNotebook(unittest.TestCase):
    def setUp(self):
        self.notebook = lab_2.Notebook()

    def test_add(self):
        self.notebook.add("Заголовок 1", "Вміст нотатка 1")
        self.assertEqual(len(self.notebook.notes), 1)

    def test_del(self):
        self.notebook.add("Заголовок 1", "Вміст нотатка 1")
        self.notebook.del_n()
        self.assertEqual(len(self.notebook.notes), 0)

    def test_display(self):
        self.notebook.add("Заголовок 1", "Вміст нотатка 1")
        self.notebook.add("Заголовок 2", "Вміст нотатка 2")

        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            self.notebook.display()
            output = mock_stdout.getvalue()

        expected_output = (
            "Note 1:\nTitle: Заголовок 1\nContent: Вміст нотатка 1\n----------\n"
            "Note 2:\nTitle: Заголовок 2\nContent: Вміст нотатка 2\n----------\n"
        )

        self.assertEqual(output, expected_output)
    
    def test_err(self):
        with self.assertRaises(AttributeError):
            self.notebook.add_note("", "Вміст нотатки 1")

if __name__ == '__main__':
    import collections.abc
    import collections
    collections.MutableMapping = collections.abc.MutableMapping
    from xmlrunner import XMLTestRunner

    
    runner = XMLTestRunner(output='test-reports')
    unittest.main(testRunner=runner)
    unittest.main()
