import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'fdgfh78@#5?>gfhf89dx,v06k'
