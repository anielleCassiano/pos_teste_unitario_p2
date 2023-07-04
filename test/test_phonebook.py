import pytest

from src.phonebook import Phonebook


class TestPhonebook:

    @pytest.fixture
    def phonebook(self):
        return Phonebook()

    def test_add_name_contain_symbol_hash(self, phonebook):
        result = phonebook.add(name='#', number='000')
        assert result == 'Nome inválido'

    def test_add_name_contain_symbol_at(self, phonebook):
        result = phonebook.add(name='@', number='000')
        assert result == 'Nome inválido'

    def test_add_name_contain_symbol_exclamation(self, phonebook):
        result = phonebook.add(name='!', number='000')
        assert result == 'Nome inválido'

    def test_add_name_contain_symbol_dollar_sign(self, phonebook):
        result = phonebook.add(name='$', number='000')
        assert result == 'Nome inválido'

    def test_add_name_contain_symbol_percent(self, phonebook):
        result = phonebook.add(name='%', number='000')
        assert result == 'Nome inválido'

    def test_add_name_with_length_less_equal_than_zero(self, phonebook):
        result = phonebook.add(name='SAMU', number='')
        assert result == 'Número inválido'

    def test_add_name_already_saved(self, phonebook):
        result = phonebook.add(name='POLICIA', number='192')
        assert result == 'Nome inválido'

    def test_add_number_already_saved(self, phonebook):
        result = phonebook.add(name='SAMU', number='190')
        assert result == 'Nome inválido'

    def test_add_name_and_number_to_phonebook(self, phonebook):
        result = phonebook.add(name='SAMU', number='192')
        assert result == 'Número adicionado'

    def test_lookup_number_contain_symbol_hash(self, phonebook):
        result = phonebook.lookup(name='#')
        assert result == 'Nome inválido'

    def test_lookup_number_contain_symbol_at(self, phonebook):
        result = phonebook.lookup(name='@')
        assert result == 'Nome inválido'

    def test_lookup_number_contain_symbol_exclamation(self, phonebook):
        result = phonebook.lookup(name='!')
        assert result == 'Nome inválido'

    def test_lookup_number_contain_symbol_dollar_sign(self, phonebook):
        result = phonebook.lookup(name='$')
        assert result == 'Nome inválido'

    def test_lookup_number_contain_symbol_percent(self, phonebook):
        result = phonebook.lookup(name='%')
        assert result == 'Nome inválido'

    def test_lookup_number_not_in_phonebook(self, phonebook):
        result = phonebook.lookup(name='SAMU')
        assert result == 'Número não encontrado'

    def test_lookup_number_in_phonebook(self, phonebook):
        result = phonebook.lookup(name='POLICIA')
        assert result == '190'

    def test_get_names_in_phonebook(self, phonebook):
        result = phonebook.get_names()
        assert result == ['POLICIA']

    def test_get_numbers_in_phonebook(self, phonebook):
        result = phonebook.get_numbers()
        assert result == ['190']

    def test_clear_phonebook(self, phonebook):
        result = phonebook.clear()
        assert result == 'Phonebook limpado'

    def test_search_name_in_phonebook(self, phonebook):
        phonebook.add('POLICIA FEDERAL', '0800')
        result = phonebook.search(search_name='POL')
        assert result == [{'POLICIA', '190'}, {'POLICIA FEDERAL', '0800'}]

    def test_get_phonebook_sorted(self, phonebook):
        phonebook.add('SAMU', '192')
        phonebook.add('BOMBEIRO', '193')
        result = phonebook.get_phonebook_sorted()
        assert result == {'BOMBEIRO': '193', 'POLICIA': '190', 'SAMU': '192'}

    def test_get_phonebook_reverse(self, phonebook):
        phonebook.add('BOMBEIRO', '193')
        phonebook.add('SAMU', '192')
        result = phonebook.get_phonebook_reverse()
        assert result == {'SAMU': '192', 'POLICIA': '190', 'BOMBEIRO': '193'}

    def test_delete_name_not_exist_in_phonebook(self, phonebook):
        result = phonebook.delete('SAMU')
        assert result == 'Nome não existe'

    def test_delete_name_from_phonebook(self, phonebook):
        result = phonebook.delete('POLICIA')
        assert result == 'Número deletado'

    def test_change_number_not_exist(self, phonebook):
        result = phonebook.change_number(name='POLICIAN', number='191')
        assert result == 'Nome não existe'

    def test_change_number(self, phonebook):
        result = phonebook.change_number(name='POLICIA', number='191')
        assert result == 'Número alterado'

    def test_change_number_check_changed_number(self, phonebook):
        phonebook.change_number(name='POLICIA', number='191')
        result = phonebook.get_numbers()
        assert result == ['191']

    def test_get_name_by_number_not_exist(self, phonebook):
        result = phonebook.get_name_by_number(number='191')
        assert result == 'Número não existe'

    def test_get_name_by_number(self, phonebook):
        result = phonebook.get_name_by_number(number='190')
        assert result == 'POLICIA'
