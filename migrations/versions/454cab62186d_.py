"""empty message

Revision ID: 454cab62186d
Revises: ff4b47ae65dc
Create Date: 2018-03-06 16:14:37.880303

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '454cab62186d'
down_revision = 'ff4b47ae65dc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sellers', sa.Column('enable', sa.Boolean(), nullable=True))
    op.add_column('users', sa.Column('wechat_id', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'wechat_id')
    op.drop_column('sellers', 'enable')
    # ### end Alembic commands ###