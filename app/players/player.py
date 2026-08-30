from abc import abstractmethod


class Player:
    @abstractmethod
    def __init__(self, nickname: str) -> None:
        self.nickname = nickname

    def get_rating(self) -> int:
        pass

    def player_info(self) -> str:
        pass
