"""Add users table

Revision ID: 567a1c759411
Revises: ada03a2270d4
Create Date: 2018-09-13 07:14:25.760300

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision = '567a1c759411'
down_revision = 'ada03a2270d4'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('uuid', UUID(), unique=True, nullable=False),
        sa.Column('first_name', sa.String(100)),
        sa.Column('last_name', sa.String(100), nullable=False),
        sa.Column('email', sa.Text, nullable=False),
        sa.Column('date_created', sa.DateTime, nullable=False, server_default=sa.func.now()),
        sa.Column('date_modified', sa.DateTime, nullable=False, server_default=sa.func.now(), server_onupdate=sa.func.now())
    )


def downgrade():
    op.drop_table('users')
