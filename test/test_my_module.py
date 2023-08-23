import pytest
from text_processing import process_text_data

@pytest.fixture
def file_fixture(tmp_path):
    file_content = "hello, world!"
    file_path = tmp_path / "test_file.txt"
    with file_path.open("w") as f:
        f.write(file_content)
    with file_path.open("r") as f:
        yield f

def test_process_text_data(file_fixture):
    result = process_text_data(file_fixture)
    assert result == "HELLO, WORLD!"

#  run the following command in the terminal: pytest test_text_processing.py