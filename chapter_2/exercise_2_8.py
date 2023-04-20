flour_kcal_per_g = 364 / 100
pimento_kcal_per_g = 20.1 / 100
olive_kcal_per_g = 115 / 100
pork_kcal_per_g = 242.1 / 100
cheese_kcal_per_g = 402.5 / 100

pizza_flour_g = 200
pizza_pimento_g = 30
pizza_olive_g = 10
pizza_pork_g = 80
pizza_cheese_g = 20

pizza_kcal = (
    flour_kcal_per_g * pizza_flour_g +
    pimento_kcal_per_g * pizza_pimento_g +
    olive_kcal_per_g * pizza_olive_g +
    pork_kcal_per_g * pizza_pork_g +
    cheese_kcal_per_g * pizza_cheese_g
)

number_of_slice = 6 

pizza_kcal_per_slice = pizza_kcal / number_of_slice

print(pizza_kcal_per_slice)
