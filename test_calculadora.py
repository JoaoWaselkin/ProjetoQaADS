import pytest
from calculadora import Calculadora  # Importa a função Calculadora do arquivo calculadora.py

def test_soma():
    # Testa a operação de soma
    assert Calculadora('soma', 2, 3) == 5
    assert Calculadora('soma', -1, 1) == 0
    assert Calculadora('soma', 0, 0) == 0

def test_subtracao():
    # Testa a operação de subtração
    assert Calculadora('subtracao', 5, 3) == 2
    assert Calculadora('subtracao', -1, -1) == 0
    assert Calculadora('subtracao', 10, 10) == 0

def test_multiplicacao():
    # Testa a operação de multiplicação
    assert Calculadora('multiplicacao', 3, 4) == 12
    assert Calculadora('multiplicacao', -2, 5) == -10
    assert Calculadora('multiplicacao', 0, 10) == 0

def test_divisao():
    # Testa a operação de divisão
    assert Calculadora('divisao', 10, 2) == 5
    assert Calculadora('divisao', 9, 3) == 3
    assert Calculadora('divisao', 1, 2) == 0.5

def test_divisao_por_zero():
    # Testa a divisão por zero
    with pytest.raises(ValueError, match="Divisão por zero não permitida"):
        Calculadora('divisao', 10, 0)

def test_operacao_invalida():
    # Testa uma operação inválida
    with pytest.raises(ValueError, match="Operação inválida. Use 'soma', 'subtracao', 'multiplicacao' ou 'divisao'"):
        Calculadora('potencia', 2, 3)