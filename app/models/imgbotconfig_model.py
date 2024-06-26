# models/imgbotconfig_model.py
from sqlalchemy import Column, Integer, String
from app import db  # Assuming 'db' is the SQLAlchemy object

class ImgBotConfig(db.Model):
    __tablename__ = 'imgbotconfig'

    id = Column(Integer, primary_key=True)
    key = Column(String(50), nullable=False)
    value = Column(String(255), nullable=True)

    def __repr__(self):
        return f"<ImgBotConfig(key='{self.key}', value='{self.value}')>"
