from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto") #password hashing context

class Hash():
    def bcrypt(password: str):
        return pwd_cxt.hash(password)