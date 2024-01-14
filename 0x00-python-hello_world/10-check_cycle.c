#include "lists.h"

/**
 * check_cycle - checks cycle in a linked list
 *
 * @list: head of the linked list
 *
 * Return: 1 if it has cycle 0, otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *t = list;
	listint_t *h = list->next;

	while (h != NULL)
	{
		if (t->n == h->n)
			return (1);
		t = t->next;
		h = h->next;
		/* Move hare twice ahead*/
		h = h->next;
	}

	return (0);
}
