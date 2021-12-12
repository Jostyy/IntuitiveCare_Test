import tabula
import pandas as pd
from zipfile import ZipFile
import os


class DataTransform:
    def __init__(self):
        self.df = pd.DataFrame()

    # Get table in pdf page and transform into pandas dataframe
    def table_to_dataframe(self, filepath, pages):
        # Single table in multiple pages
        if len(pages) > 1:
            self.df = tabula.read_pdf(
                filepath, pages=pages, multiple_tables=False, pandas_options={'index_col': 0})[-1]
        # Multiple tables in a single page
        else:
            self.df = tabula.read_pdf(
                filepath, pages=pages, multiple_tables=True)[-1]
            self.df.dropna(inplace=True)

            oldcolname = self.df.columns[0]
            newcolname = []

            # Verify dataframe header
            for i in range(0, len(self.df)):
                if self.df[oldcolname].iloc[i][0].isdigit():
                    if i == 1:
                        newcolname = newcolname[0].split(' ', 1)
                    row = i
                    break
                else:
                    newcolname.append(self.df[oldcolname].iloc[i])

            # Correct dataframe header and index
            self.df[newcolname] = self.df[oldcolname].str.split(
                ' ', 1, expand=True)
            self.df.drop(oldcolname, axis=1, inplace=True)
            self.df.drop(0 if row == 1 else [0, 1], axis=0, inplace=True)
            self.df.set_index(newcolname[0], drop=True, inplace=True)

    # Returns list of paths to files in speficified directory
    def get_file_paths(self, directory):
        file_paths = []

        for root, directories, files in os.walk(directory):
            for filename in files:
                filepath = os.path.join(root, filename)
                file_paths.append(filepath)

        return file_paths

    # Compress files with zip
    def compress_files(self, directory, filename):
        file_paths = self.get_file_paths(directory)

        with ZipFile(filename, 'w') as zip:
            for file in file_paths:
                zip.write(file)

        # Save dataframe to csv file
    def dataframe_to_csv(self, filepath):
        dir = filepath.rsplit('/', 1)[0]
        if not os.path.isdir(dir):
            os.mkdir(dir)

        self.df.dropna(inplace=True)
        self.df.to_csv(filepath, sep=';',
                       encoding='utf-8-sig')

    def transform(self, loadfile, savefile, pages):
        self.table_to_dataframe(loadfile, pages)
        self.dataframe_to_csv(savefile)
