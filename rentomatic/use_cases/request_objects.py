class StorageRoomListRequestObject:
    @classmethod
    def from_dict(cls, adict):
        return StorageRoomListRequestObject()

    def __bool__(self):
        return True