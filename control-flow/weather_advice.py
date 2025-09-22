current_weather=input("What's the weather like today?(sunny/rainy/cold):").lower()
if current_weather in ["sunny","rainy","cold"]:
    match current_weather:
        case "sunny":
            print("Wear a t-shirt and sunglasses.")
        case "rainy":
            print("Don't forget your umbrella and raincoat.")
        case "cold":
            print("Make sure to wear a warm coat and scarf.")
else:
    print("Sorry,I don't have recommendation for this weather.")