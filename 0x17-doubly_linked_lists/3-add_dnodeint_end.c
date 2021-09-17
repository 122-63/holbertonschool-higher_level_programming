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
	dlistint_t *end;


	if (head == NULL)
	{
		return NULL;
	}
	new_node = malloc(sizeof(dlistint_t));

	if (new_node == NULL)
	{
		return NULL;
	}
	new_node->n = n;
	new_node->next = NULL;
	if (*head == NULL)
	{
		new_node->prev = NULL;
		*head = new_node;
		return (new_node);
	}

	end = *head;
	while (end->next != NULL)
	{
		end = end->next;
	}
	end->next = new_node;
	end->prev = end;

	return (new_node);
}
