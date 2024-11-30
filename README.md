
# Sistema de Registro de Pedidos

Este é um programa em Python que simula o registro de pedidos em um restaurante. Ele permite registrar itens do pedido e adicionar detalhes opcionais, como o nome do cliente, a mesa e o horário.

## Funcionalidades

- Adicionar múltiplos itens ao pedido.
- Fornecer detalhes adicionais do pedido (cliente, mesa, horário).
- Exibir um resumo do pedido ao final.

## Como Funciona

A função principal é `registrar_pedido`, que aceita:
- `*itens`: Lista de itens do pedido (argumentos posicionais).
- `**detalhes`: Informações adicionais do pedido (argumentos nomeados).

### Exemplo de Código

```python
def registrar_pedido(*itens, **detalhes):
    """
    Registra um pedido de restaurante com itens e detalhes opcionais.
    
    Args:
        *itens: Lista de itens do pedido.
        **detalhes: Informações opcionais (ex.: cliente, mesa, hora).
    """
    # Exibindo os itens pedidos
    print("Itens do Pedido:")
    for item in itens:
        print(f"- {item}")

    # Exibindo os detalhes adicionais, se houver
    if detalhes:
        print("\nDetalhes do Pedido:")
        for chave, valor in detalhes.items():
            print(f"{chave.capitalize()}: {valor}")

    print("\nPedido registrado com sucesso!")

# Exemplo de uso
registrar_pedido(
    "Pizza Margherita", "Refrigerante", "Sobremesa",
    cliente="João Silva", mesa=5, hora="20:30"
)
```

### Saída Esperada

```plaintext
Itens do Pedido:
- Pizza Margherita
- Refrigerante
- Sobremesa

Detalhes do Pedido:
Cliente: João Silva
Mesa: 5
Hora: 20:30

Pedido registrado com sucesso!
```

## Requisitos

- Python 3.8 ou superior.

## Como Executar

1. Copie o código para um arquivo Python (ex.: `registrar_pedido.py`).
2. Execute o script no terminal ou em um ambiente de desenvolvimento Python.

## Licença

Este projeto é livre para uso e modificação.
