from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import app, activities

# Keep a pristine copy so each test gets isolated in-memory state.
_ORIGINAL_ACTIVITIES = deepcopy(activities)


@pytest.fixture(autouse=True)
def reset_activities() -> None:
    activities.clear()
    activities.update(deepcopy(_ORIGINAL_ACTIVITIES))


@pytest.fixture
def client() -> TestClient:
    with TestClient(app) as test_client:
        yield test_client
