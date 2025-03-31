import unittest
import pandas as pd
import app.io.input as ipt


class TestInput(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.text_file = "test_text.txt"
        cls.csv_file = "test_data.csv"
        cls.missing_file = "missing_file.txt"

        with open(cls.text_file, "w") as file:
            file.write("Hello, this is a test file.")

        df = pd.DataFrame({"Name": ["Alice", "Bob"], "Age": [23, 27], "Score": [89, 76]})
        df.to_csv(cls.csv_file, index=False)

    def test_read_file_success(self):
        content = ipt.read_file(self.text_file)
        self.assertEqual(content, "Hello, this is a test file.")

    def test_read_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            ipt.read_file(self.missing_file)

    def test_read_file_pd_success(self):
        content = ipt.read_file_pd(self.csv_file)
        df_expected = pd.DataFrame({"Name": ["Alice", "Bob"], "Age": [23, 27], "Score": [89, 76]})
        expected_output = df_expected.to_string(index=False)
        self.assertEqual(content.strip(), expected_output.strip())

    def test_read_file_pd_not_found(self):
        with self.assertRaises(FileNotFoundError):
            ipt.read_file_pd(self.missing_file)


if __name__ == '__main__':
    unittest.main()
