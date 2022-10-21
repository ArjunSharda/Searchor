from searchor import Engine

Engine.new("Custom", "https://www.example.com/search?q=")

print(Engine.Custom.search("Hello, World!"))
