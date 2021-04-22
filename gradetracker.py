class GradeCalculator:

    # Constants for accessing 
    PERCENTAGE_OF_GRADE = 0
    ASSIGNMENTS = 1

    def __init__(self):

        # Initialize the categories dict
        self.categories = {}

    def __str__(self):

        # Create base string
        return_str = ''
        
        # Loop through all categories
        for k,v in self.categories.items():

            if len(v[GradeCalculator.ASSIGNMENTS]) == 0:
                return_str += f'{k}({v[GradeCalculator.PERCENTAGE_OF_GRADE]}%):\n'

            elif len(v[GradeCalculator.ASSIGNMENTS]) == 1:
                return_str += f'{k}({v[GradeCalculator.PERCENTAGE_OF_GRADE]}%): '
                for k,v in v[GradeCalculator.ASSIGNMENTS].items():
                    return_str += f'{k}: {v[0]}/{v[1]}\n'

            else:
                return_str += f'{k}({v[GradeCalculator.PERCENTAGE_OF_GRADE]}%): '
                for k,v in v[GradeCalculator.ASSIGNMENTS].items():
                    return_str += f'{k}: {v[0]}/{v[1]}, '
                return_str = return_str[:-2]
                return_str += '\n'

        return return_str

    def add_category(self, category_name: str, percentage_of_grade: str) -> None:
