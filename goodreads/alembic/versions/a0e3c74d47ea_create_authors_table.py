"""Create authors table

Revision ID: a0e3c74d47ea
Revises: 48feb1cb1fef
Create Date: 2018-09-12 07:45:20.479358

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.schema import FetchedValue
from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision = 'a0e3c74d47ea'
down_revision = '48feb1cb1fef'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'authors',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('uuid', UUID(), nullable=False, unique=True),
        sa.Column('first_name', sa.String(100), nullable=False),
        sa.Column('last_name', sa.String(100), nullable=False),
        sa.Column('birthdate', sa.DateTime),
        sa.Column('date_created', sa.DateTime, nullable=False, server_default=sa.func.now()),
        sa.Column('date_modified', sa.DateTime, nullable=False, server_default=sa.func.now(), server_onupdate=FetchedValue())
    )


def downgrade():
    op.drop_table('authors')
