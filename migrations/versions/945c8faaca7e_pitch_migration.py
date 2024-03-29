"""Pitch Migration

Revision ID: 945c8faaca7e
Revises: ae95c455ff87
Create Date: 2019-11-25 14:44:59.241082

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '945c8faaca7e'
down_revision = 'ae95c455ff87'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('movie_id', sa.Integer(), nullable=True),
    sa.Column('movie_title', sa.String(), nullable=True),
    sa.Column('image_path', sa.String(), nullable=True),
    sa.Column('movie_review', sa.String(), nullable=True),
    sa.Column('posted', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pitches',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('category', sa.String(length=100), nullable=True),
    sa.Column('author', sa.String(length=100), nullable=True),
    sa.Column('upvote', sa.Integer(), nullable=True),
    sa.Column('downvote', sa.Integer(), nullable=True),
    sa.Column('date_posted', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pitches')
    op.drop_table('Comments')
    # ### end Alembic commands ###
