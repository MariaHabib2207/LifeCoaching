"""Your migration message

Revision ID: bc1d96e5038f
Revises: d29568bc8ced
Create Date: 2023-09-11 12:59:47.782864

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bc1d96e5038f'
down_revision = 'd29568bc8ced'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('booked_slot', schema=None) as batch_op:
        batch_op.alter_column('flag',
               existing_type=sa.BOOLEAN(),
               type_=sa.String(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('booked_slot', schema=None) as batch_op:
        batch_op.alter_column('flag',
               existing_type=sa.String(),
               type_=sa.BOOLEAN(),
               existing_nullable=True)

    # ### end Alembic commands ###