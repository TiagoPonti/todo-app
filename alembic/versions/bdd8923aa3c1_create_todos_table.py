# alembic/versions/xxxx_create_todos_table.py
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '...' # El ID generado automáticamente
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.execute("""
    CREATE TABLE todos(
        id BIGSERIAL PRIMARY KEY,
        name TEXT,
        completed BOOLEAN NOT NULL DEFAULT false
    )
    """)

def downgrade():
    op.execute("DROP TABLE todos;")