class Page:
  def __init__(self, page_number, content):
      self.page_number = page_number
      self.content = content

class VirtualMemory:
  def __init__(self):
      self.pages = {}

  def create_page(self, page_number, content):
      page = Page(page_number, content)
      self.pages[page_number] = page
      return page

# Uso del ejemplo de paginación
virtual_memory = VirtualMemory()
page1 = virtual_memory.create_page(0, "Page 1 Data")
page2 = virtual_memory.create_page(1, "Page 2 Data")

print(f"Page 1: Number={page1.page_number}, Content={page1.content}")
print(f"Page 2: Number={page2.page_number}, Content={page2.content}")
