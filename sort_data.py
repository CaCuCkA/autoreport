import re
from typing import List


class SortData:
    def __init__(self, data: list):
        self.data = data

    def sort_pictures(self) -> List[str]:
        """
        program sorting data and return list of pictures` paths, where you can
        find photos to your file
        :return: list of strings picture_paths
        """
        picture_paths = []
        for line in self.data:
            t_line = re.sub('[\n\t]', '', line)
            if t_line.endswith('png'):
                picture_paths.append(t_line)
                self.data.remove(line)
        return picture_paths

    def sort_code(self) -> List[str]:
        """
        program sorting data and return list of code, which you can input
        in your Word file
        :return: list of strings code_array
        """
        code_array = []
        try:
            for index in range(len(self.data)):
                if self.data[index].startswith('+') and self.data[index + 1].startswith('#in'):
                    self.data.pop(index)
                    inner_index = index
                    str_code = []
                    while not self.data[inner_index].startswith('+'):
                        line = self.data[inner_index]
                        str_code.append(line)
                        self.data.pop(inner_index)
                    self.data.pop(inner_index)
                    element = ''.join(str_code)
                    code_array.append(element)
        except IndexError:
            return code_array

    def sort_tests(self) -> List[List[str]]:
        """
        program sorting data and return list of testing data, which you can input
        in your Word file
        :return: list of lists with strings test_array
        """

        test_array = []
        task_tests = []

        try:
            for index in range(len(self.data)):
                try:
                    count = int(re.sub('[\n]', '', self.data[index]))
                except ValueError:
                    continue
                else:
                    if index != 1 and self.data[index + 1].startswith('+'):
                        for _ in range(2):
                            self.data.pop(index)
                        while count:
                            temp_line = []
                            while not self.data[index].startswith('+'):
                                line = self.data[index]
                                temp_line.append(line)
                                self.data.pop(index)
                            if count != 1:
                                for _ in range(2):
                                    self.data.pop(index)
                            else:
                                self.data.pop(index)
                            element = ''.join(temp_line)
                            task_tests.append(element)
                            count -= 1
                        test_array.append(task_tests)
                        task_tests = []
        finally:

            return test_array

    def remaining_data(self) -> str:
        """
         program sorting data and return string of data
        :return: string
        """
        if self.data[0].startswith('+'):
            temp_array = []
            self.data.pop(0)
            while not self.data[0].startswith('+'):
                temp_array.append(self.data[0])
                self.data.pop(0)
            self.data.pop(0)
            return ''.join(temp_array)
        else:
            result = self.data[0]
            self.data.pop(0)
            return result
