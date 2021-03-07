"""
Tests for API handlers

"""
import json
import os
from flask import jsonify
import pytest
import ast

from app import create_app
from app.api.demoService import DemoHelloWorld



@pytest.fixture(scope='module', autouse=True)
def client():
    app = create_app()
    return app.test_client()


def test_not_found(client):
    response = client.get('/noexist')
    assert response.status_code == 404
    parsed_data = json.loads(response.data)
    assert parsed_data.get('error') == 'Not Found'


def test_hello(client):
    response = client.get('/api/v1/demo/1')
    assert response.status_code == 200
    parsed_data = json.loads(response.data)
    assert parsed_data == '{"message": "Hi !!"}'