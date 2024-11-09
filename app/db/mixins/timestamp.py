from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Date, text


class CreatedAtMixin:

    created_at = Column(
        DateTime,
        nullable=False,
        default=datetime.now,
        server_default=text('now()')
    )


class UpdatedAtMixin(CreatedAtMixin):

    updated_at = Column(
        DateTime,
        nullable=False,
        default=datetime.now,
        onupdate=datetime.now,
        server_default=text('now()')
    )


class ClosedAtMixin:

    planning_closed_at = Column(DateTime)
    critical_closed_at = Column(DateTime)


class StartedAtMixin:

    started_at = Column(Date, nullable=False)


class EndedAtMixin(StartedAtMixin):

    ended_at = Column(Date)
    is_until_now = Column(Boolean, nullable=False, default=False)
