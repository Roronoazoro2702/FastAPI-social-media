"""add content column to posts table

Revision ID: a8e1fec1987b
Revises: 31009c6640a6
Create Date: 2024-07-04 14:42:27.572273

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a8e1fec1987b'
down_revision: Union[str, None] = '31009c6640a6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
