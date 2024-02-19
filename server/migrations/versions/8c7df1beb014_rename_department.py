"""rename department

Revision ID: 8c7df1beb014
Revises: a58b5ca6e5b3
Create Date: 2024-02-19 16:05:39.428052

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8c7df1beb014'
down_revision = 'a58b5ca6e5b3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('department', 'departments')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('departments', 'department')
    # ### end Alembic commands ###