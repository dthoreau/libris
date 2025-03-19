"""user authentication

Revision ID: 8caa40d1700c
Revises: a4fe8c1f0093
Create Date: 2025-02-27 10:26:28.966360

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from uuid import uuid4

from hashlib import blake2b


# revision identifiers, used by Alembic.
revision: str = '8caa40d1700c'
down_revision: Union[str, None] = 'a4fe8c1f0093'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.UUID(as_uuid=False), primary_key=True),
        sa.Column('username', sa.String, nullable=False),
        sa.Column('email', sa.String, nullable=False),
        sa.Column('full_name', sa.String, nullable=False),
        sa.Column('hashed_password', sa.String, nullable=True),
        sa.Column('disabled', sa.Boolean, nullable=False, default=False),
    )

    pwd = 'password'

    op.execute(f"""
        INSERT INTO users (id, username, full_name, email, hashed_password,
               disabled)
            VALUES ('{uuid4()}', 'admin', 'Admin', 'dominic@thoreau.kiwi',
                    '{blake2b(pwd.encode(encoding='utf-8')).hexdigest()}',  
                    'false')
    """)


def downgrade() -> None:
    op.drop_table('users')
    pass
