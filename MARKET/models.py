from MARKET import db


class Market(db.Model):
    __table__: 'Contacts'
    id = db.Column(db.Integer, primary_key=True)
    Nom = db.Column(db.String(64))
    Prenom = db.Column(db.String(64))
    Email = db.Column(db.String(64))
    Message = db.Column(db.Text())

    def __repr__(self):
        return f'<Market: {self.Email}-{self.Message}>'
  