# Висновок
Метод Бойєра-Мура послідовно перевершує як KMP, так і Рабіна-Карпа у всіх випадках. Він особливо ефективний як для існуючих, так і для неіснуючих підрядків.
KMP працює краще, ніж Rabin-Karp, але повільніше, ніж Boyer-Moore, особливо для неіснуючих підрядків.
Рабін-Карп є найповільнішим серед трьох алгоритмів у всіх випадках.

Виходячи з результатів тестування, алгоритм Бойєра-Мура є найкращим вибором для пошуку підрядків у заданих текстах. Він має найшвидший час виконання як для існуючих, так і для неіснуючих підрядків.
