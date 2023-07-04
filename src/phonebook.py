class Phonebook:
    def __init__(self):
        self.entries = {'POLICIA': '190'}
        self._INVALID_NAMES = ['#', '@', '!', '$', '%']

    def add(self, name, number):
        """
        :param name: name of person in string
        :param number: number of person in string
        :return: 'Nome inválido' or 'Número invalido' or 'Número adicionado'
        """
        if name in self._INVALID_NAMES:
            return 'Nome inválido'

        if len(number) == 0:
            return 'Número inválido'

        if name in self.entries.keys() or number in self.entries.values():
            return 'Nome inválido'

        self.entries[name] = number
        return 'Número adicionado'

    def lookup(self, name):
        """
        :param name: name of person in string
        :return: return number of person with name
        """
        if name in self._INVALID_NAMES:
            return 'Nome inválido'

        if name not in self.entries.keys():
            return 'Número não encontrado'

        return self.entries[name]

    def get_names(self):
        """

        :return: return all names in phonebook
        """
        return list(self.entries.keys())

    def get_numbers(self):
        """

        :return: return all numbers in phonebook
        """
        return list(self.entries.values())

    def clear(self):
        """
        Clear all phonebook
        :return: return 'phonebook limpado'
        """
        self.entries = {}
        return 'Phonebook limpado'

    def search(self, search_name):
        """
        Search all substring with search_name
        :param search_name: string with name for search
        :return: return list with results of search
        """
        result = []
        for name, number in self.entries.items():
            if search_name in name:
                result.append({name, number})
        return result

    def get_phonebook_sorted(self):
        """

        :return: return phonebook in sorted order
        """
        result = dict(list(self.entries.items()))
        return result

    def get_phonebook_reverse(self):
        """

        :return: return phonebook in reverse sorted order
        """
        result = dict(reversed(list(self.entries.items())))
        return result

    def delete(self, name):
        """
        Delete person with name
        :param name: String with name
        :return: return 'Numero deletado'
        """
        if name not in self.entries.keys():
            return 'Nome não existe'

        self.entries.pop(name)
        return 'Número deletado'

    def change_number(self, name, number):
        if name not in self.entries.keys():
            return 'Nome não existe'

        self.entries[name] = number
        return 'Número alterado'

    def get_name_by_number(self, number):
        if number not in self.entries.values():
            return 'Número não existe'

        for key, value in self.entries.items():
            if value == number:
                return key
