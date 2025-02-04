#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
"""
@Time    : 2023/9/4 15:40:40
@Author  : Stitch-z
@File    : test_file.py
"""
from pathlib import Path

import aiofiles
import pytest

from metagpt.utils.file import File


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("root_path", "filename", "content"),
    [(Path("/code/MetaGPT/data/tutorial_docx/2023-09-07_17-05-20"), "test.md", "Hello World!")]
)
async def test_write_file(root_path: Path, filename: str, content: bytes):
    full_file_name = await File.write(root_path=root_path, filename=filename, content=content.encode('utf-8'))
    assert isinstance(full_file_name, Path)
    assert root_path / filename == full_file_name
    async with aiofiles.open(full_file_name, mode="r") as reader:
        body = await reader.read()
        assert body == content