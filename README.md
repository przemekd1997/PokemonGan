# PokemonGan
Generowanie obrazów z pokemonami za pomocą GAN'ów

Główną część aplikacji po stronie użytkownika stanowi strona HTML połączona z arkuszami stylów CSS. Dodatkowo wykorzystywane są biblioteki Bootstrap w wersji 3.3.7 oraz JQuery w wersji 3.5.1, aby zapewnić iluzję witryny internetowej zawartej na jednej, pojedynczej stronie internetowej. Po wybraniu określonej metody uruchamiana jest funkcja JQuery. Powoduje ona zmianę klas nagłówków z metodami ich ciał. Sprawia to, że poprzednio wybrana metoda znika i pojawia się ciało nowo wybranej oraz jej nazwa się powiększa. Gdy najedzie się myszką na napis “Legenda” wyświetli się nam komunikat opisujący konkretną metodę. Po wciśnięciu przycisku losowania za pomocą JavaScript (JQuery) wysyłane jest zapytanie do odpowiedniego endpointu serwera. Po otrzymaniu odpowiedzi, dostarczone obrazy są zakodowane w Base64, a następnie są konwertowane do rozszerzenia jpg, po czym wyświetlone w odpowiednich miejscach.
Serwer został napisany w języku Python z użyciem micro frameworka Flask. Po uruchomieniu wczytuje każdy zapisany model oraz oczekuje na nadchodzące żądania. Po otrzymaniu zapytania uruchamiana jest odpowiednia metoda. Następnie losowane jest pięć seed’ów, które spełniają wymagania danego modelu. Sieć na ich podstawie generuje pięć obrazów. Następnie konwertowane są obrazy do postaci Base64. Każdy z takich obrazów jest umieszczony w obiekcie JSON, a następnie zwracany. Modele 1 i 3 korzystają z biblioteki TensorFlow 2. Model 2 korzysta z biblioteki PyTorch w wersji 1.7.1.

Na dysku Google https://drive.google.com/drive/folders/1Dbd6rOAyK5H2jeYME1I2OCB5NMV8vHzD?usp=sharing znajdują się 3 pliki (gan1, gan2, gan3) zostały one użyte to nauki każdego modelu. Dataset na którym były one uczone znajdują się w archiwum dataset. Archiwum Models zawiera w sobię wyniki każdego modelu po x epokach. Każdy model został przetrenowany 2 razy: na całym datasecie oraz tylko na tych obrazkach, których tło jest białe. Każda sesja treningowa trwała ok. 8 godzin. W ramach eksperymentu model 1 był dodatkowo trenowany przez 7 sesji po 8 godzin.

Model 1 bazowany jest na dwóch modelach z artykułów o GAN’ach (https://machinelearningmastery.com/how-to-develop-a-generative-adversarial-network-for-an-mnist-handwritten-digits-from-scratch-in-keras/ , https://www.wouterbulten.nl/blog/tech/getting-started-with-gans-2-colorful-mnist/) Obrazy generowane za pomocą Modelu 1 są dostępne w 3 wariantach:
- Powstałe w wyniku nauki na obrazach o różnokolorowych tłach - wybrany został generator po 210 epokach nauki.
- Powstałe w wyniku nauki na obrazach o białych tłach - wybrany został generator po 200 epokach nauki.
- Powstałe w wyniku 7 dniowej sesji treningowej po 8 godzin - na obrazach o różnokolorowych tłach.


Model 2 jest modelem kontrolnym. Pochodzi on z artykułu (https://medium.com/@yvanscher/using-gans-to-create-monsters-for-your-game-c1a3ece2f0a0) opisującego generowanie obrazów z potworami. Prawie cały model jest używany w niezmienionej formie. Jedyną zmianą jest generowanie obrazów kontrolnych podczas treningu. W oryginale autor generował zawsze za pomocą tego samego ziarna, jako że w pozostałych modelach generowany jest zawsze losowy to zmodyfikowałem lekko tę funkcję. Ten model został dodany, aby można było porównać wyniki pozostałych modeli z czymś co zostało stworzone przez osob, która ma większe doświadczenie z sieciami neuronowymi. Obrazy generowane za pomocą Modelu 2 są dostępne w 2 wariantach:
- Powstałe w wyniku nauki na obrazach o różnokolorowych tłach - wybrany został generator po 70 epokach nauki.
- Powstałe w wyniku nauki na obrazach o białych tłach - wybrany został generator po 90 epokach nauki.

Model 3 jest dalszą modyfikacją modelu 1. Wprowadziłem kilka zmiany w pętli uczącej oraz lekko zmieniłem generator. 
- W generatorze zamiast funkcji sigmoidalnej używam tangensa hiperbolicznego.
- Zmieniłem zakres liczb w ziarnie umieszczając w nim liczby ujemne.
- Zmieniłem batch size tak aby bardziej przypominał model 2
- Upewniłem się, że przy każdej epoce cały zbiór danych zostanie wykorzystany bez powtórzeń.

Obrazy generowane za pomocą Modelu 3 są dostępne w 2 wariantach:
- Powstałe w wyniku nauki na obrazach o różnokolorowych tłach - wybrany został generator po 100 epokach nauki.
- Powstałe w wyniku nauki na obrazach o białych tłach - wybrany został generator po 120 epokach nauki.
