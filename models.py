from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import class_mapper
import uuid
from datetime import datetime
from decimal import Decimal

from sqlalchemy import Column, Integer, String, Boolean, DateTime, Time, Float, Text, ForeignKey, JSON, Numeric, Date, \
    TIMESTAMP, UUID, LargeBinary, text as text_sql, Interval
from sqlalchemy.types import Enum
from sqlalchemy.ext.declarative import declarative_base


@as_declarative()
class Base:
    id: int
    __name__: str

    # Auto-generate table name if not provided
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    # Generic to_dict() method
    def to_dict(self):
        """
        Converts the SQLAlchemy model instance to a dictionary, ensuring UUID fields are converted to strings.
        """
        result = {}
        for column in class_mapper(self.__class__).columns:
            value = getattr(self, column.key)
                # Handle UUID fields
            if isinstance(value, uuid.UUID):
                value = str(value)
            # Handle datetime fields
            elif isinstance(value, datetime):
                value = value.isoformat()  # Convert to ISO 8601 string
            # Handle Decimal fields
            elif isinstance(value, Decimal):
                value = float(value)

            result[column.key] = value
        return result




class Categories(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=True)
    name = Column(String)
    color = Column(String, nullable=True)
    created_at_dt = Column(DateTime, nullable=True, server_default=text_sql("now()"))
    updated_at_dt = Column(DateTime, nullable=True, server_default=text_sql("now()"))


class Tags(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=True)
    name = Column(String)
    created_at_dt = Column(DateTime, nullable=True, server_default=text_sql("now()"))


class TaskTags(Base):
    __tablename__ = "task_tags"

    id = Column(Integer, primary_key=True, autoincrement=True)
    task_id = Column(Integer, nullable=True)
    tag_id = Column(Integer, nullable=True)


class Tasks(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=True)
    category_id = Column(Integer, nullable=True)
    title = Column(String)
    description = Column(String, nullable=True)
    status = Column(String, nullable=True)
    priority = Column(String, nullable=True)
    due_date_dt = Column(DateTime, nullable=True, server_default=text_sql("now()"))
    created_at_dt = Column(DateTime, nullable=True, server_default=text_sql("now()"))
    updated_at_dt = Column(DateTime, nullable=True, server_default=text_sql("now()"))


class UserPreferences(Base):
    __tablename__ = "user_preferences"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=True)
    theme = Column(String, nullable=True)
    default_sort = Column(String, nullable=True)
    notifications_enabled = Column(Integer, nullable=True)
    updated_at_dt = Column(DateTime, nullable=True, server_default=text_sql("now()"))


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String)
    password = Column(String)
    created_at_dt = Column(DateTime, nullable=True, server_default=text_sql("now()"))


