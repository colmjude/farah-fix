"""empty message

Revision ID: 51190ff4a410
Revises: 1f80132fc1b1
Create Date: 2024-01-22 16:42:35.879834

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '51190ff4a410'
down_revision = '1f80132fc1b1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.add_column(sa.Column('farah_product_id', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.drop_column('farah_product_id')

    # ### end Alembic commands ###