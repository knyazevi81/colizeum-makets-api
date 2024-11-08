"""Update Tasks

Revision ID: 670371b7e2ca
Revises: 78eb7797167e
Create Date: 2024-11-03 11:34:50.142900

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '670371b7e2ca'
down_revision: Union[str, None] = '78eb7797167e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks', sa.Column('task_name', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tasks', 'task_name')
    # ### end Alembic commands ###
