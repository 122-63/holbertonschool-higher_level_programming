#include "lists.h"
/**
 * get_dnodeint_at_index - returns the nth node of a dlistint_t linked list.
 * @head:puntero
 * @index:variable
 * Return: current
 */
dlistint_t *get_dnodeint_at_index(dlistint_t *head, unsigned int index)
{
	unsigned int i;
	dlistint_t *current = head;

	for (i = 1; i <= index; i++)
	{
		if (current == NULL)
		{
			return (NULL);
		}
		current = current->next;
	}
	return (current);
}
