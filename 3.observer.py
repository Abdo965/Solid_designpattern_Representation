class WeatherData:
    """Subject (Weather Station)"""
    def __init__(self):
        self.observers = []
        self.temperature = None
        self.humidity = None
        self.pressure = None
    
    def register_observer(self, observer):
        """Attach an observer to the subject"""
        self.observers.append(observer)

    def unregister_observer(self, observer):
        """Detach an observer from the subject"""
        self.observers.remove(observer)

    def notify_observers(self):
        """Notify all registered observers about data changes"""
        for observer in self.observers:
            observer.update(self.temperature, self.humidity, self.pressure)

    def set_measurements(self, temperature, humidity, pressure):
        """Update weather data and notify observers"""
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.notify_observers()

class Observer:
    """Interface for weather observers"""
    def update(self, temperature, humidity, pressure):
        pass

class NewsChannel(Observer):
    """Concrete observer (News Channel)"""
    def update(self, temperature, humidity, pressure):
        print("News Channel: Updating weather forecast...") 
        # Use data to update weather forecast

class WeatherApp(Observer):
    """Concrete observer (Weather App)"""
    def update(self, temperature, humidity, pressure):
        print("Weather App: Updating weather information...")
        # Use data to update weather information

# Example Usage
weather_data = WeatherData()
news_channel = NewsChannel()
weather_app = WeatherApp()

weather_data.register_observer(news_channel)
weather_data.register_observer(weather_app)

weather_data.set_measurements(25, 60, 1013)
