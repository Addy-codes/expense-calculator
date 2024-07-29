from sqlalchemy.ext.declarative import as_declarative, declared_attr
import sqlalchemy as sa
import uuid

@as_declarative()
class Base:
    id: any
    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    @declared_attr
    def id(cls):
        return sa.Column(sa.String, primary_key=True, default=lambda: str(uuid.uuid4()))
