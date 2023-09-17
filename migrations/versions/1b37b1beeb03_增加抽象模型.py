"""增加抽象模型

Revision ID: 1b37b1beeb03
Revises: 3495bdcb2c7b
Create Date: 2023-09-05 23:32:41.098163

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1b37b1beeb03'
down_revision = '3495bdcb2c7b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('createAt', sa.DateTime(), nullable=False, comment='创建时间'))
        batch_op.add_column(sa.Column('updateAt', sa.DateTime(), nullable=True, comment='更新时间'))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('updateAt')
        batch_op.drop_column('createAt')

    # ### end Alembic commands ###
