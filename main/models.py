# from datetime import datetime
# from email.policy import default
# from app import db

# class Comments(db.model):
#     id = db.Column(db.Interger, primary_key = True)
#     title = db.Column(db.string(100), nullable=False)
#     content = db.Column(db.text, nullable=False)
#     author = db.Column(db.String(20), nullable=False, default='N/A')
#     date_posted = db.Column(db.DateTime, nullable = False, default=datetime.utcnow)

#     def __repr__(self):
#         return 'Comment' + str(self.id)