from core import label, Table, FieldCode, FieldText
from app import option


class Information(Table):
    def _init(self):
        self._name = 'Information'
        self._caption = label('Information')
        
        self.pk = FieldCode('Primary key', label('Primary key'), 10)
        self.name = FieldText('Name', label('Name'), 50)
        self.description = FieldText('Description', label('Description'), 250)
        self.copyright = FieldCode('Copyright', label('Copyright'), 50)

        self._setprimarykey(self.pk)
              
