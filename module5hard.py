import time


class User:
    """
    User class containing attributes: nickname, password and age
    """

    def __init__(self, nickname, password, age=99):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __eq__(self, other):
        return (self.nickname == other.nickname
                and hash(self.password) == hash(other.password))

    def __str__(self):
        return self.nickname

    def get_nickname(self):
        return self.nickname


class Video:

    def __init__(self, title, duration, time_now=0, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __eq__(self, other):
        return self.title == other.title

    def __repr__(self):
        return str(self)

    def __str__(self):
        return self.title

    def get_title(self):
        return self.title


class UrTube:

    def __init__(self):

        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, login, password):
        search_user = User(login, password)
        for user in self.users:
            if user == search_user:
                self.current_user = user

    def register(self, nickname, password, age):
        for user in self.users:
            if user.get_nickname() == nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for video in args:
            if video in self.videos:
                continue
            else:
                self.videos.append(video)

    def get_videos(self, searching_value):
        found_videos = []
        for video in self.videos:
            if searching_value.lower() in video.get_title().lower():
                found_videos.append(video)

        return found_videos

    def watch_video(self, viewing_video):
        if self.current_user:
            if self.current_user.age < 18:
                print('Вам нет 18 лет, пожалуйста покиньте страницу')
            else:
                for video in self.videos:
                    if viewing_video in video.title:
                        for i in range(1, 11):
                            print(i, end=' ')
                            time.sleep(1)
                        print('Конец видео')
        else:
            print('Войдите в аккаунт, чтобы смотреть видео')


if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')
