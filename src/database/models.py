import enum

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, func, event, Date, Enum
from sqlalchemy.orm import relationship, declarative_base


Base = declarative_base()

class Role(enum.Enum):
    admin: str = 'admin'
    moderator: str = 'moderator'
    user: str = 'user'



class Contact(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True)
    firstname = Column(String, index=True)
    lastname = Column(String)
    email = Column(String, unique=True, index=True)
    phone = Column(String, default="None", nullable=False)
    birthday = Column(Date, default=None, nullable=True)
    additional = Column(String, default="None", nullable=False)
    created_at = Column(DateTime, default=func.now())  
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    user_id = Column(
        "user_id", ForeignKey("users.id", ondelete="CASCADE"), default=None
    )
    user = relationship("User", backref="notes")


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(50))
    email = Column(String(250), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    created_at = Column("crated_at", DateTime, default=func.now())
    avatar = Column(String(255), nullable=True)
    refresh_token = Column(String(255), nullable=True)
    roles = Column('role', Enum(Role), default=Role.user)