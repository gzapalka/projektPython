Automat biletowy MPK 

![Capture](https://user-images.githubusercontent.com/71458539/120379977-d4b60300-c320-11eb-853b-ab6a05d2b7bd.PNG)

1. Opis zadania:
Automat przechowuje informacje o monetach/banknotach znajdujqcych sip w nim (1, 2, 5, 10, 20, 50gr, 1, 2, 5, 10, 20, 50zt) [dziedziczenie: mozna napisa6 uniwersalnq klase PrzechowywaczMonet po kt6rej dziedziczy6 bedzie automat]. Okno z listą biletów w różnych cenach (jako przyciski). 
Wymagane bilety: 20-minutowy, 40-minutowy, 60-minutowy w wariantach normalnym i ulgowym. 
Możliwość wybrania wiecej niż jednego rodzaju biletu. Możliwość wprowadzenia liczby biletow. Po wybraniu biletu pojawia się okno z listą monet (przyciski) oraz możliwością dodania kolejnego biletu lub liczby biletów. lnterfejs ma dodatkowo zawierać pole na wybór liczby wrzucanych monet (domyślnie jedna). Po wrzuceniu monet, których wartość jest wieksza lub równa cenie wybranych biletów, automat sprawdza czy mote wydać resztę:
- Brak reszty/może wydać: wyskakuje okienko z informacjq o zakupach, wydaje reszte (dolicza wrzucone monety, odlicza wydane jako reszta), wraca do wyboru biletów.
- Nie mote wydać: wyskakuje okienko z napisem "Tylko odliczona kwota" oraz zwraca wrzucone monety. 


Testy 1. 
1. Bilet kupiony za odliczoną kwotę - oczekiwany brak reszty. \
2. Bilet kupiony płacąc więcej - oczekiwana reszta. 
3. Bilet kupiony placąc więcej, automat nie ma jak wydać reszty - oczekiwana informacja o błędzie oraz zwrócenie takiej samej liczby monet o tych samych nominałach, co wrzucone.
4. Zakup biletu placąc po 1gr - suma stu monet 1gr ma być rowna 1z1 (dla floatOw suma sto razy 0.01+0.01+...+0.01 nie będzie równa 1.0). Platności można dokonać za pomocq pętli for w interpreterze. 
5. Zakup dwóch różnych biletów naraz - cena powinna być suma. 
6. Dodanie biletu, wrzucenie kilku monet, dodanie drugiego biletu, wrzucenie pozostalych monet, zakup za odliczoną kwotę - oczekiwany brak reszty (wrzucone monety nie zerują się po dodaniu biletu). 
7. Próba wrzucenia ujemnej oraz niecałkowitej liczby monet (oczekiwany komunikat o błądzie). 

Link do githuba:
https://github.com/gzapalka/projektPython
