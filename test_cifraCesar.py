import pytest
from unittest.mock import patch
from cifraCesar import cifra_Cesar

# função para simular comportamento do input
def user_input_side_effects(inputs):
    def side_effect(prompt):
        return inputs.pop(0)
    return side_effect
# ID do caso de teste = CT01 | Verifica se a função produz as saídas corretas para 2 casos de teste
def test_CT01():
    inputs = ["2", "VQREQFGT", "2", "ZWBGLZ", "25"]
    expected_output = ["TOPCODER", "AXCHMA"]
    with patch('builtins.input', side_effect=user_input_side_effects(inputs)):
        assert cifra_Cesar() == expected_output
# ID do caso de teste = CT02 | Testa como a função trata uma sentença vazia
def test_CT02():
    inputs = ["1", "", "ABCDE", "3"]
    expected_output = ["XYZAB"]
    with patch('builtins.input', side_effect=user_input_side_effects(inputs)):
        assert cifra_Cesar() == expected_output
# ID do caso de teste = CT03 | Avalia a resposta do programa quando um número negativo é inserido na quatidade de casos de teste
def test_CT03():
    inputs = ["-1", "1", "VQREQFGT", "2"]
    expected_output = ["TOPCODER"]
    with patch('builtins.input', side_effect=user_input_side_effects(inputs)):
        assert cifra_Cesar() == expected_output
# ID do caso de teste = CT04 | Testa como o programa lida com um número negativo como deslocamento da cifra
def test_CT04():
    inputs = ["2", "XSTGSHIV", "-2", "2", "ZWBGLZ", "25"]
    expected_output = ["VQREQFGT", "AXCHMA"]
    with patch('builtins.input', side_effect=user_input_side_effects(inputs)):
        assert cifra_Cesar() == expected_output
# ID do caso de teste = CT05 | Verifica a resposta do programa quando a senteça contém caracteres não alfabéticos
def test_CT05():
    inputs = ["1", "AB3DE", "ABCDE", "2"]
    expected_output = ["YZABC"]
    with patch('builtins.input', side_effect=user_input_side_effects(inputs)):
        assert cifra_Cesar() == expected_output
# ID do caso de teste = CT06 | Avalia como o programa responde com um valor não inteiro inserido no caso de teste
def test_CT06():
    inputs = ["ABC", "1", "ABCDE", "2"]
    expected_output = ["YZABC"]
    with patch('builtins.input', side_effect=user_input_side_effects(inputs)):
        assert cifra_Cesar() == expected_output
# ID do caso de teste = CT07 | Testa a capacidade do programa de lidar com uma sentença que excede o limite de 50 caracteres
def test_CT07():
    inputs = ["1", "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "1"]
    expected_output = ["ZABCDEFGHIJKLMNOPQRSTUVWXY"]
    with patch('builtins.input', side_effect=user_input_side_effects(inputs)):
        assert cifra_Cesar() == expected_output

if __name__ == "__main__":
    pytest.main()