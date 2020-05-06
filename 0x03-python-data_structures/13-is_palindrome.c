#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
*add_nodeint - adds a new node at the beginning of a listint_t list
*@head: head of listint_t
*@n: int to add in listint_t list
*Return: address of the new element, or NULL if it failed
*/
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new;

	if (*head == NULL || head == NULL)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = n;
	new->next = *head;
	*head = new;
	return (new);
}
/**
*is_palindrome - identify if a syngle linked list is palindrome
*@head: head of listint_t
*Return: 1 if it is palindrome else 0
*/
int is_palindrome(listint_t **head)
{
	listint_t *head2 = *head;
	listint_t *aux = NULL;

	if (*head == NULL || head == NULL)
		return (0);
	while (head2->next)
	{
		add_nodeint(&aux, head2->n);
		head2 = head2->next;
	}
	print_listint(aux);
	if (head2->next == NULL)
		return (1);
	while (head2->next)
	{
		if (head2->n == aux->n)
		{
			head2 = head2->next;
			aux = aux->next;
		}
		else
			return (0);
	}
	return (1);
}
