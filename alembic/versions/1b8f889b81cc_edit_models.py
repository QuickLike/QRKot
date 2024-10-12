"""edit models

Revision ID: 1b8f889b81cc
Revises: 
Create Date: 2024-10-11 12:56:29.344052

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1b8f889b81cc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('CharityProject',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('full_amount', sa.Integer(), nullable=False),
    sa.Column('invested_amount', sa.Integer(), nullable=True),
    sa.Column('fully_invested', sa.Boolean(), nullable=True),
    sa.Column('create_date', sa.DateTime(), nullable=True),
    sa.Column('close_date', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.CheckConstraint('invested_amount <= full_amount', name='check_invested_amount_not_exceed_full'),
    sa.CheckConstraint('invested_amount >= 0', name='check_invested_amount_positive'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=320), nullable=False),
    sa.Column('hashed_password', sa.String(length=1024), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('is_superuser', sa.Boolean(), nullable=False),
    sa.Column('is_verified', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_table('Donation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('full_amount', sa.Integer(), nullable=False),
    sa.Column('invested_amount', sa.Integer(), nullable=True),
    sa.Column('fully_invested', sa.Boolean(), nullable=True),
    sa.Column('create_date', sa.DateTime(), nullable=True),
    sa.Column('close_date', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('comment', sa.Text(), nullable=True),
    sa.CheckConstraint('invested_amount <= full_amount', name='check_invested_amount_not_exceed_full'),
    sa.CheckConstraint('invested_amount >= 0', name='check_invested_amount_positive'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Donation')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_table('CharityProject')
    # ### end Alembic commands ###