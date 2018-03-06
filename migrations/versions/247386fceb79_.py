"""empty message

Revision ID: 247386fceb79
Revises: eac9f5a95842
Create Date: 2018-03-06 00:49:15.827358

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '247386fceb79'
down_revision = 'eac9f5a95842'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('goodsed', sa.Column('note', sa.UnicodeText(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('goodsed', 'note')
    # ### end Alembic commands ###
