from core import label, Table, field


class Information(Table):
    def _init(self):
        self._name = 'Information'
        self._caption = label('Information')
        
        self.pk = field.Code('Primary key', label('Primary key'), 10)
        self.name = field.Text('Name', label('Name'), 50)
        self.description = field.Text('Description', label('Description'), 250)
        self.copyright = field.Text('Copyright', label('Copyright'), 50)
        self.indicator = field.Text('Indicator', label('Indicator'), 50)

        self._setprimarykey(self.pk)
              
