"""organization

Revision ID: 8f1264bcc95f
Revises: a08e0129a82b
Create Date: 2023-06-08 17:27:54.852406

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8f1264bcc95f'
down_revision = 'a08e0129a82b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('form', sa.Column('organization', sa.String(), nullable=True))
    op.drop_column('form', 'organiztion')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('form', sa.Column('organiztion', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('form', 'organization')
    # ### end Alembic commands ###