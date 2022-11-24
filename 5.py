# общий метод, который будут использовать все наследники этого класса
class ChessPiece(ABC):
    def draw(self):
        print("Drew a chess piece")
    # абстрактный метод, который нужно необходимо переопределять для каждого предкласса
    @abstractmethod
    def move(self):
        pass
class queen(ChessPiece):
    def move(self):
        print("queen move")
queen.move("ds")