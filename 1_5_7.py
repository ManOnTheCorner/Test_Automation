"""
Иерархическая структура + порядок элементов
С текстом вроде бы разобрались! Давайте теперь поиграем шрифтами на кнопках.
Найдите вторую кнопку (она с текстом "Edit") на карточке с котом и бананом.
Напишите для неё уникальный селектор, так, чтобы никакие другие элементы не выделялись.
"""
[name='banana'] .btn-group :nth-child(2)
{
    color:blue;
}






img {
	height: 100px;
}
.card-body {

    width: 200px;
    border= 1px;
    border: 1px solid rgba(0,0,0,.125);
    padding-right: 15px;
    padding-left: 15px;
    box-shadow: 0 0.25rem 0.75rem rgba(0, 0, 0, .05);
    border-top-left-radius: calc(.25rem - 1px);
    border-top-right-radius: calc(.25rem - 1px);
    margin-right: 15px;
    margin-left: 15px;
}

.btn-group {
    margin-bottom: 10px;
}


.column {
	display: flex;
}

* {
    color: black;
}