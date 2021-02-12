class Sensive:
    SQLALCHEMY_DATABASE_URI ='sqlite:///data-dev.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_SORT_KEYS = False

    MAIL_SERVER = smtp.sendgrid.net
    MAIL_PORT = 587
    MAIL_USERNAME = apikey
    MAIL_PASSWORD = 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
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    
    JWT_SECURY_KEY  = 'ddgdnjkaikujroerinhtgfer'