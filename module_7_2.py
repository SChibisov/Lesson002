class manager_file_read:
    def __init__(self, file_name):
        self.file_name = file_name

    def __enter__(self):
        self.file = open(self.file_name, 'r')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with manager_file_read('byron.txt') as r_file:
    read_file = r_file.read()

print(read_file)
