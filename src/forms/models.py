import uuid
from datetime import datetime

import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from ..database import Base


class Option(Base):
    __tablename__ = 'option'

    id: int = sa.Column(sa.Integer, primary_key=True, nullable=False)
    title: str = sa.Column(sa.String)
    item_id: int = sa.Column(
        sa.Integer, sa.ForeignKey('item.id', ondelete="CASCADE"), nullable=False)
    item = relationship('Item',
                        uselist=False, back_populates='options')

class Item(Base):
    __tablename__ = 'item'

    id: int = sa.Column(sa.Integer, primary_key=True, nullable=False)
    title: str = sa.Column(sa.String)
    description: str = sa.Column(sa.Text)
    item_type: str = sa.Column(sa.String)
    item_order: int = sa.Column(sa.Integer)
    required: bool = sa.Column(sa.Boolean)
    form_id: int = sa.Column(
        sa.Integer, sa.ForeignKey('form.id', ondelete="CASCADE"), nullable=False)
    form = relationship('Form',
                        uselist=False, back_populates='items')
    options = relationship('Option',
                           uselist=True, back_populates='item')

class Form(Base):
    __tablename__ = 'form'

    id = sa.Column(sa.Integer, primary_key=True, nullable=False)
    title = sa.Column(sa.String)
    description: str = sa.Column(sa.String)
    is_template: bool = sa.Column(sa.Boolean)
    organization: str = sa.Column(sa.String)
    color: str = sa.Column(sa.String)
    to_review: bool = sa.Column(sa.Boolean, default=False)
    created_at: datetime = sa.Column(sa.DateTime(timezone=True),
                                     default=datetime.utcnow)
    link: str = sa.Column(sa.String)
    creator_id: uuid.UUID = sa.Column(
        UUID(as_uuid=True), sa.ForeignKey('user.id', ondelete="CASCADE"))
    items = relationship('Item',
                         uselist=True, back_populates='form')


# class Question(Base):
#     id: int = sa.Column(sa.Integer, primary_key=True, nullable=False)
#     required: bool = sa.Column(sa.Boolean)
#     question_type: str = sa.Column(sa.String)
#     prompt: dict = sa.Column(JSONB)
#     item_id = sa.Column(sa.Integer, sa.ForeignKey('item.id'), nullable=False)

#     item = relationship('Item', lazy='joined',
#                         uselist=False, back_populates='question')
