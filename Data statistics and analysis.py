class ParkingData:
    def __init__(self, parking_duration, revenue):
        self.parking_duration = parking_duration
        self.revenue = revenue

class DataAnalytics:
    def __init__(self):
        self.parking_data = []

    def add_parking_data(self, parking_data):
        self.parking_data.append(parking_data)

    def average_parking_duration(self):
        total_duration = sum(data.parking_duration for data in self.parking_data)
        average_duration = total_duration / len(self.parking_data)
        return average_duration

    def total_revenue(self):
        total_revenue = sum(data.revenue for data in self.parking_data)
        return total_revenue

# 创建数据统计和分析对象
data_analytics = DataAnalytics()

# 添加停车数据
data1 = ParkingData(2, 10)
data2 = ParkingData(3, 15)
data_analytics.add_parking_data(data1)
data_analytics.add_parking_data(data2)

# 计算平均停车时长和总收入
average_duration = data_analytics.average_parking_duration()
total_revenue = data_analytics.total_revenue()

print(f"Average parking duration: {average_duration} hours")
print(f"Total revenue: ${total_revenue}")