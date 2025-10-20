"""
Database models for HydraBot
Defines User, Reminder, and ReminderLog tables
"""

from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

Base = declarative_base()

# Constant for cascade operations
CASCADE_DELETE = "all, delete-orphan"


class User(Base):
    """User model - stores user info from SMS or Telegram"""
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    platform = Column(String(20), nullable=False)  # 'twilio' or 'telegram'
    platform_id = Column(String(100), unique=True, nullable=False)  # phone number or chat_id
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    reminders = relationship("Reminder", back_populates="user", cascade=CASCADE_DELETE)
    logs = relationship("ReminderLog", back_populates="user", cascade=CASCADE_DELETE)


class Reminder(Base):
    """Reminder model - stores scheduled reminders"""
    __tablename__ = "reminders"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    # Reminder details
    title = Column(String(200), nullable=False)
    interval_minutes = Column(Integer, nullable=True)  # For recurring reminders (e.g., water every 2 hours)
    scheduled_time = Column(DateTime, nullable=True)  # For one-time reminders
    is_recurring = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    
    # Tracking
    last_sent_at = Column(DateTime, nullable=True)
    next_send_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    user = relationship("User", back_populates="reminders")
    logs = relationship("ReminderLog", back_populates="reminder", cascade=CASCADE_DELETE)


class ReminderLog(Base):
    """Log model - tracks reminder completions and history"""
    __tablename__ = "reminder_logs"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    reminder_id = Column(Integer, ForeignKey("reminders.id"), nullable=True)
    
    # Log details
    action = Column(String(50), nullable=False)  # 'sent', 'completed', 'cancelled', etc.
    reminder_title = Column(String(200), nullable=True)
    notes = Column(Text, nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    user = relationship("User", back_populates="logs")
    reminder = relationship("Reminder", back_populates="logs")


# Database setup
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./hydrabot.db")
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db():
    """Initialize database - create all tables"""
    Base.metadata.create_all(bind=engine)
    print("✅ Database initialized successfully")


def get_db():
    """Dependency for getting database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
