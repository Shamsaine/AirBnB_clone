# the __init__ file that turns a module into a package
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
