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

	if (head == NULL)
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
	int value;

	if (head == NULL)
		return (0);
	if (*head == NULL || head2->next == NULL)
		return (1);
	while (head2 != NULL)
	{
		value = head2->n;
		add_nodeint(&aux, value);
		head2 = head2->next;
	}
	while (*head != NULL)
	{
		if ((*head)->n == aux->n)
		{
			*head = (*head)->next;
			aux = aux->next;
		}
		else
			return (0);
	}
	return (1);
}
