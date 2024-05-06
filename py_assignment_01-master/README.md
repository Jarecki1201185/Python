# Zadanie 1 (2 pkt)

Napisz moduł `square.py`, który narysuje kwadrat o zadanej długości boku (liczbie gwiazdek) oraz grubości ścianek, pusty w środku (patrz przykład poniżej dla parametrów 10 i 2).
Parametry przekaż z lini poleceń (argumenty funkcji main), sprawdzając ich poprawność.

Program ma:
* zwrócić 1 w przypadku błędnych argumentów,
* zwrócić 2 w przypadku nielogicznych argumentw (np grubość wieksza niż połowa długości),
* wypisać na ekranie żądany kwadrat i zwróci 0.

Przykładowy wynik obraz dla zewnętrznego rozmiaru 10 i grubości 2.
```
$ ./square.py 10 2
* * * * * * * * * *
* * * * * * * * * *
* *             * *
* *             * *
* *             * *
* *             * *
* *             * *
* *             * *
* * * * * * * * * *
* * * * * * * * * *
```

# Zadanie 2 (2 pkt)

Napisz moduł `compare.py`, który zapyta o dwa ciągi znaków oraz je porówna, nie zwracając uwagi na wielkość
liter (tzn. żeby traktował literę `A` i `a` jako takie same).

Program:
* zwróci 0 jeśli ciagi są takie same
* zwróci 1 jeśli ciagi się różnią

# Zadanie 3 (2 pkt)

Napisz moduł `palindrom.py`, który wczytuje zdanie, a potem sprawdza, czy jest palindromem (tzn. czytane
wspak brzmi tak samo). Przykład: `Kobyła ma mały bok`. Oczywiście trzeba tu ignorować spacje oraz
nie zwracać uwagi na wielkość liter (można wykorzystać funkcje z języka C++: `toupper`, `tolower`).

Program:
* zwróci 0 jeśli ciag jest palindromem
* zwróci 1 jeśli ciag nie jest palindromem

# Zadanie 4 (2 pkt)

W module `fibonnaci.py` napisz dwie funkcję `def fib_x(int) -> int` (zamień `x` wg wzorca poniżej) wyliczającą kolejne wyrażenia ciągu Fibonacciego:
1. w wersji rekurencyjnej (czyli funkcja wywołuje samą siebie) (funkcja `fib_r`),
1. w wersji z jedną pętlą for (funkcja `fib_l`).

W module `fibonacci.py` wykonywanym jako program wywołaj obydwie funkcje, zmierz czasy wykonania dla pierwszych `n` wartości (wykorzystaj klasy `chrono` z bibliteki C++). Wartosć `n` przekazywana jest jako argument programu.
Przykładowo, jeśli n=10 to policzony ma być sumaryczny czas dla `fibo_x(1)`, `fibo_x(2)`, ..., `fibo_x(10)`.

Program ma wypisać nazwę funkcji oraz czas wykonania obliczeń w sekundach.

Niech przykładowe wywołanie oraz wynik program wygląda tak:
```
./fibonacci.py 10
fib_r 1
fib_l 2
```

funkcja `fib_r` wykonała 100 obliczeń w czasie 1 s, a `fib_l` wykonała 100 obliczeń w czasie 2 s.

Zbadaj jak wygląda czas wykonania tych obliczeń w obu podejściach.

# Punktowanie

Każdy program uzyska:
1. Max 1 pkt za prawidłowe wykonanie działania
1. Max 1 pkt za prawidłowe jakość napisanego kodu
