"""Add reviews table

Revision ID: d15ad0f2ddb7
Revises: 2c6dd5f6ded2
Create Date: 2018-09-14 07:22:48.787145

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.schema import FetchedValue


# revision identifiers, used by Alembic.
revision = 'd15ad0f2ddb7'
down_revision = '2c6dd5f6ded2'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'reviews',
        sa.Column('book_id', sa.Integer, nullable=False),
        sa.Column('user_id', sa.Integer, nullable=False),
        sa.Column('rating', sa.Integer, nullable=False),
        sa.Column('review', sa.Text),
        sa.Column('date_created', sa.DateTime, nullable=False, server_default=sa.func.now()),
        sa.Column('date_modified', sa.DateTime, nullable=False, server_default=sa.func.now(), server_onupdate=FetchedValue())
    )
    op.create_check_constraint(
        'rating_range_ck',
        'reviews',
        sa.sql.expression.between(sa.column('rating'), 1, 5)
    )
    op.create_foreign_key(
        'reviews_books_fkey',
        'reviews',
        'books',
        ['book_id'],
        ['id']
    )
    op.create_foreign_key(
        'reviews_users_fkey',
        'reviews',
        'users',
        ['user_id'],
        ['id']
    )
    op.create_index('reviews_book_id_ix', 'reviews', ['book_id'])
    op.create_index('reviews_user_id_ix', 'reviews', ['user_id'])


def downgrade():
    op.drop_table('reviews')
