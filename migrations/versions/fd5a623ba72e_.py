"""empty message

Revision ID: fd5a623ba72e
Revises: 87f566ece329
Create Date: 2018-03-19 18:18:14.823121

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fd5a623ba72e'
down_revision = '87f566ece329'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profile', sa.Column('biography', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_profile', 'biography')
    # ### end Alembic commands ###