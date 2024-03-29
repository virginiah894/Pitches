"""initial migration

Revision ID: 81665337e09b
Revises: a52f7d491bb1
Create Date: 2019-11-26 04:27:54.551985

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '81665337e09b'
down_revision = 'a52f7d491bb1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('pitch_id', sa.Integer(), nullable=True))
    op.drop_column('comments', 'pitch_title')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('pitch_title', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('comments', 'pitch_id')
    # ### end Alembic commands ###
