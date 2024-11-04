"""add fullname

Revision ID: 4dae93d2ea0e
Revises: 2a452f23ddfe
Create Date: 2024-11-04 20:58:53.554582

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4dae93d2ea0e'
down_revision: Union[str, None] = '2a452f23ddfe'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('fullname', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'fullname')
    # ### end Alembic commands ###