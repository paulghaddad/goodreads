"""Add lists table

Revision ID: a56487f626b3
Revises: a0e3c74d47ea
Create Date: 2018-09-12 07:56:09.209760

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID

# revision identifiers, used by Alembic.
revision = 'a56487f626b3'
down_revision = 'a0e3c74d47ea'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'lists',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('uuid', UUID(), unique=True),
        sa.Column('name', sa.Text),
        sa.Column('date_created', sa.DateTime, nullable=False, server_default=sa.func.now()),
        sa.Column('date_modified', sa.DateTime, nullable=False, server_default=sa.func.now(), server_onupdate=sa.func.now())
    )


def downgrade():
    op.drop_table('lists')
