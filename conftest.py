import pytest

@pytest.fixture
def shared_numbers():
    return [10, 20, 30]

@pytest.fixture
def db_connection():
    print("\n准备 建立连接")
    conn = {"status": "connected"}
    yield conn
    print("\n清理 关闭连接")

    