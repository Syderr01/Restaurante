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
