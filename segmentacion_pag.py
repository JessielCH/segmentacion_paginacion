class ProcessSegment:
  def __init__(self, name, base, limit):
      self.name = name
      self.base = base
      self.limit = limit

class ProcessManager:
  def __init__(self):
      self.segments = {}

  def create_process_segment(self, name, base, limit):
      segment = ProcessSegment(name, base, limit)
      self.segments[name] = segment
      return segment

# Uso del ejemplo de paginación segmentada
process_manager = ProcessManager()
segment1 = process_manager.create_process_segment("Code", 0, 1024)
segment2 = process_manager.create_process_segment("Data", 2048, 512)

print(f"Segment 1: {segment1.name}, Base: {segment1.base}, Limit: {segment1.limit}")
print(f"Segment 2: {segment2.name}, Base: {segment2.base}, Limit: {segment2.limit}")
