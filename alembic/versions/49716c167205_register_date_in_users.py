"""register date in users

Revision ID: 49716c167205
Revises: f12d3c042d8d
Create Date: 2022-03-04 11:52:44.018010

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '49716c167205'
down_revision = 'f12d3c042d8d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('posts')
    # ### end Alembic commands ###
