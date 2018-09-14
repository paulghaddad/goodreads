"""Add book_authors table

Revision ID: 2c6dd5f6ded2
Revises: dd31e96a6a67
Create Date: 2018-09-14 07:15:07.817230

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2c6dd5f6ded2'
down_revision = 'dd31e96a6a67'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'book_authors',
        sa.Column('book_id', sa.Integer, nullable=False),
        sa.Column('author_id', sa.Integer, nullable=False)
    )
    op.create_foreign_key(
        'book_authors_books_fkey',
        'book_authors',
        'books',
        ['book_id'],
        ['id']
    )
    op.create_foreign_key(
        'book_authors_authors_fkey',
        'book_authors',
        'authors',
        ['author_id'],
        ['id']
    )
    op.create_index('book_authors_book_id_ix', 'book_authors', ['book_id'])
    op.create_index('book_authors_author_id_ix', 'book_authors', ['author_id'])


def downgrade():
    op.drop_table('book_authors')
