class Rectangle: 
    # Sobrecarga
    def __init__(self, width, height):
        self._width = width
        self._height = height
    def __str__(self):
        return f"Rectangle(width={self._width}, height={self._height})"
    
    # Metodos
    def set_width(self, width):
        self._width = width

    def set_height(self, height):
        self._height = height

    def get_area(self):
        return self._width * self._height

    def get_perimeter(self):
        return 2*(self._width + self._height)

    def get_diagonal(self):
        return ((self._height)**2 + (self._width)**2)**0.5

    def get_picture(self):
        resultado = ""
        if self._height > 50 or self._width>50:
            return 'Too big for picture.'
        for i in range(self._height):
            for j in range(self._width):
                resultado+='*'
            resultado+="\n"
        return resultado

    def get_amount_inside(self, figure):
        count = 0
        area_other = figure.get_area()
        mi_area = self.get_area()

        flag = True
        while flag:
            mi_area -= area_other
            if mi_area >= 0:
                count +=1
            else:
                flag = False
        return count
    
    
class Square(Rectangle):
    def __init__(self, side):
        self._side = side
        super().__init__(side, side)
    
    def __str__(self):
        return f"Square(side={self._side})"
    
    def set_width(self, width):
        self._width = width
        self._side = width
    
    def set_height(self, height):
        self._height = height
        self._side = height
    
    def set_side(self, side):
        self._side = side
        self.set_width(side)
        self.set_height(side)


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
