class DataSegment:
  def __init__(self, name, size):
      self.name = name
      self.size = size

class StorageSystem:
  def __init__(self):
      self.segments = {}

  def create_data_segment(self, name, size):
      segment = DataSegment(name, size)
      self.segments[name] = segment
      return segment

# Uso del ejemplo de segmentación
storage_system = StorageSystem()
segment1 = storage_system.create_data_segment("UserFiles", 1024)
segment2 = storage_system.create_data_segment("SystemFiles", 512)

print(f"Segment 1: {segment1.name}, Size: {segment1.size} MB")
print(f"Segment 2: {segment2.name}, Size: {segment2.size} MB")
