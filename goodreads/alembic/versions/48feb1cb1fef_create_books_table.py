"""Create books table

Revision ID: 48feb1cb1fef
Revises: 
Create Date: 2018-09-12 06:58:50.366666

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.schema import FetchedValue
from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision = '48feb1cb1fef'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'books',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('uuid', UUID(), nullable=False, unique=True),
        sa.Column('title', sa.Text, nullable=False),
        sa.Column('publish_date', sa.Date),
        sa.Column('description', sa.Text),
        sa.Column('length', sa.Integer),
        sa.Column('date_created', sa.DateTime, nullable=False, server_default=sa.func.now()),
        sa.Column('date_modified', sa.DateTime, nullable=False, server_default=sa.func.now(), server_onupdate=FetchedValue())
    )


def downgrade():
    op.drop_table('books')
