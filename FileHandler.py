class FileHandler:

    # constructor, initialize all the members
    def __init__(self):
        self.path = ""
        self.fileHandle = None
        self.numOfColumns = 0
        self.columns = dict()
        self.table = dict()

    # Parse the file present at path
    # path: Path to the file that needs to be parsed
    # The parser assumes that the file has the following format:
    # | col1        | col2          | col3 |
    # | row1_field1 | row1_field2   | row1_field3 |
    # | row2_field1 | row2_field2   | row2_field3 |
    # ...
    def parse(self, path):
        self.path = path
        self.fileHandle = open(path, "r+")
        if self.fileHandle is None:
            print("path does not exist")
            return

        header_row = self.fileHandle.readline()
        self.columns = header_row.split('|')
        self.numOfColumns = len(self.columns)

        for row in self.fileHandle:
            self.parse_row(row)

    # Parse a single row, and store in table
    # row: The row data that needs to be parsed
    def parse_row(self, row):
        elements = list()
        columns = row.split('|')
        for element in columns:
            elements.append(element.strip())
        self.table[columns[0].strip()] = elements

    def add_row(self, username, password, full_name, phone_number):
        if (self.get_row(username)) is not None:
            print("User already exists")
            return False

        self.table[username] = [username, password, full_name, phone_number]
        return True

    # get a row from the parsed table
    # key: key to the row in the table
    # returns the row if it exists, None otherwise
    def get_row(self, key):
        if self.fileHandle is None:
            print("Table not yet parsed, call parse() first")
            return
        if key in self.table:
            return self.table[key]
        return None

    def write_table(self):
        self.fileHandle.close()
        self.fileHandle = open(self.path, "r+")
        for element in self.columns:
            self.fileHandle.write(element)
            if element is not self.columns[self.numOfColumns - 1]:
                self.fileHandle.write('|')

        for username in self.table.keys():
            if (len(self.table[username])) is self.numOfColumns:
                self.fileHandle.write('\n')

                for col in range(self.numOfColumns):
                    self.fileHandle.write(self.table[username][col])
                    if col is not self.numOfColumns - 1:
                        self.fileHandle.write('|')
