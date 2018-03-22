"""empty message

Revision ID: d5d39d13db7d
Revises: fd5a623ba72e
Create Date: 2018-03-22 00:12:37.795197

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd5d39d13db7d'
down_revision = 'fd5a623ba72e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_profile',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('biography', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('sex', sa.String(), nullable=True),
    sa.Column('created_on', sa.String(), nullable=True),
    sa.Column('filename', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_profile')
    # ### end Alembic commands ###
