from sqlalchemy.orm import Session
from src.models.category import CategoryModel

def create_category(db: Session, name: str, user_id: int):
    existing_category = db.query(CategoryModel).filter(CategoryModel.user_id == user_id,CategoryModel.name.ilike(name)).first()

    if existing_category:
        return None

    category = CategoryModel(name=name,user_id=user_id)

    db.add(category)
    db.commit()
    db.refresh(category)

    return category

def get_user_categories(db: Session, user_id: int):
    return db.query(CategoryModel).filter(CategoryModel.user_id == user_id).all()

def update_category(db: Session,category_id: int,name: str,user_id: int):
    category = db.query(CategoryModel).filter(CategoryModel.id == category_id,CategoryModel.user_id == user_id).first()

    if not category:
        return None

    category.name = name

    db.commit()
    db.refresh(category)

    return category

def delete_category(db: Session,category_id: int,user_id: int):
    category = db.query(CategoryModel).filter(CategoryModel.id == category_id,CategoryModel.user_id == user_id).first()

    if not category:
        return None

    db.delete(category)
    db.commit()

    return category