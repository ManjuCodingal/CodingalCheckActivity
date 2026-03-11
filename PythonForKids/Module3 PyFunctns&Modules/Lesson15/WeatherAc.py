def weather_condition(spring, autumn):
    print("\nWeather Summary:")
    print("🌸 Spring weather:", spring)
    print("🍂 Autumn weather:", autumn)

# Take user input for each season
spring_weather = input("Enter the weather in spring: ")
autumn_weather = input("Enter the weather in autumn: ")

# Call the function with user inputs
weather_condition(spring_weather, autumn_weather)