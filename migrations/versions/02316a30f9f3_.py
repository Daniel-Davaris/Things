"""empty message

Revision ID: 02316a30f9f3
Revises: 76cb5f09d723
Create Date: 2019-10-15 01:00:20.990557

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '02316a30f9f3'
down_revision = '76cb5f09d723'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('item', sa.Column('quantity', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('item', 'quantity')
    # ### end Alembic commands ###
