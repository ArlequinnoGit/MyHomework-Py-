import hashlib
from time import sleep


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self._set_password(password)
        self.age = age

    def _set_password(self, password):
        """Хеширует пароль."""
        self.password_hash = int(hashlib.sha256(password.encode()).hexdigest(), 16)

    @property
    def password(self):
        return self.password_hash

    def __repr__(self):
        return f"User({self.nickname}, {self.password}, {self.age})"


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __repr__(self):
        return f"Video({self.title}, {self.duration}, {self.time_now}, {self.adult_mode})"


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        """Пытается войти под пользователем с указанным ником и паролем."""
        for user in self.users:
            if user.nickname == nickname and user.password == int(
                hashlib.sha256(password.encode()).hexdigest(), 16):
                self.current_user = user
                break
        else:
            print("Неправильный логин или пароль.")

    def register(self, nickname, password, age):
        """Регистрирует нового пользователя, если такого еще нет."""
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует.")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.log_in(nickname, password)

    def log_out(self):
        """Выходит из аккаунта текущего пользователя."""
        self.current_user = None

    def add(self, *videos):
        """Добавляет новые видео, если таких еще нет."""
        for video in videos:
            if any(video.title == existing_video.title for existing_video in self.videos):
                continue
            self.videos.append(video)

    def get_videos(self, search_word):
        """Ищет видео по ключевому слову и возвращает список совпадающих названий."""
        search_word = search_word.lower()
        matching_titles = [
            video.title
            for video in self.videos
            if search_word in video.title.lower()
        ]
        return matching_titles

    def watch_video(self, title):
        """Выводит видео на экран, если оно существует и пользователь соответствует требованиям."""
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return
                for second in range(video.time_now + 1, video.duration + 1):
                    print(f"Воспроизведение: {second}/{video.duration}")
                    sleep(1)
                print("Конец видео")
                video.time_now = 0
                return
        print("Видео не найдено")

if __name__ == "__main__":
            ur = UrTube()
            v1 = Video('Лучший язык программирования 2024 года', 200)
            v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

            # Добавление видео
            ur.add(v1, v2)

            # Проверка поиска
            print(ur.get_videos('лучший'))  # ['Лучший язык программирования 2024 года']
            print(ur.get_videos('ПРОГ'))  # ['Лучший язык программирования 2024 года']

            # Проверка на вход пользователя и возрастное ограничение
            ur.watch_video('Для чего девушкам парень программист?')  # Войдите в аккаунт, чтобы смотреть видео
            ur.register('vasya_pupkin', 'lolkekcheburek', 13)
            ur.watch_video('Для чего девушкам парень программист?')  # Вам нет 18 лет, пожалуйста покиньте страницу
            ur.register('urban_pythonist', '123', 25)
            ur.watch_video('Для чего девушкам парень программист?')  # Воспроизведение: 1/10 ... Конец видео

            # Проверка входа в другой аккаунт
            ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
            print(ur.current_user)  # Пользователь vasya_pupkin уже существует.

            # Попытка воспроизведения несуществующего видео
            ur.watch_video('Лучший язык программирования 2024 года!')  # Видео не найдено