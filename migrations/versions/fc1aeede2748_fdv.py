"""fdv

Revision ID: fc1aeede2748
Revises: 2ba3b6ef1135
Create Date: 2022-04-20 20:15:59.608446

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fc1aeede2748'
down_revision = '2ba3b6ef1135'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('car_wash', sa.Column('username', sa.String(length=60), nullable=False))
    op.add_column('car_wash', sa.Column('password', sa.String(length=180), nullable=False))
    op.create_unique_constraint(None, 'car_wash', ['password'])
    op.create_unique_constraint(None, 'car_wash', ['username'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'car_wash', type_='unique')
    op.drop_constraint(None, 'car_wash', type_='unique')
    op.drop_column('car_wash', 'password')
    op.drop_column('car_wash', 'username')
    # ### end Alembic commands ###
