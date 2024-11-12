import pytest

from lambda_handler.app import app


def test_flask_simple():
    app.config["TESTING"] = True
    client = app.test_client()
    result = client.get("/hello")
    assert b'{"msg":"get method"}\n' == result.data


def test_flask_template():
    app.config["TESTING"] = True
    client = app.test_client()
    result = client.get("/")
    # htmlの特定の文字列が入っているか確認。仮でdoctype
    assert b"<!doctype html>" in result.data
