"""empty message

Revision ID: c08f70f85bfa
Revises: 4702f906188e
Create Date: 2024-01-25 22:16:54.893295

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c08f70f85bfa'
down_revision = '4702f906188e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('price', schema=None) as batch_op:
        batch_op.add_column(sa.Column('product_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('fk_price_product_id', 'product', ['product_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('price', schema=None) as batch_op:
        batch_op.drop_constraint('fk_price_product_id', type_='foreignkey')
        batch_op.drop_column('product_id')

    # ### end Alembic commands ###