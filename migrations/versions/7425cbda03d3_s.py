"""s

Revision ID: 7425cbda03d3
Revises: 
Create Date: 2023-06-17 04:23:22.330968

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7425cbda03d3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Player',
    sa.Column('ID', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('Name', sa.VARCHAR(length=255), nullable=False),
    sa.PrimaryKeyConstraint('ID')
    )
    op.create_index(op.f('ix_Players_Name'), 'Player', ['Name'], unique=False)
    op.create_table('Match',
    sa.Column('ID', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('Player1', sa.Integer(), nullable=False),
    sa.Column('Player2', sa.Integer(), nullable=False),
    sa.Column('Winner', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['Player1'], ['Player.ID'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['Player2'], ['Player.ID'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['Winner'], ['Player.ID'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('ID')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Match')
    op.drop_index(op.f('ix_Players_Name'), table_name='Player')
    op.drop_table('Player')
    # ### end Alembic commands ###
