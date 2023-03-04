class Order:
    def __init__(self, number, status):
        self.number = number
        self.status = status

    def __repr__(self) -> str:
        return f'<Order:number={self.number},status={self.status}>'