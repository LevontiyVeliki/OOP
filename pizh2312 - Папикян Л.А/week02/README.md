Индивидуальное задание.
	Класс содержит целое число - количество снежинок. 
Класс включает методы перегрузки арифметических операторов сложения, вычитания, умножения и деления. Код этих методов должен выполнять увеличение или уменьшение количества снежинок на число n или в n раз.

Класс так же включает метод makeSnow(), который принимает сам объект и число снежинок в ряду. 

В ходе выполнения индивидуального задания Вариант 5 было создано два класса.
Класс Snow - родительский класс.
Класс Snow_baby - класс наследник.

От своего родителя класс Snow_baby унаследовал методы, позволяющие выполнять различные действия с кол-вом снежинок.

Была реализована защита переменных от внешнего вмешательства - инкапсуляция.
Было реализовано наследование - Snow и Snow_baby.
Был реализован абстрактный метод внутри класса Snow - Snow_man, его реализация уже была написана в классе Snow_baby.

Описание классов.
Snow - родительский класс, который хранит в себе переменные, отвечающие за хранение количества снежинок. Методы:
__call__ - отвечает за выполнение действий, которые необходимы при вызове класса, как функции. То есть просто заполняет стандартно переменные.
__init__ - отвечает за удобное заполнение переменных при объявлении переменной.
__mul__ - стандартный метод для умножения
__add__ - стандартный метод для сложения
__truediv__ - стандартный метод для деления
__sub__ - стандартный метод для вычитания

make_snow - метод, который выполняет основную задачу индивидуального задания, выводит "снегопад".
snow_man - метод, который является абстрактным.

Snow_baby - это дочерний класс, который по сути передаёт все методы на выполнение родительскому классу, а сам только реализует абстрактный метод snow_man.

Snow_man метод, который выводит в консоль небольшой рисунок снеговика.

