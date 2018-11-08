"""empty message

Revision ID: 528a31fb6993
Revises: 56df3dca8056
Create Date: 2018-11-07 23:33:05.631280

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '528a31fb6993'
down_revision = '56df3dca8056'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('teamname', sa.String(length=64), nullable=True))
    op.create_index(op.f('ix_user_teamname'), 'user', ['teamname'], unique=False)
    op.drop_index('ix_user_email', table_name='user')
    op.drop_index('ix_user_username', table_name='user')
    op.drop_column('user', 'email')
    op.drop_column('user', 'username')
    op.drop_column('user', 'password_hash')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('password_hash', sa.VARCHAR(length=128), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('username', sa.VARCHAR(length=64), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('email', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.create_index('ix_user_username', 'user', ['username'], unique=True)
    op.create_index('ix_user_email', 'user', ['email'], unique=True)
    op.drop_index(op.f('ix_user_teamname'), table_name='user')
    op.drop_column('user', 'teamname')
    # ### end Alembic commands ###
