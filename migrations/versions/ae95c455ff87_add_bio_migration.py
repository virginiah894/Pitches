"""Add bio Migration

Revision ID: ae95c455ff87
Revises: b49cbe4d6bbf
Create Date: 2019-11-24 12:07:25.710157

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ae95c455ff87'
down_revision = 'b49cbe4d6bbf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('bio', sa.String(length=200), nullable=True))
    op.add_column('users', sa.Column('password_secure', sa.String(length=200), nullable=True))
    op.add_column('users', sa.Column('profile_pic_path', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'profile_pic_path')
    op.drop_column('users', 'password_secure')
    op.drop_column('users', 'bio')
    # ### end Alembic commands ###
