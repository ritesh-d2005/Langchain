from langchain_text_splitters import RecursiveCharacterTextSplitter,Language

code="""
  class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def main():
    calc = Calculator()
    print(calc.add(10, 5))
    print(calc.subtract(10, 5))
    print(multiply(10, 5))
    print(divide(10, 5))

if __name__ == "__main__":
    main()

"""
splitter=RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=200,
    chunk_overlap=0
)
chunks=splitter.split_text(code)
print(len(chunks))
print(chunks[0])

