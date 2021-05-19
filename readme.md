1. Program ProjZal pełni rolę serwera danych - jest aplikacją internetową która ma przechwytywać , zapisywać i wyświetlać tekstowo oraz graficznie 
   dane pobrane z urządzenia - klienta . Urządzeniem tym może być mikrokomputer Raspberry Pi .
   Dzięki zastosowaniu API istnieje  dowolność urządzenia które będzie wysyłało dane.  
   Klient wysyła do serwera ProjZal słownik z danymi  (z czterema odczytami temperatur , oraz datą i godziną pomiaru)
   W bazie danych parametry te są zapisywane pod nazwą endpointu na który jest wysyłany słownik metodą POST.
   Standardowo endpoint'y te mają nazwę channel_*.
   Do symulacji pracy mikorokomputera wysyłającego dane ( wysyłania danych testowych) służy dołączony program client.py
   W celu testowym  w bazie danych są zostały wprowadzone dane z datą 04.04.2021
   
2. Aplikacja korzysta z wersji 3.9.1 
3. Program został umieszczony na platformie HEROKU pod adresem  https://projzal.herokuapp.com/
   (user - testowy ; hasło - testowy; Dostęp do API : 'X-User-Token': 'HsudXwo.token.uzytkownika' )
4. Jest to wersja demonstracyjna programu

