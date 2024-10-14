class ParkingLot:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.available_spots = capacity
        self.occupied_spots = 0

    def occupy_spot(self):
        if self.available_spots > 0:
            self.available_spots -= 1
            self.occupied_spots += 1
            print("Spot occupied successfully")
        else:
            print("No available parking spots")

    def free_spot(self):
        if self.occupied_spots > 0:
            self.available_spots += 1
            self.occupied_spots -= 1
            print("Spot freed successfully")
        else:
            print("No occupied parking spots")

class ParkingLotManager:
    def __init__(self):
        self.parking_lots = []

    def add_parking_lot(self, parking_lot):
        self.parking_lots.append(parking_lot)

    def list_parking_lots(self):
        for parking_lot in self.parking_lots:
            print(f"{parking_lot.name} - Capacity: {parking_lot.capacity}, Available Spots: {parking_lot.available_spots}")

# 创建停车场管理系统实例
parking_lot_manager = ParkingLotManager()

# 添加停车场
parking_lot1 = ParkingLot("Parking Lot 1", 50)
parking_lot2 = ParkingLot("Parking Lot 2", 100)
parking_lot_manager.add_parking_lot(parking_lot1)
parking_lot_manager.add_parking_lot(parking_lot2)

# 列出所有停车场
parking_lot_manager.list_parking_lots()

# 操作停车场
parking_lot1.occupy_spot()
parking_lot2.free_spot()

# 更新停车场状态
parking_lot_manager.list_parking_lots()