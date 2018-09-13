"""Add genres table

Revision ID: ada03a2270d4
Revises: a56487f626b3
Create Date: 2018-09-13 07:04:19.312778

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID

# revision identifiers, used by Alembic.
revision = 'ada03a2270d4'
down_revision = 'a56487f626b3'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'genres',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('uuid', UUID(), unique=True, nullable=False),
        sa.Column('name', sa.String(100), unique=True, nullable=False),
        sa.Column('date_created', sa.DateTime, nullable=False, server_default=sa.func.now()),
        sa.Column('date_modified', sa.DateTime, nullable=False, server_default=sa.func.now(), server_onupdate=sa.func.now())
    )


def downgrade():
    op.drop_table('genres')
