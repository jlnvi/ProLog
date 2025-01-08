# ProLog

Exercice 1 :

1. Qui est le père de Marc ? Jacques est le père de Marc.
   
![1](https://github.com/user-attachments/assets/bc8899b4-6242-45bb-83bc-ed6bec8e1038)

2.	Marc a-t-il des enfants ? Sophie est la fille de Marc

![2](https://github.com/user-attachments/assets/9d0dc616-9512-482b-b9de-eeaaa0ef8392)

Exercice 2 : 

Ajoutez une règle pour définir ce qu’est un grand-parent :
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).

1.	Qui est le grand-parent de Paul ? Il en a pas 

![4](https://github.com/user-attachments/assets/cd10957e-3479-4f12-900e-aebb7eaf776c)

2.	Jacques est-il grand-parent de Sophie ? Vrai
   
![3](https://github.com/user-attachments/assets/dee88cb3-dbec-486c-a05a-983a8af451e8)

Exercice 3 : 

Ajoutez une règle pour définir les frères et sœurs :
freresoeur(Y, Z) :- parent(X, Y), parent(X, Z), Y \= Z.

1.	Paul a-t-il des frères ou des sœurs ? Non, il en a pas
   ![5](https://github.com/user-attachments/assets/dda1ec24-33d9-4b3f-8b22-2541147ed47d)

   Exercice 4 : 
1.	Trouvez tous les hommes dans la base de données :

   ![6](https://github.com/user-attachments/assets/dbbd7bef-09e7-4527-91bb-c16084af5491)

  	
2.	Recherchez tous les parents de Sophie :

   ![7](https://github.com/user-attachments/assets/15734c7a-863e-43b2-8e68-1a50f863a271)
Exercice 5:

![9](https://github.com/user-attachments/assets/a89b7784-e4bf-40f6-93da-080496709be1)

Exercice 6 : 

![10](https://github.com/user-attachments/assets/695e9be3-0f6f-4ae9-9865-8ac54bf637b8)

Exercice 7 :

present([N|_], N).
present([_ | Queue], X) :- present(Queue, X).

Posez la question suivante pour trouver si Marie est présente dans la liste contenant pierre, marie et paul
![11](https://github.com/user-attachments/assets/0a308926-258b-4608-b71e-1b93fc1df8b1)

