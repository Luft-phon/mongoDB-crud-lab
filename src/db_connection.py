from pymongo import MongoClient
from configparser import ConfigParser
from typing import Optional


# ---- Config & low-level helpers ----

_config = ConfigParser()
_config.read("config.ini")

_MONGO_CLIENT: Optional[MongoClient] = None


def get_db_name() -> str:
    return _config["server"]["database"]


def get_client() -> MongoClient:
    global _MONGO_CLIENT
    if _MONGO_CLIENT is None:
        host = _config["server"]["host"]
        port = _config["server"]["port"]
        url = f"mongodb://{host}:{port}/"
        _MONGO_CLIENT = MongoClient(url)
    return _MONGO_CLIENT


def get_db():
    client = get_client()
    db_name = get_db_name()
    return client[db_name]


# ---- Simple connection test ----

def test_connection():
    try:
        client = get_client()
        db = get_db()

        print("Database names:", client.list_database_names())
        print("Connected to DB:", db.name)
        print("Collections:", db.list_collection_names())

        # test session
        with client.start_session() as session:
            print("Session started successfully")
    except Exception as e:
        print("Connection failed:", e)


# ---- Session wrappers (SQLAlchemy-style-ish) ----

class Session:
    """Represents a MongoDB session wrapper used for typing."""

    def __init__(self, db, mongo_session):
        self.db = db                 # the database object
        self.session = mongo_session  # the actual MongoDB ClientSession


class SessionLocal:
    """Mimics SQLAlchemy SessionLocal for MongoDB."""

    def __init__(self):
        self.client = get_client()
        self.mongo_session = self.client.start_session()
        self.db = get_db()
        self.session_obj = Session(self.db, self.mongo_session)

    def __call__(self) -> Session:
        """Allow calling SessionLocal() to return a Session object."""
        return self.session_obj

    def start_transaction(self):
        """Explicitly start a transaction if you plan to use commit/rollback."""
        self.mongo_session.start_transaction()

    def close(self):
        self.mongo_session.end_session()

    def commit(self):
        try:
            self.mongo_session.commit_transaction()
        except Exception as exc:
            # Optionally log exc here
            pass

    def rollback(self):
        try:
            self.mongo_session.abort_transaction()
        except Exception as exc:
            # Optionally log exc here
            pass


if __name__ == "__main__":
    test_connection()
