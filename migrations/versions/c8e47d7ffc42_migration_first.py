"""migration first

Revision ID: c8e47d7ffc42
Revises: 
Create Date: 2024-07-07 00:09:38.630566

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c8e47d7ffc42'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('department',
    sa.Column('department_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('department_id')
    )
    op.create_table('job',
    sa.Column('job_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=50), nullable=False),
    sa.Column('salary_range', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('job_id')
    )
    op.create_table('training',
    sa.Column('training_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('training_name', sa.String(length=50), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('status', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('training_id')
    )
    op.create_table('employee',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('address', sa.String(length=200), nullable=True),
    sa.Column('phone', sa.String(length=20), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('job_id', sa.Integer(), nullable=True),
    sa.Column('department_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['department_id'], ['department.department_id'], ),
    sa.ForeignKeyConstraint(['job_id'], ['job.job_id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phone')
    )
    op.create_table('attendence',
    sa.Column('attendence_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('check_in_time', sa.DateTime(), nullable=False),
    sa.Column('check_out_time', sa.Date(), nullable=False),
    sa.Column('employee_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['employee_id'], ['employee.id'], ),
    sa.PrimaryKeyConstraint('attendence_id')
    )
    op.create_table('benefit',
    sa.Column('benefit_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('benefit_type', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=200), nullable=False),
    sa.Column('start_date', sa.Date(), nullable=False),
    sa.Column('end_date', sa.Date(), nullable=False),
    sa.Column('employee_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['employee_id'], ['employee.id'], ),
    sa.PrimaryKeyConstraint('benefit_id')
    )
    op.create_table('document',
    sa.Column('document_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('document_type', sa.String(length=50), nullable=False),
    sa.Column('file_path', sa.String(length=200), nullable=False),
    sa.Column('employee_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['employee_id'], ['employee.id'], ),
    sa.PrimaryKeyConstraint('document_id')
    )
    op.create_table('employee_training',
    sa.Column('e_id', sa.Integer(), nullable=False),
    sa.Column('t_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['e_id'], ['employee.id'], ),
    sa.ForeignKeyConstraint(['t_id'], ['training.training_id'], ),
    sa.PrimaryKeyConstraint('e_id', 't_id')
    )
    op.create_table('payroll',
    sa.Column('payroll_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('salary', sa.Integer(), nullable=False),
    sa.Column('bonus', sa.Integer(), nullable=False),
    sa.Column('deduction', sa.Integer(), nullable=False),
    sa.Column('paydate', sa.Date(), nullable=False),
    sa.Column('employee_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['employee_id'], ['employee.id'], ),
    sa.PrimaryKeyConstraint('payroll_id')
    )
    op.create_table('performance',
    sa.Column('performance_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('reviewdate', sa.Date(), nullable=False),
    sa.Column('score', sa.Integer(), nullable=False),
    sa.Column('feedback', sa.String(length=200), nullable=False),
    sa.Column('employee_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['employee_id'], ['employee.id'], ),
    sa.PrimaryKeyConstraint('performance_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('performance')
    op.drop_table('payroll')
    op.drop_table('employee_training')
    op.drop_table('document')
    op.drop_table('benefit')
    op.drop_table('attendence')
    op.drop_table('employee')
    op.drop_table('training')
    op.drop_table('job')
    op.drop_table('department')
    # ### end Alembic commands ###