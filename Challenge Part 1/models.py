from main import db, ma
from werkzeug.security import generate_password_hash, check_password_hash

class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1001), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)

    def __init__(self, name, email):
        self.name = name
        self.email = email
        # self.password = password

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def __repr__(self):
        return f'<Company {self.name}>'
    
    def saveCompanyDetails_to_db(self):
        db.session.add(self)
        db.session.commit()

    def deleteCompanyDetails_from_db(self):
        db.session.delete(self)
        db.session.commit()
    
    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()
    

    
class Tool(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_id  = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)
    name = db.Column(db.String(1001), nullable=False)
    version = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(10), default='draft') 


class Section(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tool_id = db.Column(db.Integer, db.ForeignKey('tool.id'), nullable=False)
    name = db.Column(db.String(1001), nullable=False)

class Component(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    section_id = db.Column(db.Integer, db.ForeignKey('section.id'), nullable=False)
    type = db.Column(db.String(50))
    variant  = db.Column(db.String(50))
    pricing = db.Column(db.Float)

class CompanySchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'email')



class ToolSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'version')



class ComponentSchema(ma.Schema):
    class Meta:
        fields = ('id', 'type', 'variant', 'pricing')
