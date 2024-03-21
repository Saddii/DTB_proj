# DTBpr






Projekt Bazy Danych 2023 - Dokumentacja

Data: 30 czerwca 2023

Spis treści:

    Spis użytych technologii

    Lista plików i opis zawartości

    Instrukcja uruchamiania

    Opis zależności funkcyjnych z wyjaśnieniem

    Spis użytych technologii
    Podczas tworzenia projektu wykorzystano Pythona, MariaDb oraz Git.

1.1 Python
Wykorzystane biblioteki:

    datetime,
    pandas,
    mysql,
    cvs,
    math,
    numpy,
    random,
    itertools,
    matplotlib,
    os.

1.2 MariaDb
Używany jako dialekt MySQL do komunikacji z bazą danych.

1.3 Git
Narzędzie do kontroli wersji i pracy w grupie.

    Lista plików i opis zawartości
    Projekt zawiera 4 skrypty w folderze głównym:

    bob the builder.py,
    drop all,
    Analiza danych.py,
    Generator.py,
    Oraz plik "dokumentacja.pdf".

    Instrukcja uruchamiania
    Aby stworzyć nową bazę i wypełnić ją danymi, należy uruchomić plik "bob the builder.py".
    Aby wygenerować analizę danych, uruchom plik "Analiza danych.py". Plik "Generator.py" tworzy raport w formacie PDF na podstawie analizy.

    Opis zależności funkcyjnych z wyjaśnieniem
    W projekcie wykorzystano wiele tabel, takich jak "customers", "games", "inventory" itd., które są powiązane kluczami głównymi i obcymi, aby przechowywać dane o klientach, grach, wynajmie itp.
