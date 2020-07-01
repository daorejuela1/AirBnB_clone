#!/usr/bin/python3
""" call to filestorage class """


from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
