#!/usr/bin/env python
# coding: utf-8

# ### Задание на 4 занятие
# #### В программном коде дописать пропуски так, чтобы были выполнены следующие задания:

# In[1]:


class Sharp(object):
    def __init__(self, x, y, screen=[]):
        self._x = x 
        self._y = y
        self.screen = screen if screen else [['.']*40 in range(40)]
        
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __lt__(self, other): #<
        return self.x < other.x and self.y < other.y
    
    def __le__(self, other): #<=
        return self.x <= other.x and self.y <= other.u
    
    def __gt__(self, other):
        return not self.__le__(other)
    
    def __ge__(self, other):
        return not self.__lt__(other)
    
    @property
    def print_screen(self):
         print("\n".join(["".join(line) for line in self.screen]))
                           
    def clear_screen(self):
        self.screen=[['.'] * 40 for _ in range(40)]
            
    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
              
    def draw(self):
        self.screen[self._y][self._x]='*'
        
    def __str__(self):
        return f'Это точка с координатами ({self.x};{self.y})'
    
    @property
    def area(self):
        return 0
    
    def up(self):
        self._y -= 1
        self.draw()
        
    def down(self):
        self._y += 1       
        self.draw()
        
    def right(self):
        self._x += 1
        self.draw()
        
    def left(self):
        self._x -= 1
        self.draw()


# In[2]:


class Rectangle(Sharp):
    
    def __init__(self,x,y,w,h,screen):
        super().__init__(x,y,screen)
        self.h = h 
        self.w = w
        
    def color(self):
        for x1 in range(self.x, self.x+self.w):
            type(self).screen[self.y][x1]='*'
            type(self).screen[self.y+self.h-1][x1]='*'
        for x1 in range(self.y, self.y+self.h):
            type(self).screen[x1][self.x]='*'
            type(self).screen[x1][self.x+self.w-1]='*'
        
    def draw(self):
        for j in range(self.y, self.y + self.h):
            for i in range(self.x, self.x + self.w):
                self.screen[j - 1][i - 1]= ' '
                
    @property
    def area(self):
        return self.h * self.w
    
    def __str__(self):
        return f'Это прямоугольник с шириной {self.w} и высотой {self.h}'
            


# In[3]:


class Square(Rectangle):
    def __init__(self, x, y, w, screen):
        super().__init__(x, y, w, w, screen)
    def __str__(self):
        return f'Это квадрат со стороной {self.w}'


# In[4]:


class Triangle(Sharp):   
    def __init__(self, sh1, sh2, sh3, screen=[]):        
        self.sh1 = sh1
        self.sh2 = sh2
        self.sh3 = sh3
        self.screen = self.screen = screen if screen else [['.'] * 40 in range(40)]
                
    def line(self,sh1,sh2):
        L = (max(abs(sh2.x - sh1.x),abs(sh2.y - sh1.y)))+1
        dx = (sh2.x-sh1.x) / L if L!=0 else 0
        dy = (sh2.y-sh1.y) / L if L!=0 else 0
        y = sh1.y
        x = sh1.x
        for i in range(0,L):
            self.screen[round(y)][round(x)]='*'
            y += dy
            x += dx
        self.screen[sh2.y][sh2.x]='*'  
        
    def draw(self):
        self.line(self.sh2, self.sh1)
        self.line(self.sh3, self.sh1)
        self.line(self.sh2, self.sh3)
    
    @property
    def area(self):
        from math import sqrt
        a=sqrt((self.sh1.x-self.sh2.x)**2+(self.sh1.y-self.sh2.y)**2)
        b=sqrt((self.sh1.x-self.sh3.x)**2+(self.sh1.y-self.sh3.y)**2)
        c=sqrt((self.sh2.x-self.sh3.x)**2+(self.sh2.y-self.sh3.y)**2)
        p=(a+b+c)/2
        s=sqrt(p*(p-a)*(p-b)*(p-c))
        return s
    
    def __str__(self):
        from math import sqrt
        a=sqrt((self.sh1.x-self.sh2.x)**2+(self.sh1.y-self.sh2.y)**2)
        b=sqrt((self.sh1.x-self.sh3.x)**2+(self.sh1.y-self.sh3.y)**2)
        c=sqrt((self.sh2.x-self.sh3.x)**2+(self.sh2.y-self.sh3.y)**2)
        return f'Это треугольник с длинами сторон {a}, {b} и {c}'


# In[5]:


class Line(object):
    def __init__(self, sh1, sh2, screen=[]):
        self.sh1 = sh1
        self.sh2 = sh2
        self.screen = screen if screen else [['.']*40 in range(40)]
        
    def draw(self):
        L = (max(self.sh2.x-self.sh1.x,self.sh2.y-self.sh1.y))+1
        dx = (self.sh2.x-self.sh1.x) / L if L!=0 else 0
        dy = (self.sh2.y-self.sh1.y) / L if L!=0 else 0
        y = self.sh1.y
        x = self.sh1.x
        for i in range(0,L):
            self.screen[round(y)][round(x)] = ' '
            y += dy
            x += dx
        self.screen[self.sh2.y][self.sh2.x] = ' '  
        
    def print_screen(self):
        for i in self.screen:
            for j in i:
                print(j, end='')
            print()
        
    def __str__(self):
        from math import sqrt
        a=sqrt((self.sh1.x-self.sh2.x)**2+(self.sh1.y-self.sh2.y)**2)
        return f'Линия длины {a}'


# In[6]:


def print_screen(screen):
    for i in range(len(screen)):
        print(''.join(screen[i])) 


# In[7]:


my_screen = [['&'] * 40 for _ in range(40)]       


# In[12]:


sh = Sharp(10, 1, my_screen)
r = Rectangle(2, 5, 4, 3, my_screen)

tr3 = Triangle(Sharp(10, 35, my_screen),Sharp(17, 25, my_screen),Sharp(36, 25, my_screen), my_screen)
sq = Square(10, 15, 5, my_screen) 
l = Line(Sharp(15, 3, my_screen), Sharp(30, 18, my_screen), my_screen)
l2 = Line(Sharp(30, 3, my_screen), Sharp(16, 18, my_screen), my_screen)


# In[13]:


for i in (sh,r,sq, tr3, l, l2):
    i.draw()


# In[11]:


print_screen(my_screen)


# In[ ]:





# In[ ]:




