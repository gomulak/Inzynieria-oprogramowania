# Inzynieria-oprogramowania
Projekt stworzony w ramach przedmiotu Inżynieria oprogramowania na Uniwersytecie Gdańskim

## Wymagana dokumentacja

Wymagane dokumenty
1. Charakterystyka oprogramowania
a. Nazwa skrócona - jedno dwa słowa
b. Nazwa pełna
c. Krótki opis ze wskazaniem celów - jeden dwa akapity

2. Prawa autorskie.
a. Autorzy
b. Warunki licencyjne do oprogramowania wytworzonego przez grupę

3. Specyfikacja wymagań
| identyfikator | nazwa | opis | priorytet | kategoria |
| ----------- | -------------------- | ------------------------------------------------------------------------------------ | ------- | ------------ |
| `WYM-001` | Wprowadzenie danych | Użytkownik może wprowadzić parametry zwierzęcia, takie jak wiek, waga, płeć, typ rasy. | Wymagane	| Funkcjonalne |
| `WYM-002`	| Przesyłanie zdjęcia	| Użytkownik może przesłać zdjęcie zwierzęcia, aby aplikacja określiła jego gatunek.	| Wymagane |	Funkcjonalne |
| `WYM-003`	| Rozpoznawanie gatunku	| Aplikacja rozpoznaje, czy przesłane zdjęcie przedstawia kota, czy psa, przy użyciu sieci neuronowej. |	Wymagane | Funkcjonalne  |
| `WYM-004`	| Szacowanie czasu pobytu	| Aplikacja, na podstawie wprowadzonych parametrów i rozpoznania gatunku, szacuje czas pobytu w schronisku.	| Wymagane |	Funkcjonalne |
| `WYM-005`	| Wizualizacja wyników	| Wynik szacowania jest przedstawiany użytkownikowi w formie przejrzystego komunikatu (np. liczba dni, tygodni).	| Przydatne |	Funkcjonalne |
| `WYM-006`	| Historia szacowań	| Użytkownik może przejrzeć historię szacowań dla różnych zwierząt (zapis wyników w sesji).	| Opcjonalne |	Funkcjonalne |
| `WYM-007`	| Wydajność przetwarzania |	Wynik szacowania czasu pobytu zwierzęcia powinien być dostępny w czasie krótszym niż 3 sekundy.	| Wymagane |	Pozafunkcjonalne |
| `WYM-008`	| Dokładność klasyfikatora	| Klasyfikator czasu pobytu powinien osiągnąć dokładność powyżej 85% na podstawie testowych danych adoptowanych zwierząt.	| Wymagane |	Pozafunkcjonalne |
| `WYM-009` |	Instrukcja użytkowania |	Aplikacja dostarcza instrukcje użytkowania oraz wyjaśnia sposób szacowania czasu (pomoc online). |	Przydatne |	Funkcjonalne |
| `WYM-010` |	Walidacja danych |	Aplikacja sprawdza, czy wprowadzone dane są prawidłowe (np. wiek to liczba, zdjęcie w odpowiednim formacie).	| Wymagane |	Funkcjonalne |
| `WYM-011` |	WebScraping |	Aplikacja automatycznie pobiera zdefiniowane dane ze strony internetowej.	| Wymagane	| Funkcjonalne |

5. Architektura systemu/oprogramowania
a. Architektura rozwoju - stos technologiczny w postaci wykazu składającego się z: nazwy, przeznaczenia, numeru wersji - narzędzie programistyczne i technologie informatyczne wykorzystywane podczas rozwoju oprogramowania
b. Architektura uruchomieniowa - stos technologiczny w postaci wykazu składającego się z: nazwy, przeznaczenia, numeru wersji - narzędzie programistyczne i technologie informatyczne wymagane podczas
wykonywania oprogramowania lub systemu w środowisku docelowym

6. Testy
a. Scenariusze testów
b. Sprawozdanie z wykonania scenariuszy testów
