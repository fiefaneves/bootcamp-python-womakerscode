from datetime import datetime

from . import schemas
from . import models_SQLite
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, APIRouter, Response
from .database_SQLite import get_db

router = APIRouter()

# [...] get(read) all records
@router.get('/')
def get_notes(db: Session = Depends(get_db), limit: int = 10, page: int = 1, search: str = ''):
    skip = (page - 1) * limit

    notes = db.query(models_SQLite.Note).filter(models_SQLite.Note.title.contains(search)).limit(limit).offset(skip).all()
    return {'status': 'sucess', 'results': len(notes), 'notes': notes}

# [...] create record
@router.post('/', status_code=status.HTTP_201_CREATED)
def create_note(payload: schemas.NoteBaseSchema, db: Session = Depends(get_db)):
    new_note = models_SQLite.Note(**payload.dict())
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return {"status": "sucess", "note": new_note}

# [...] edit record
@router.patch('/{noteId}')
def update_note(noteId: str, payload: schemas.NoteBaseSchema, db: Session = Depends(get_db)):
    note_query = db.query(models_SQLite.Note).filter(models_SQLite.Note.id == noteId)
    db_note = note_query.first()

    if not db_note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No note with this id: {noteId} found')
    update_data = payload.dict(exclude_unset=True)
    note_query.filter(models_SQLite.Note.id == noteId).update(update_data, synchronize_session=False)
    db.commit()
    db.refresh(db_note)
    return {"status": "sucess", "note": db_note}

# [...] get(read) single record
@router.get('/{noteId}')
def get_post(noteId: str, db: Session = Depends(get_db)):
    note = db.query(models_SQLite.Note).filter(models_SQLite.Note.id == noteId).first()
    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No note with this id: {id} found")
    return {"status": "sucess", "note": note}

# [...] delete record
@router.delete('/{noteId}')
def delete_post(noteId: str, db: Session = Depends(get_db)):
    note_query = db.query(models_SQLite.Note).filter(models_SQLite.Note.id == noteId)
    note = note_query.first()
    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No note with this id: {id} found")
    note_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)