"""Test cases for the wikipedia module."""
from unittest.mock import Mock

import click
import pytest

from tutompy import wikipedia


def test_random_page_uses_given_language(mock_requests_get: Mock) -> None:
    """It selects the specified Wikipedia language edition."""
    wikipedia.random_page(language="fr")
    args, _ = mock_requests_get.call_args
    assert "fr.wikipedia.org" in args[0]


def test_random_page_returns_page(mock_requests_get: Mock) -> None:
    """It returns an object of type Page."""
    page = wikipedia.random_page()
    assert isinstance(page, wikipedia.Page)


def test_random_page_handles_validation_errors(mock_requests_get: Mock) -> None:
    mock_requests_get.return_value.__enter__.return_value.json.return_value = None
    """It raises `ClickException` when validation fails."""
    with pytest.raises(click.ClickException):
        wikipedia.random_page()
