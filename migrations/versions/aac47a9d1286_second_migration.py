"""Second  Migration

Revision ID: aac47a9d1286
Revises: cd017b61c5a5
Create Date: 2021-06-20 14:10:51.443241

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aac47a9d1286'
down_revision = 'cd017b61c5a5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogs', sa.Column('blog_by', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('blogs', 'blog_by')
    # ### end Alembic commands ###
