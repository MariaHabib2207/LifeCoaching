"""Add full_name column to Appointment model

Revision ID: e47b7fd50205
Revises: 0019ef647595
Create Date: 2023-09-08 17:13:57.073516

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e47b7fd50205'
down_revision = '0019ef647595'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('appointment', schema=None) as batch_op:
        batch_op.alter_column('start_time',
               existing_type=sa.DATETIME(),
               nullable=True)
        batch_op.alter_column('end_time',
               existing_type=sa.DATETIME(),
               nullable=True)

    with op.batch_alter_table('booked_slot', schema=None) as batch_op:
        batch_op.alter_column('appointment_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('booking_time',
               existing_type=sa.DATETIME(),
               nullable=True)
        batch_op.alter_column('user_email',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('booked_slot', schema=None) as batch_op:
        batch_op.alter_column('user_email',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
        batch_op.alter_column('booking_time',
               existing_type=sa.DATETIME(),
               nullable=False)
        batch_op.alter_column('appointment_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    with op.batch_alter_table('appointment', schema=None) as batch_op:
        batch_op.alter_column('end_time',
               existing_type=sa.DATETIME(),
               nullable=False)
        batch_op.alter_column('start_time',
               existing_type=sa.DATETIME(),
               nullable=False)

    # ### end Alembic commands ###