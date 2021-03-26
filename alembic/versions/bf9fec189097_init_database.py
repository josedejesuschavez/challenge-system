"""Init database

Revision ID: bf9fec189097
Revises: 
Create Date: 2021-03-25 08:30:36.426626

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bf9fec189097'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.String(36), primary_key=True),
        sa.Column('user_name', sa.String(50), nullable=False),
        sa.Column('password', sa.String(50), nullable=False),
    )

    op.create_table(
        'tokens',
        sa.Column('id', sa.String(36), primary_key=True),
        sa.Column('token', sa.String(500), nullable=False),
        sa.Column('user_name', sa.String(50), nullable=False),
    )


def downgrade():
    op.drop_table('users')
