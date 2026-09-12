def calcular_frete(valor_carrinho: float, regiao: str, valor_frete_base: float = None) -> float:
    """
    Calcula o valor do frete de acordo com o valor do carrinho, região e valor de frete base opcional.
    """
    # RB-05: IF price <= 0, THEN show the error 'Valor de carrinho inválido'
    if valor_carrinho <= 0:
        raise ValueError("Valor de carrinho inválido")

    # RB-01: WHEN the region is "Norte", the limit is R$300.00. For other regions, the limit is R$200.00.
    limit = 300.00 if regiao == "Norte" else 200.00

    # RF-02: WHEN the user calculates the shipping cost, THE SYSTEM SHALL set the shipping cost to zero.
    # (If the cart value meets the free shipping limit).
    if valor_carrinho >= limit:
        return 0.0

    # Determine base rate if not provided
    if valor_frete_base is None:
        base_rates = {
            "Norte": 50.0,
            "Nordeste": 25.0,
            "Sudeste": 15.0,
            "Sul": 9.0,
            "Centro-Oeste": 30.0
        }
        valor_frete_base = base_rates.get(regiao, 30.0)

    # Apply discounts:
    # RB-02: IF the shipping cost > than R$40.00, reduce by 10%
    if valor_frete_base > 40.00:
        shipping_cost = valor_frete_base * 0.90
    # RB-03: IF the shipping cost R$19.99 >= x >= R$29.99, reduce by 50%
    elif 19.99 <= valor_frete_base <= 29.99:
        shipping_cost = valor_frete_base * 0.50
    # RB-04: IF the shipping cost > R$10.00 x < R$19.99, reduce by 10%
    elif 10.00 < valor_frete_base < 19.99:
        shipping_cost = valor_frete_base * 0.90
    else:
        shipping_cost = valor_frete_base

    return round(shipping_cost, 2)
