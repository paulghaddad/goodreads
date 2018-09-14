"""Add book_genres table

Revision ID: 37e01636d8af
Revises: 567a1c759411
Create Date: 2018-09-13 07:43:34.742545

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '37e01636d8af'
down_revision = '567a1c759411'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'book_genres',
        sa.Column('book_id', sa.Integer, nullable=False),
        sa.Column('genre_id', sa.Integer, nullable=False)
    )
    op.create_foreign_key(
        'book_genres_books_fkey',
        'book_genres',
        'books',
        ['book_id'],
        ['id']
    )
    op.create_foreign_key(
        'book_genres_genres_fkey',
        'book_genres',
        'genres',
        ['genre_id'],
        ['id']
    )
    op.create_index('book_genres_book_id_ix', 'book_genres', ['book_id'])
    op.create_index('book_genres_genre_id_ix', 'book_genres', ['genre_id'])


def downgrade():
    op.drop_table('book_genres')
