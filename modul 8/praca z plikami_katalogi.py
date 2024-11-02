import os

# sprawdza czy istnieje dany plik lub folder względem folderu w którym obecnie jesteśmy
# makedirs tworzy katalogi, wchodzi coraz głębviej i tworzy wszystkie brakujące katalogi

# Kod działa poprawnie, mimo że używa ukośników w "złą" stronę, ponieważ Python automatycznie obsługuje ukośniki (/) jako separator ścieżki w systemach operacyjnych takich jak Windows.

# Ukośnik do przodu (/) jest uniwersalnym separatorem ścieżek, akceptowanym na wszystkich systemach operacyjnych (Windows, macOS, Linux).
# Na systemach Unixowych (macOS, Linux), ukośnik (/) jest naturalnym separatorem.
# Na Windows, mimo że standardowo używa się odwrotnego ukośnika (\), Python automatycznie konwertuje ukośniki do przodu (/) na odpowiedni format.
# Dzięki temu kod działa niezależnie od używanego systemu operacyjnego i typu separatora w ścieżce.



path = 'target/directory/is/inside'
if not os.path.exists(path):
    os.makedirs(path)