"""'add'

Revision ID: 5e186944b5bb
Revises: 
Create Date: 2018-01-19 13:31:22.495047

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5e186944b5bb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('course_ibfk_1', 'course', type_='foreignkey')
    op.create_foreign_key(None, 'course', 'user', ['author_id'], ['id'], ondelete='CASCADE')
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_constraint(None, 'course', type_='foreignkey')
    op.create_foreign_key('course_ibfk_1', 'course', 'user', ['author_id'], ['id'], ondelete='SET NULL')
    # ### end Alembic commands ###
