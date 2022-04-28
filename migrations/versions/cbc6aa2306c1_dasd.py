"""dasd

Revision ID: cbc6aa2306c1
Revises: aeca2a2706c2
Create Date: 2022-04-26 17:50:21.275628

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cbc6aa2306c1'
down_revision = 'aeca2a2706c2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('device_counter_total',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('device_id', sa.Integer(), nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.Column('coin', sa.Numeric(precision=8, scale=2), nullable=True),
    sa.Column('bill', sa.Numeric(precision=8, scale=2), nullable=True),
    sa.Column('cashless', sa.Numeric(precision=8, scale=2), nullable=True),
    sa.Column('bonus', sa.Numeric(precision=8, scale=2), nullable=True),
    sa.Column('service', sa.Numeric(precision=8, scale=2), nullable=True),
    sa.Column('last_update', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('device_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('device_counter_total')
    # ### end Alembic commands ###
