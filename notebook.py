from dataclasses import dataclass, field
import datetime
from typing import List, ClassVar
# Store the next available id for all new notes
last_id: int = 0
    # increment id

def get_incremented_id():
        global last_id
        last_id += 1
        return last_id

@dataclass
class Note:
    '''Represent a note in the notebook. Match against a string in searches and
    store tags for each note.'''

    '''Initiallize a note with memo and optional
    space-sperated tags. Automatically set the note's creation date and a
    unique id.'''
    memo: str
    tags: str
    creation_date = datetime.date.today()
    id: int = field(default_factory=get_incremented_id,init=False)

    def match(self, filter: str) -> bool:
        '''Determine if this note matches the filter
        text. Return True if it matches, False otherwise.
        Search is case sensitive and matches both text and tags.'''
        return filter in self.memo or filter in self.tags

class Notebook:
    '''Represent a collection of notes that can be tagged, 
    modified, and searched.'''
    def __init__(self):
        '''Initialize a notebook with an empty list.''' 
        self.notes: List[Note] = []
    def add_new_note(self, memo: str, tags: str=''):
        '''Create a new note and add it to the list.''' 
        self.notes.append(Note(memo, tags))

    def _find_note(self, note_id: int) -> Note:
        '''Locate the note with the given id.'''
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
        return None
        
    def modify_memo(self, note_id, memo):
        '''Find the note with the given id and change its 
        memo to the given value.'''
        note = self._find_note(note_id)
        if note:
            note.memo = memo
            return True
        return False
    def modify_tags(self, note_id: int, tags: str):
        '''Find the note with the given id and change its 
        tags to the given value.'''
        note = self._find_note(note_id)
        if note:
            note.tags = tags
            return True
        return False
            
    def search(self, filter: str):
        '''Find all notes that match the given filter 
        string.'''
        return [note for note in self.notes if 
                note.match(filter)]