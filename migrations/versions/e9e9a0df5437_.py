"""empty message

Revision ID: e9e9a0df5437
Revises: f3c53cb4d458
Create Date: 2020-11-02 19:50:24.469927

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e9e9a0df5437'
down_revision = 'f3c53cb4d458'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('images')
    op.add_column('hotel', sa.Column('image1', sa.String(length=256), nullable=True))
    op.add_column('hotel', sa.Column('image2', sa.String(length=256), nullable=True))
    op.add_column('hotel', sa.Column('image3', sa.String(length=256), nullable=True))
    op.add_column('hotel', sa.Column('image4', sa.String(length=256), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('hotel', 'image4')
    op.drop_column('hotel', 'image3')
    op.drop_column('hotel', 'image2')
    op.drop_column('hotel', 'image1')
    op.create_table('images',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('image1', sa.VARCHAR(length=256), autoincrement=False, nullable=True),
    sa.Column('image2', sa.VARCHAR(length=256), autoincrement=False, nullable=True),
    sa.Column('image3', sa.VARCHAR(length=256), autoincrement=False, nullable=True),
    sa.Column('image4', sa.VARCHAR(length=256), autoincrement=False, nullable=True),
    sa.Column('image5', sa.VARCHAR(length=256), autoincrement=False, nullable=True),
    sa.Column('hotel_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['hotel_id'], ['hotel.id'], name='images_hotel_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='images_pkey')
    )
    # ### end Alembic commands ###
