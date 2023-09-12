from api.config.database import db
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime
from sqlalchemy.sql import func

class User(db.Model):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(80), unique=True, nullable=False)
    name = Column(String(80))
    height_in_meters = Column(Float(precision=2))
    active = Column(Boolean, default=True)  # For example, defaulting to active
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    deleted_at = Column(DateTime)

    # company_id = Column(Integer, db.ForeignKey('company.id'), nullable=False)
    # company = db.relationship('Company', backref='user')

    def to_dict(self):
        return dict(
            id=self.id,
            email=self.email,
            name=self.name,
            height_in_meters=self.height_in_meters,
            active=self.active,
            created_at=str(self.created_at) if self.created_at else None,
            updated_at=str(self.updated_at) if self.updated_at else None,
            deleted_at=str(self.deleted_at) if self.deleted_at else None
        )
