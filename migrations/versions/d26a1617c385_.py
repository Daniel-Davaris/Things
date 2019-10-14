"""empty message

Revision ID: d26a1617c385
Revises: 87546e1673b7
Create Date: 2019-10-14 23:27:41.976090

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd26a1617c385'
down_revision = '87546e1673b7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('brand_item', sa.Column('id', sa.Integer(), nullable=False))
    op.alter_column('brand_item', 'brand_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('brand_item', 'item_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.add_column('category_item', sa.Column('id', sa.Integer(), nullable=False))
    op.alter_column('category_item', 'category_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('category_item', 'item_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('category_item', 'item_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('category_item', 'category_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_column('category_item', 'id')
    op.alter_column('brand_item', 'item_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('brand_item', 'brand_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_column('brand_item', 'id')
    # ### end Alembic commands ###
