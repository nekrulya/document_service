"""Add Company, Department, Position and relationship between tables

Revision ID: d6910d62ef15
Revises: 64ee13655d9d
Create Date: 2024-04-11 15:02:12.713303

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd6910d62ef15'
down_revision = '64ee13655d9d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'company')
    op.drop_column('user', 'position')
    op.drop_column('user', 'department')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('department', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('user', sa.Column('position', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('user', sa.Column('company', sa.VARCHAR(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
