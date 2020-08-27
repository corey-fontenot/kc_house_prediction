"""empty message

Revision ID: e4104d05e55a
Revises: 884de287a982
Create Date: 2020-08-27 13:23:27.287222

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e4104d05e55a'
down_revision = '884de287a982'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('estimates',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('bedrooms', sa.Integer(), nullable=False),
    sa.Column('bathrooms', sa.Integer(), nullable=False),
    sa.Column('floors', sa.Integer(), nullable=False),
    sa.Column('zipcode', sa.String(), nullable=False),
    sa.Column('waterfront', sa.Boolean(), nullable=False),
    sa.Column('view', sa.Boolean(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('estimates')
    # ### end Alembic commands ###
