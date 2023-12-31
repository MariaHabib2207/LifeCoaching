"""Your migration message

Revision ID: 61517aab1630
Revises: 
Create Date: 2023-08-28 18:45:15.050405

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '61517aab1630'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('appointment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('full_name', sa.String(length=100), nullable=False),
    sa.Column('status', sa.String(length=20), nullable=True),
    sa.Column('payment_status', sa.String(length=20), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('appointment')
    # ### end Alembic commands ###
