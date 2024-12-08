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
        #Search in the dataframe's names for the ingredient. 
        matches = self.dataframe[self.dataframe['ingredient'].str.contains(ingredient, na = False)]
        return matches if not matches.empty else None

    def retrieve(self, ingredient_name):
        """
        Retrieves an entry from the dataframe correspondant to a given ingredient name.

        Args:
            ingredient_name ([str]): [ingredient name to find in the dataframe].

        Returns:
            [dict]: [dictionary with values containing the ingredient's details, or None if not found].
        """
        #Retrieve the ingredient from the datafram if it is there.
        ingredient_data = self.is_in(ingredient_name)
        if ingredient_data is not None:
            return ingredient_data.iloc[0].to_dict()
        return None


