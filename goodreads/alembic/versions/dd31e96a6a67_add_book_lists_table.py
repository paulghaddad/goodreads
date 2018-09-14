"""Add book_lists table

Revision ID: dd31e96a6a67
Revises: 37e01636d8af
Create Date: 2018-09-14 07:05:52.715714

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dd31e96a6a67'
down_revision = '37e01636d8af'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'book_lists',
        sa.Column('book_id', sa.Integer, nullable=False),
        sa.Column('list_id', sa.Integer, nullable=False)
    )
    op.create_foreign_key(
        'book_lists_books_fkey',
        'book_lists',
        'books',
        ['book_id'],
        ['id']
    )
    op.create_foreign_key(
        'book_lists_lists_fkey',
        'book_lists',
        'lists',
        ['list_id'],
        ['id']
    )
    op.create_index('book_lists_book_id_ix', 'book_lists', ['book_id'])
    op.create_index('book_lists_list_id_ix', 'book_lists', ['list_id'])


def downgrade():
    op.drop_table('book_lists')
