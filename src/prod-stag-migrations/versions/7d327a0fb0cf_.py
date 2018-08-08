"""empty message

Revision ID: 7d327a0fb0cf
Revises: 
Create Date: 2018-07-24 17:10:37.313600

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7d327a0fb0cf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('activity_types',
    sa.Column('uuid', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('photo', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('value', sa.Integer(), nullable=True),
    sa.Column('supports_multiple_participants', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('uuid')
    )
    op.create_table('centers',
    sa.Column('uuid', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('photo', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('uuid')
    )
    op.create_table('roles',
    sa.Column('uuid', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('photo', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('uuid')
    )
    op.create_table('societies',
    sa.Column('uuid', sa.String(), nullable=False),
    sa.Column('photo', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('color_scheme', sa.String(), nullable=True),
    sa.Column('logo', sa.String(), nullable=True),
    sa.Column('_total_points', sa.Integer(), nullable=True),
    sa.Column('_used_points', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('uuid'),
    sa.UniqueConstraint('name')
    )
    op.create_table('cohorts',
    sa.Column('uuid', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('photo', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('center_id', sa.String(), nullable=True),
    sa.Column('society_id', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['center_id'], ['centers.uuid'], ),
    sa.ForeignKeyConstraint(['society_id'], ['societies.uuid'], ),
    sa.PrimaryKeyConstraint('uuid')
    )
    op.create_table('users',
    sa.Column('uuid', sa.String(), nullable=False),
    sa.Column('photo', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('society_id', sa.String(), nullable=True),
    sa.Column('center_id', sa.String(), nullable=True),
    sa.Column('cohort_id', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['center_id'], ['centers.uuid'], ),
    sa.ForeignKeyConstraint(['cohort_id'], ['cohorts.uuid'], ),
    sa.ForeignKeyConstraint(['society_id'], ['societies.uuid'], ),
    sa.PrimaryKeyConstraint('uuid'),
    sa.UniqueConstraint('email')
    )
    op.create_table('activities',
    sa.Column('uuid', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('photo', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('activity_type_id', sa.String(), nullable=True),
    sa.Column('activity_date', sa.Date(), nullable=True),
    sa.Column('added_by_id', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['activity_type_id'], ['activity_types.uuid'], ),
    sa.ForeignKeyConstraint(['added_by_id'], ['users.uuid'], ),
    sa.PrimaryKeyConstraint('uuid')
    )
    op.create_table('redemptions',
    sa.Column('uuid', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('photo', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('user_id', sa.String(), nullable=False),
    sa.Column('society_id', sa.String(), nullable=True),
    sa.Column('value', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(), nullable=False),
    sa.Column('center_id', sa.String(), nullable=False),
    sa.Column('comment', sa.String(), nullable=True),
    sa.Column('rejection', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['center_id'], ['centers.uuid'], ),
    sa.ForeignKeyConstraint(['society_id'], ['societies.uuid'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.uuid'], ),
    sa.PrimaryKeyConstraint('uuid')
    )
    op.create_table('user_role',
    sa.Column('user_uuid', sa.String(), nullable=False),
    sa.Column('role_uuid', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['role_uuid'], ['roles.uuid'], ),
    sa.ForeignKeyConstraint(['user_uuid'], ['users.uuid'], )
    )
    op.create_table('logged_activities',
    sa.Column('uuid', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('photo', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('value', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(), nullable=True),
    sa.Column('approved_at', sa.DateTime(), nullable=True),
    sa.Column('activity_date', sa.Date(), nullable=True),
    sa.Column('redeemed', sa.Boolean(), nullable=False),
    sa.Column('no_of_participants', sa.Integer(), nullable=True),
    sa.Column('approver_id', sa.String(), nullable=True),
    sa.Column('reviewer_id', sa.String(), nullable=True),
    sa.Column('activity_type_id', sa.String(), nullable=False),
    sa.Column('user_id', sa.String(), nullable=False),
    sa.Column('society_id', sa.String(), nullable=False),
    sa.Column('activity_id', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['activity_id'], ['activities.uuid'], ),
    sa.ForeignKeyConstraint(['activity_type_id'], ['activity_types.uuid'], ),
    sa.ForeignKeyConstraint(['society_id'], ['societies.uuid'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.uuid'], ),
    sa.PrimaryKeyConstraint('uuid')
    )
    op.create_table('user_activity',
    sa.Column('user_uuid', sa.String(), nullable=False),
    sa.Column('activity_uuid', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['activity_uuid'], ['activities.uuid'], ),
    sa.ForeignKeyConstraint(['user_uuid'], ['users.uuid'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_activity')
    op.drop_table('logged_activities')
    op.drop_table('user_role')
    op.drop_table('redemptions')
    op.drop_table('activities')
    op.drop_table('users')
    op.drop_table('cohorts')
    op.drop_table('societies')
    op.drop_table('roles')
    op.drop_table('centers')
    op.drop_table('activity_types')
    # ### end Alembic commands ###
