from pydantic import BaseModel
from enum import Enum

class kelas(str,Enum):
    def __str__(self):
        return str(self.value)
    XII = "XII"
    XI  = "XI"
    X = "X"

class jenis_kelamin(str,Enum):
    def __str__(self):
        return str(self.value)
    LAKI = "Laki - laki"
    PEREMPUAN  = "Perempuan"

class Student(BaseModel):
    nisn : str
    name : str
    kelas : kelas
    jurusan : str
    jenis_kelamin : jenis_kelamin
    