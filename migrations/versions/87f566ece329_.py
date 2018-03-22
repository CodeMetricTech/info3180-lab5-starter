"""empty message

Revision ID: 87f566ece329
Revises: 73c37dc61d15
Create Date: 2018-03-19 18:09:18.285081

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '87f566ece329'
down_revision = '73c37dc61d15'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(u'user_profile_username_key', 'user_profile', type_='unique')
    op.drop_column('user_profile', 'username')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profile', sa.Column('username', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.create_unique_constraint(u'user_profile_username_key', 'user_profile', ['username'])
    # ### end Alembic commands ###
