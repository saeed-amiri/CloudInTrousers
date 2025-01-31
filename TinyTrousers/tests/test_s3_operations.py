"""
Test cases for the s3_operations module.
"""

import pytest

from s3_operations import upload_to_s3


def test_upload_to_s3() -> None:
    with pytest.raises(Exception):
        upload_to_s3("test-bucket", "test-file.txt")
