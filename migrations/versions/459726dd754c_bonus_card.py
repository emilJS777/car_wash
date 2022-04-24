"""bonus card

Revision ID: 459726dd754c
Revises: 44e0ce4cbf15
Create Date: 2022-03-16 11:52:58.949884

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '459726dd754c'
down_revision = '44e0ce4cbf15'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('loyal_card',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('code', sa.String(length=120), nullable=False),
    sa.Column('price', sa.Numeric(), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('code')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('loyal_card')
    # ### end Alembic commands ###