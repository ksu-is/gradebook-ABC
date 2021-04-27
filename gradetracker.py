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
        assert len(category_name) > 0, f'GradeCalculator.add_category: Category name must not be an empty string'
        assert len(percentage_of_grade) > 0, f'GradeCalculator.add_category: Category percentage must not be an empty string'

        try:
            percentage_of_grade = float(percentage_of_grade)
        except:
            raise AssertionError(f'GradeCalculator.add_category: Category percentage must be an int or float')

        assert percentage_of_grade > 0, f'GradeCalculator.add_category: Category percentage must be greater than 0'
        
        if category_name in self.categories:
            raise KeyError(f'GradeCalculator.add_category: Category {category_name} has already been added')
        self.categories[category_name] = (percentage_of_grade, {})

        if not self._is_possible_grade_less_than_or_equal_100():
            total_percentage_too_long = self._calculate_total_possible_grade()
            del self.categories[category_name]
            raise ValueError(f'GradeCalculator.add_category: Percentage {percentage_of_grade}% of category {category_name} would make the total possible percentage {total_percentage_too_long}%, which exceeds the possible 100%')

    def remove_category(self, category_name: str) -> None:
        '''
        Removes a category from self.categories, given a category name.
        If given an invalid category_name, raises KeyError
        '''
        if category_name not in self.categories:
            raise KeyError(f"GradeCalculator.remove_category: Category '{category_name}' is not a valid key")
        del self.categories[category_name]
