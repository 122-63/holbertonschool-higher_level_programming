#include "lists.h"
/**
 * add_dnodeint_end - new node at the end of a dlistint_t list.
 * @head:doble puntero
 * @n:variable
 * Return: the address of the new element, or NULL if it failed
 */
dlistint_t *add_dnodeint_end(dlistint_t **head, const int n)
{
	dlistint_t *new_node;
	dlistint_t *end = *head;

	if (head == NULL)
	{
		return (NULL);
	}
	new_node = malloc(sizeof(dlistint_t));

	if (new_node == NULL)
	{
		return (NULL);
	}
	if (end == NULL)
	{
		return (NULL);
	}
	while (end->next != NULL)
	{
		end = end->next;
	}
	end->next = new_node;

	new_node->n = n;
	new_node->next = NULL;
	new_node->prev = *head;
	new_node = NULL;

	return (new_node);
}
