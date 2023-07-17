def studentEntity(item) -> dict:
    return {
        "id":str(item["_id"]),
        "nisn":item["nisn"],
        "name":item["name"],
        "kelas":item["kelas"],
        "jurusan": item.get("jurusan", ""),
        "jenis_kelamin":item["jenis_kelamin"]
    }
    
def studentsEntity(entity) -> list:
    return [studentEntity(item)for item in entity]
