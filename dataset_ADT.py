'''
ADT for datasets storage.
'''

import pandas as pd

class DataframeDataset:
    """
    Storage for a dataset in dataframe.
    """
    #Slot for the dataframe.
    slots = ('dataframe')

    def read_data(self, path):
        """
        Reads the data from a dataset and filters for relevant columns.

        Args:
            path (str): Path to the Excel File

        """
        #Read the excel and save in the slot.
        dataframe = pd.read_excel(path, usecols=[0, 1, 2, 3])

        #Rename the columns
        dataframe.columns = ['ingredient', 'reason,' 'comedogenic', 'irritating']
        dataframe['ingredient'] = dataframe['ingredient'].str.strip().str.lower()

        self.dataframe = dataframe

    def is_in(self, ingredient):
        """
        Checks if the given ingredient is in the dataframe.

        Args:
            ingredients ([str]): Ingredient name to search for.

        Returns:
            pd.DataFrame: The rows(s) matching the ingredients, or None if not found.
        """
        #Search in the dataframe's names for the ingredient. STOPPED HERE!
        for name in self.dataframe['name'].to_numpy():
            if ingredient in name:
                return self.dataframe.loc[self.dataframe['name'] == name]

    def retrieve(self, ingredient_name):
        """
        Retrieves an entry from the dataframe correspondant to a given ingredient name.

        Args:
            ingredient_name ([str]): [ingredient name to find in the dataframe].

        Returns:
            [dict]: [dictionary with values correspondant to a given ingredient name].
        """
        #Retrieve the ingredient from the datafram if it is there.
        get_ingredient = self.is_in(ingredient_name)
        if get_ingredient is not None:
            return get_ingredient.iloc[0]

def preprocess(path, row_range, column_range, drop_strings):
    """
    Preprocessing of the datasets.

    Args:
        path ([string]): [path to a dataset].
        row_range ([tuple]): [range of rows to retrieve from the dataset].
        column_range ([tuple]): [range of columns to retrieve from the dataset].
    """
    def modify_name(name):
        return name.strip()[:name.find(' ')]

    dataframe = pd.read_excel(path)

    #Extract the needed columns and rows.
    dataframe = dataframe.iloc[row_range[0]: row_range[1],
                                    column_range[0]: column_range[1]]

    column_labels = dataframe.columns.tolist()

    #Construct a mapper fpr the labels.
    mapper_dict = {column_labels[0]:'name'}

    mapper_update = lambda lenght: {column_labels[index + 1]:'property'+str(index) for index in range(lenght)}
    mapper_update = mapper_update(len(column_labels[1:]))

    mapper_dict.update(mapper_update)

    #Rename the columns into the normal ones.
    dataframe.rename(columns = mapper_dict, inplace = True)

    #Drop the null values.
    dataframe.dropna(inplace = True)

    #Drop the invalid and unneeded rows using given identifiers.
    for drop_string in drop_strings:
        dataframe.drop(dataframe[dataframe['name'] == drop_string].index, inplace = True)
    
    dataframe['name'] = dataframe['name'].apply(modify_name)

    #Write the datafram into a file.
    dataframe.to_excel(path[:path.rfind('/')]+'_new.xlsx')
