"""Initial commit

Revision ID: 22c9a254b41e
Revises:
Create Date: 2019-06-17 17:42:47.075692

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "22c9a254b41e"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "data_cell",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column(
            "cell_type",
            sa.Enum("query", "text", "chart", name="datacelltype"),
            nullable=False,
        ),
        sa.Column("context", sa.Text(length=16777215), nullable=True),
        sa.Column("meta", sa.JSON(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        mysql_charset="utf8mb4",
        mysql_engine="InnoDB",
    )
    op.create_table(
        "data_job_metadata",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("job_name", sa.String(length=191), nullable=True),
        sa.Column("job_info", sa.JSON(), nullable=True),
        sa.Column("job_owner", sa.String(length=255), nullable=True),
        sa.Column("query_text", sa.Text(length=16777215), nullable=True),
        sa.Column("is_adhoc", sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        mysql_charset="utf8mb4",
        mysql_engine="InnoDB",
    )
    op.create_index(
        op.f("ix_data_job_metadata_job_name"),
        "data_job_metadata",
        ["job_name"],
        unique=False,
    )
    op.create_table(
        "environment",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("description", sa.String(length=5000), nullable=True),
        sa.Column("image", sa.String(length=2083), nullable=True),
        sa.Column("public", sa.Boolean(), nullable=True),
        sa.Column("archived", sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_environment_name"), "environment", ["name"], unique=True)
    op.create_table(
        "function_documentation",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("language", sa.String(length=255), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("params", sa.String(length=255), nullable=False),
        sa.Column("return_type", sa.String(length=255), nullable=False),
        sa.Column("description", sa.String(length=5000), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        mysql_charset="utf8mb4",
        mysql_engine="InnoDB",
    )
    op.create_table(
        "key_value_store",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("key", sa.String(length=191), nullable=True),
        sa.Column("value", sa.Text(length=16777215), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        mysql_charset="utf8mb4",
        mysql_engine="InnoDB",
    )
    op.create_index(
        op.f("ix_key_value_store_key"), "key_value_store", ["key"], unique=True
    )
    op.create_table(
        "query_metastore",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("metastore_url", sa.JSON(), nullable=True),
        sa.Column("acl_control", sa.Text(length=16777215), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    op.create_table(
        "task_run_record",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=True),
        sa.Column(
            "status",
            sa.Enum("RUNNING", "SUCCESS", "FAILURE", name="taskrunstatus"),
            nullable=False,
        ),
        sa.Column("alerted", sa.Boolean(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "task_schedule",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("task", sa.String(length=255), nullable=False),
        sa.Column("cron", sa.String(length=255), nullable=True),
        sa.Column("start_time", sa.DateTime(), nullable=True),
        sa.Column("args", sa.JSON(), nullable=True),
        sa.Column("kwargs", sa.JSON(), nullable=True),
        sa.Column("options", sa.JSON(), nullable=True),
        sa.Column("last_run_at", sa.DateTime(), nullable=True),
        sa.Column("total_run_count", sa.Integer(), nullable=True),
        sa.Column("enabled", sa.Boolean(), nullable=True),
        sa.Column("no_changes", sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    op.create_table(
        "task_schedules",
        sa.Column("id", sa.SmallInteger(), nullable=False),
        sa.Column("last_update", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("id"),
    )
    op.create_table(
        "user",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("username", sa.String(length=255), nullable=True),
        sa.Column("fullname", sa.String(length=255), nullable=True),
        sa.Column("password", sa.String(length=255), nullable=True),
        sa.Column("email", sa.String(length=255), nullable=True),
        sa.Column("profile_img", sa.String(length=2083), nullable=True),
        sa.Column("deleted", sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("username"),
    )
    op.create_table(
        "announcements",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.Column("uid", sa.Integer(), nullable=True),
        sa.Column("message", sa.String(length=5000), nullable=True),
        sa.Column("url_regex", sa.String(length=255), nullable=True),
        sa.Column("can_dismiss", sa.Boolean(), nullable=True),
        sa.ForeignKeyConstraint(["uid"], ["user.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "api_access_token",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("token", sa.String(length=128), nullable=False),
        sa.Column("description", sa.String(length=5000), nullable=True),
        sa.Column("enabled", sa.Boolean(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("creator_uid", sa.Integer(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.Column("updater_uid", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(["creator_uid"], ["user.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["updater_uid"], ["user.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("token"),
    )
    op.create_table(
        "data_doc",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("environment_id", sa.Integer(), nullable=False),
        sa.Column("public", sa.BOOLEAN(), nullable=False),
        sa.Column("archived", sa.BOOLEAN(), nullable=False),
        sa.Column("owner_uid", sa.Integer(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.Column("meta", sa.JSON(), nullable=False),
        sa.ForeignKeyConstraint(
            ["environment_id"], ["environment.id"], ondelete="CASCADE"
        ),
        sa.ForeignKeyConstraint(["owner_uid"], ["user.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        mysql_charset="utf8mb4",
        mysql_engine="InnoDB",
    )
    op.create_table(
        "data_schema",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.Column("name", sa.String(length=255), nullable=True),
        sa.Column("table_count", sa.Integer(), nullable=True),
        sa.Column("description", sa.Text(length=16777215), nullable=True),
        sa.Column("metastore_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(["metastore_id"], ["query_metastore.id"],),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_data_schema_name"), "data_schema", ["name"], unique=False)
    op.create_table(
        "impression",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("item_id", sa.Integer(), nullable=True),
        sa.Column(
            "item_type",
            sa.Enum("DATA_DOC", "DATA_TABLE", name="itemtype"),
            nullable=True,
        ),
        sa.Column("uid", sa.Integer(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(["uid"], ["user.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "query_engine",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("description", sa.String(length=255), nullable=True),
        sa.Column("language", sa.String(length=255), nullable=False),
        sa.Column("executor", sa.String(length=255), nullable=False),
        sa.Column("executor_params", sa.JSON(), nullable=True),
        sa.Column("control_params", sa.JSON(), nullable=False),
        sa.Column("metastore_id", sa.Integer(), nullable=True),
        sa.Column("environment_id", sa.Integer(), nullable=False),
        sa.Column("archived", sa.Boolean(), nullable=True),
        sa.ForeignKeyConstraint(
            ["environment_id"], ["environment.id"], ondelete="CASCADE"
        ),
        sa.ForeignKeyConstraint(["metastore_id"], ["query_metastore.id"],),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    op.create_table(
        "user_environment",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("environment_id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["environment_id"], ["environment.id"], ondelete="CASCADE"
        ),
        sa.ForeignKeyConstraint(["user_id"], ["user.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "user_role",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("uid", sa.Integer(), nullable=True),
        sa.Column("role", sa.Enum("ADMIN", name="userroletype"), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(["uid"], ["user.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "user_setting",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("uid", sa.Integer(), nullable=True),
        sa.Column("key", sa.String(length=255), nullable=True),
        sa.Column("value", sa.String(length=5000), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(["uid"], ["user.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        mysql_charset="utf8mb4",
        mysql_engine="InnoDB",
    )
    op.create_table(
        "data_doc_data_cell",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("data_doc_id", sa.Integer(), nullable=False),
        sa.Column("data_cell_id", sa.Integer(), nullable=False),
        sa.Column("cell_order", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(["data_cell_id"], ["data_cell.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["data_doc_id"], ["data_doc.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("data_cell_id"),
    )
    op.create_table(
        "data_doc_editor",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("data_doc_id", sa.Integer(), nullable=True),
        sa.Column("uid", sa.Integer(), nullable=True),
        sa.Column("read", sa.Boolean(), nullable=False),
        sa.Column("write", sa.Boolean(), nullable=False),
        sa.ForeignKeyConstraint(["data_doc_id"], ["data_doc.id"],),
        sa.ForeignKeyConstraint(["uid"], ["user.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("data_doc_id", "uid", name="unique_data_doc_user"),
    )
    op.create_table(
        "data_table",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.Column("name", sa.String(length=255), nullable=True),
        sa.Column("type", sa.String(length=255), nullable=True),
        sa.Column("owner", sa.String(length=255), nullable=True),
        sa.Column("table_created_at", sa.DateTime(), nullable=True),
        sa.Column("table_updated_by", sa.String(length=255), nullable=True),
        sa.Column("table_updated_at", sa.DateTime(), nullable=True),
        sa.Column("data_size_bytes", sa.BigInteger(), nullable=True),
        sa.Column("location", sa.String(length=2083), nullable=True),
        sa.Column("column_count", sa.Integer(), nullable=True),
        sa.Column("schema_id", sa.Integer(), nullable=True),
        sa.Column("golden", sa.Boolean(), nullable=True),
        sa.ForeignKeyConstraint(["schema_id"], ["data_schema.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_data_table_name"), "data_table", ["name"], unique=False)
    op.create_index(op.f("ix_data_table_type"), "data_table", ["type"], unique=False)
    op.create_table(
        "favorite_data_doc",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("data_doc_id", sa.Integer(), nullable=True),
        sa.Column("uid", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(["data_doc_id"], ["data_doc.id"],),
        sa.ForeignKeyConstraint(["uid"], ["user.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "query_execution",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("task_id", sa.String(length=255), nullable=True),
        sa.Column(
            "status",
            sa.Enum(
                "INITIALIZED",
                "DELIVERED",
                "RUNNING",
                "DONE",
                "ERROR",
                "CANCEL",
                name="queryexecutionstatus",
            ),
            nullable=True,
        ),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("completed_at", sa.DateTime(), nullable=True),
        sa.Column("query", sa.Text(length=16777215), nullable=True),
        sa.Column("engine_id", sa.Integer(), nullable=True),
        sa.Column("uid", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(["engine_id"], ["query_engine.id"],),
        sa.ForeignKeyConstraint(["uid"], ["user.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        mysql_charset="utf8mb4",
        mysql_engine="InnoDB",
    )
    op.create_table(
        "query_snippet",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("context", sa.Text(length=16777215), nullable=True),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.Column("engine_id", sa.Integer(), nullable=True),
        sa.Column("description", sa.String(length=5000), nullable=True),
        sa.Column("is_public", sa.Boolean(), nullable=False),
        sa.Column("golden", sa.Boolean(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("created_by", sa.Integer(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.Column("last_updated_by", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(["created_by"], ["user.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["engine_id"], ["query_engine.id"],),
        sa.ForeignKeyConstraint(["last_updated_by"], ["user.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        mysql_charset="utf8mb4",
        mysql_engine="InnoDB",
    )
    op.create_table(
        "data_cell_query_execution",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("query_execution_id", sa.Integer(), nullable=False),
        sa.Column("data_cell_id", sa.Integer(), nullable=False),
        sa.Column("latest", sa.Boolean(), nullable=False),
        sa.ForeignKeyConstraint(["data_cell_id"], ["data_cell.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(
            ["query_execution_id"], ["query_execution.id"], ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "data_table_column",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.Column("name", sa.String(length=255), nullable=True),
        sa.Column("type", sa.String(length=255), nullable=True),
        sa.Column("comment", sa.String(length=5000), nullable=True),
        sa.Column("description", sa.Text(length=16777215), nullable=True),
        sa.Column("table_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(["table_id"], ["data_table.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_data_table_column_name"), "data_table_column", ["name"], unique=False
    )
    op.create_table(
        "data_table_information",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("data_table_id", sa.Integer(), nullable=True),
        sa.Column("latest_partitions", sa.String(length=5000), nullable=True),
        sa.Column("earliest_partitions", sa.String(length=5000), nullable=True),
        sa.Column("description", sa.Text(length=16777215), nullable=True),
        sa.Column(
            "hive_metastore_description", sa.Text(length=16777215), nullable=True
        ),
        sa.ForeignKeyConstraint(
            ["data_table_id"], ["data_table.id"], ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("id"),
        mysql_charset="utf8mb4",
        mysql_engine="InnoDB",
    )
    op.create_table(
        "data_table_ownership",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("data_table_id", sa.Integer(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("owner", sa.String(length=255), nullable=True),
        sa.ForeignKeyConstraint(
            ["data_table_id"], ["data_table.id"], ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("data_table_id"),
    )
    op.create_table(
        "query_execution_error",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("query_execution_id", sa.Integer(), nullable=True),
        sa.Column("error_type", sa.Integer(), nullable=False),
        sa.Column("error_message_extracted", sa.String(length=5000), nullable=True),
        sa.Column("error_message", sa.Text(length=65535), nullable=True),
        sa.ForeignKeyConstraint(
            ["query_execution_id"], ["query_execution.id"], ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("id"),
        mysql_charset="utf8mb4",
        mysql_engine="InnoDB",
    )
    op.create_table(
        "query_execution_notification",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("query_execution_id", sa.Integer(), nullable=True),
        sa.Column("user", sa.String(length=255), nullable=False),
        sa.ForeignKeyConstraint(
            ["query_execution_id"], ["query_execution.id"], ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "statement_execution",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("statement_range_start", sa.Integer(), nullable=False),
        sa.Column("statement_range_end", sa.Integer(), nullable=False),
        sa.Column("query_execution_id", sa.Integer(), nullable=True),
        sa.Column(
            "status",
            sa.Enum(
                "INITIALIZED",
                "RUNNING",
                "UPLOADING",
                "DONE",
                "ERROR",
                "CANCEL",
                name="statementexecutionstatus",
            ),
            nullable=True,
        ),
        sa.Column("tracking_url", sa.String(length=2083), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("completed_at", sa.DateTime(), nullable=True),
        sa.Column("result_row_count", sa.BigInteger(), nullable=False),
        sa.Column("result_path", sa.String(length=2083), nullable=True),
        sa.Column("has_log", sa.Boolean(), nullable=False),
        sa.Column("log_path", sa.String(length=2083), nullable=True),
        sa.ForeignKeyConstraint(
            ["query_execution_id"], ["query_execution.id"], ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "table_lineage",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("table_id", sa.Integer(), nullable=True),
        sa.Column("parent_table_id", sa.Integer(), nullable=True),
        sa.Column("job_metadata_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(["job_metadata_id"], ["data_job_metadata.id"],),
        sa.ForeignKeyConstraint(
            ["parent_table_id"], ["data_table.id"], ondelete="CASCADE"
        ),
        sa.ForeignKeyConstraint(["table_id"], ["data_table.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "statement_execution_stream_log",
        sa.Column("id", sa.BigInteger(), nullable=False),
        sa.Column("statement_execution_id", sa.Integer(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("log", sa.String(length=5000), nullable=True),
        sa.ForeignKeyConstraint(
            ["statement_execution_id"], ["statement_execution.id"], ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("statement_execution_stream_log")
    op.drop_table("table_lineage")
    op.drop_table("statement_execution")
    op.drop_table("query_execution_notification")
    op.drop_table("query_execution_error")
    op.drop_table("data_table_ownership")
    op.drop_table("data_table_information")
    op.drop_index(op.f("ix_data_table_column_name"), table_name="data_table_column")
    op.drop_table("data_table_column")
    op.drop_table("data_cell_query_execution")
    op.drop_table("query_snippet")
    op.drop_table("query_execution")
    op.drop_table("favorite_data_doc")
    op.drop_index(op.f("ix_data_table_type"), table_name="data_table")
    op.drop_index(op.f("ix_data_table_name"), table_name="data_table")
    op.drop_table("data_table")
    op.drop_table("data_doc_editor")
    op.drop_table("data_doc_data_cell")
    op.drop_table("user_setting")
    op.drop_table("user_role")
    op.drop_table("user_environment")
    op.drop_table("query_engine")
    op.drop_table("impression")
    op.drop_index(op.f("ix_data_schema_name"), table_name="data_schema")
    op.drop_table("data_schema")
    op.drop_table("data_doc")
    op.drop_table("api_access_token")
    op.drop_table("announcements")
    op.drop_table("user")
    op.drop_table("task_schedules")
    op.drop_table("task_schedule")
    op.drop_table("task_run_record")
    op.drop_table("query_metastore")
    op.drop_index(op.f("ix_key_value_store_key"), table_name="key_value_store")
    op.drop_table("key_value_store")
    op.drop_table("function_documentation")
    op.drop_index(op.f("ix_environment_name"), table_name="environment")
    op.drop_table("environment")
    op.drop_index(op.f("ix_data_job_metadata_job_name"), table_name="data_job_metadata")
    op.drop_table("data_job_metadata")
    op.drop_table("data_cell")
    # ### end Alembic commands ###
