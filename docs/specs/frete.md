RF-01: THE SYSTEM SHALL calculate the shipping cost considering the rules below
RF-02: WHEN the user calculates the shipping cost, THE SYSTEM SHALL set the shipping cost to zero
RNF-01: THE SYSTEM SHALL calculate the shipping cost under 100ms

RB-01: WHEN the region is "Norte", the limit is R$300.00. For other regions, the limit is R$200.00
RB-02: IF the shipping cost > than R$40.00, THE SYSTEM SHALL reduce the price by 10%
RB-03: IF the shipping cost R$19.99 >= x >= R$29.99, THE SYSTEM SHALL reduce the price by 50%
RB-04: IF the shipping cost > R$10.00 x < R$19.99, THE SYSTEM SHALL reduce the price by 10%
RB-05: IF price <= 0, THEN show the error 'Valor de carrinho inválido'