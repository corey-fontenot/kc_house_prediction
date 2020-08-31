"""data models

Revision ID: 124fa6e8077a
Revises: ef3aa7cbfa4f
Create Date: 2020-08-30 15:28:52.715436

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '124fa6e8077a'
down_revision = 'ef3aa7cbfa4f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('data_model',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('model', sa.PickleType(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_data_model_name'), 'data_model', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_data_model_name'), table_name='data_model')
    op.drop_table('data_model')
    # ### end Alembic commands ###