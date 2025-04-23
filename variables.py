"""
Type (int, str, float, bool, list, set, dict, tuple, )
Değişken-Variable
    LValue

Name(ismi) ->
1. Builtin isimlere dikkat et
2. alpha (A-Za-z) başlayacak; devamında alphanumeric (A-Za-z0-9)
3. başlangıçta yada herhangi bir yerde space (boşuk) kullanamazsınız
4. Case Sensitive dir yani a = 5, A = 6, elma=8, Elma=88, eLma=9

* Variable tanımlarken öncelikle LValue olacak.
* Değer atamanız lazım (= assignment operator) (değer atama operatorü)

RValue alıyor LValue nun içine koyuyor

Type nı belirtmeniz lazım
int a = 5; C, C++, Java Static typing)

Ama Python: Dynamic Typing

Implicit

Explicit
"""
a = 5
b = 9999
c = -123456
d = 0
print(type(a))

a = "Python"
print(type(a))


