"""Add Company, Department, Position and relationship between tables

Revision ID: 56e5bba4226e
Revises: f3405d4d7241
Create Date: 2024-04-11 15:20:03.450677

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56e5bba4226e'
down_revision = 'f3405d4d7241'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('department', sa.Column('company_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'department', 'company', ['company_id'], ['id'])
    op.add_column('position', sa.Column('company_id', sa.Integer(), nullable=True))
    op.add_column('position', sa.Column('department_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'position', 'company', ['company_id'], ['id'])
    op.create_foreign_key(None, 'position', 'department', ['department_id'], ['id'])
    op.add_column('user', sa.Column('company_id', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('department_id', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('position_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'user', 'department', ['department_id'], ['id'])
    op.create_foreign_key(None, 'user', 'position', ['position_id'], ['id'])
    op.create_foreign_key(None, 'user', 'company', ['company_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='foreignkey')
    op.drop_constraint(None, 'user', type_='foreignkey')
    op.drop_constraint(None, 'user', type_='foreignkey')
    op.drop_column('user', 'position_id')
    op.drop_column('user', 'department_id')
    op.drop_column('user', 'company_id')
    op.drop_constraint(None, 'position', type_='foreignkey')
    op.drop_constraint(None, 'position', type_='foreignkey')
    op.drop_column('position', 'department_id')
    op.drop_column('position', 'company_id')
    op.drop_constraint(None, 'department', type_='foreignkey')
    op.drop_column('department', 'company_id')
    # ### end Alembic commands ###
